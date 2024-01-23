structDef = ["S", 14, 14]   # identifier of the struct problems, total number of rules, number of strict rules (not warning)
#########################
####   REGRAS
#########################
msg_Srule01 = "ERRO "+structDef[0]+"01: Sentença sem identificador (verificação interrompida)."
msg_Srule02 = "ERRO "+structDef[0]+"02: Sentença sem texto original (verificação interrompida)."
msg_Srule03 = "ERRO "+structDef[0]+"03: Linha inesperada - meta informação sem # (verificação interrompida)."
msg_Srule04 = "ERRO "+structDef[0]+"04: Linha inesperada entre linhas de tokens (verificação interrompida)."
msg_Srule05 = "ERRO "+structDef[0]+"05: Erro de formato desconhecido (verificação interrompida)."
msg_Srule06 = "ERRO "+structDef[0]+"06: Token sem os 10 campos obrigatórios (verificação interrompida)."
msg_Srule07 = "ERRO "+structDef[0]+"07: Sentença original incompatível com os tokens informados."
msg_Srule08 = "ERRO "+structDef[0]+"08: Numeração errada de tokens de contração (token inexistente)."
msg_Srule09 = "ERRO "+structDef[0]+"09: Numeração errada de tokens de contração (números errados)."
msg_Srule10 = "ERRO "+structDef[0]+"10: Numeração errada de tokens de contração (números fora de sequência)."
msg_Srule11 = "ERRO "+structDef[0]+"11: Numeração errada de tokens (números fora de sequência)."
msg_Srule12 = "ERRO "+structDef[0]+"12: Numeração errada de tokens (relação de dependência com token inexistente)."
msg_Srule13 = "ERRO "+structDef[0]+"13: Multíplos tokens marcados como root na sentença (token {} também marcado como root)."
msg_Srule14 = "ERRO "+structDef[0]+"14: Sentença sem token root."
msg_Srule15 = "ERRO "+structDef[0]+"15: Token sem caminho até o token root da sentença."
msg_Srule16 = "ERRO "+structDef[0]+"16: Token com mais do que uma dependência."


def goodFormat(name, dump, samples):
    infile = open(name, "r")
    status, SID, text, rLine = "start", "none", "none", 0
    for line in infile:
        rLine += 1
        if (status == "start") or (status == "waiting"):
            if (line[0] == "#"):
                status = "meta"
                if (line[:12] == "# sent_id = "):
                    SID = line[12:-1]
                elif (line[:9] == "# text = "):
                    text = line[9:-1]
            elif (line[:-1].strip() != ""):
                if (status == "start"):
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule05), file=dump)
                    return "notCoNLL-U", rLine
                else:
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule03), file=dump)
                    return "unexpec", rLine
        elif (status == "meta"):
            if (line[0] == "#"):
                if (line[:12] == "# sent_id = "):
                    SID = line[12:-1]
                elif (line[:9] == "# text = "):
                    text = line[9:-1]
            elif (line[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
                status = "tokens"
                fields = line[:-1].split("\t")
                if (len(fields) != 10):
                    if (SID != "none"):
                        print("{}\t{}\t{}".format(SID, "linha: "+rLine, msg_Srule06), file=dump)
                        return "tenFields_"+SID, rLine
                    else:
                        print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule06), file=dump)
                        return "tenFields", rLine
            else:
                if (SID != "none"):
                    print("{}\t{}\t{}".format(SID, "linha: "+rLine, msg_Srule03), file=dump)
                    return "unexpec_"+SID, rLine
                else:
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule03), file=dump)
                    return "unexpec", rLine
        elif (status == "tokens"):
            if (line[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]):
                status = "tokens"
                fields = line[:-1].split("\t")
                if (len(fields) != 10):
                    if (SID != "none"):
                        print("{}\t{}\t{}".format(SID, "linha: "+rLine, msg_Srule06), file=dump)
                        return "tenFields_"+SID, rLine
                    else:
                        print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule06), file=dump)
                        return "tenFields", rLine
            elif (line[:-1].strip() == ""):
                status = "waiting"
                if (SID == "none") and (text == "none"):
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule01), file=dump)
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule02), file=dump)
                    return "missSIDtext", rLine
                elif (SID == "none"):
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule01), file=dump)
                    return "missSID", rLine
                elif (text == "none"):
                    print("{}\t{}\t{}".format(SID, "linha: "+rLine, msg_Srule02), file=dump)
                    return "missText_"+SID, rLine
                SID, text = "none", "none"
            else:
                if (SID != "none"):
                    print("{}\t{}\t{}".format(SID, "linha: "+rLine, msg_Srule04), file=dump)
                    return "unexpec_"+SID, rLine
                else:
                    print("{}\t{}\t{}".format("?", "linha: "+rLine, msg_Srule04), file=dump)
                    return "unexpec", rLine
    infile.close()
    return "ok"

def goodNumbers(b, dump, samples):
    acc = 0
    i = 1
    for j in range(len(b[4])):
        if ("-" in b[4][j][0]):
            if (j+2 > len(b[4])):
                acc += 1
                '''Regra 08 - Numeração errada de tokens concatenados (token inexistente).'''
                print("{}\t{}\t{}".format(b[0], b[4][j][0], msg_Srule08), file=dump)
            elif (b[4][j][0] != b[4][j+1][0]+"-"+b[4][j+2][0]):
                acc += 1
                '''Regra 09 - Numeração errada de tokens concatenados (números errados).'''
                print("{}\t{}\t{}".format(b[0], b[4][j][0], msg_Srule09), file=dump)
            else:
                dash = b[4][j][0].find("-")
                first = b[4][j][0][:dash]
                second = b[4][j][0][dash+1:]
                if (first != str(i)) or (second != str(i+1)):
                    acc += 1
                    '''Regra 10 - Numeração errada de tokens concatenados (números fora de sequência).'''
                    print("{}\t{}\t{}".format(b[0], b[4][j][0], msg_Srule10), file=dump)
        else:
            if (b[4][j][0] != str(i)):
                acc += 1
                '''Regra 11 - Numeração errada de tokens (números fora de sequência).'''
                print("{}\t{}\t{}".format(b[0], b[4][j][0], msg_Srule11), file=dump)
            try:
                if (eval(b[4][j][6]) > b[2]):
                    acc += 1
                    '''Regra 12 - Numeração errada de tokens (relação de dependência com token inexistente).'''
                    print("{}\t{}\t{}".format(b[0], b[4][j][0], msg_Srule12), file=dump)
            except:
                acc += 1
                '''Regra 12 - Numeração errada de tokens (relação de dependência com token inexistente).'''
                print("{}\t{}\t{}".format(b[0], b[4][j][0], msg_Srule12), file=dump)
            i += 1
    return acc

def wellformedTree(b, dump, samples):
    acc = 0
    root = ""
    for tk in b[4]:
        if (tk[6] == "0") and (root == ""):
            root = tk[0]
        elif (tk[6] == "0") and (root != ""):
            acc += 1
            '''Regra 13 - Multíplos tokens marcados como root na sentença (token {} também marcado como root).'''
            print("{}\t{}\t{}".format(b[0], tk[0], msg_Srule13.format(root)), file=dump)
            root += ", "+tk[0]
    if (root == ""):
        acc += 1
        '''Regra 14 - Sentença sem token root.'''
        print("{}\t{}\t{}".format(b[0], str(b[2]-1), msg_Srule14), file=dump)
    else:
        tokens = [0]*(b[2]+1)
        search = ["0"]
        while (search != []):
            idx = search.pop()
            for tk in b[4]:
                if (tk[6] == idx):
                    tokens[eval(tk[0])] += 1
                    if (tokens[eval(tk[0])] == 1):
                        search.append(tk[0])
        for i in range(1,len(tokens)):
            if (tokens[i] == 0):
                acc += 1
                '''Regra 15 - Token sem caminho até o token root da sentença.'''
                print("{}\t{}\t{}".format(b[0], str(i), msg_Srule15), file=dump)
            elif (tokens[i] > 1):
                acc += 1
                '''Regra 16 - Token com mais do que uma dependência.'''
                print("{}\t{}\t{}".format(b[0], str(i), msg_Srule16), file=dump)
    return acc
