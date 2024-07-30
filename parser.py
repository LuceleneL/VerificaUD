# rules to be in the porttinari_check verificador
#
# function to be accessed:
#
#   checkSent(b, dump, rep) - it performs all verifications over the sentence 'b',
#                             it prints out the report in the output file 'dump'
#                             it samples the sentences with problems at the 'rep'
#                      - it returns:
#                         - an array with verifications perceived to each rule
#                         - the sentence total number of verifications perceived

parserDef = ["P", 69, 61]   # identifier of the parser problems, total number of rules, number of strict rules (not warning)
#########################
####   REGRAS
#########################
msg_Prule01 = "ERRO "+parserDef[0]+"01: Todo token dependente de det é DET (o inverso não é verdadeiro)."
msg_Prule02 = "ERRO "+parserDef[0]+"02: Todo token dependente de amod é ADJ (o inverso não é verdadeiro)."
msg_Prule03 = "ERRO "+parserDef[0]+"03: Todo token dependente de iobj é PRON, tem feature Case=Dat e lema: ['me', 'te', 'se', 'lhe', 'nos', 'vos', 'lhes'] (o inverso não é verdadeiro)."
msg_Prule04 = "ERRO "+parserDef[0]+"04: Todo token dependente de obj que é PRON, tem feature Case=Acc e lema ['me', 'te', 'se', 'o', 'a', 'nos', 'vos', 'os', 'as', 'lo', 'la', 'los', 'las', 'no', 'na', 'nos', 'nas']."
msg_Prule05 = "ERRO "+parserDef[0]+"05: Nenhum ADP é head de relação - Exceções: pode ser head da relação fixed (e se for de fixed, pode ser de punct, cc e conj também), pode ser head de conj se o dependente for ADP, pode ser head de cc se o token ADP for dependente de conj."
msg_Prule06 = "ERRO "+parserDef[0]+"06: Nenhum token CCONJ é head de relação - Exceção: pode ser head da relação fixed (e se for de fixed, pode ser de punct também), pode ser head de conj dependente de CCONJ."
msg_Prule07 = "ERRO "+parserDef[0]+"07: Nenhum SCONJ é head de relação - Exceções: pode ser head da relação fixed (e se for de fixed, pode ser de punct, cc e conj também), pode ser head de conj se o dependente for SCONJ, pode ser head de cc se o token SCONJ for dependente de conj."
msg_Prule08 = "ERRO "+parserDef[0]+"08: Nenhum DET é head de relação - Exceções: pode ser head da relação fixed (e se for de fixed, pode ser de punct, cc e conj também), pode ser head de conj se o dependente for DET, pode ser head de cc se o token DET for dependente de conj."
msg_Prule09 = "ERRO "+parserDef[0]+"09: Um token AUX não pode ser head de relação (exceto punct) se for dependente de aux, aux:pass ou cop."
msg_Prule10 = "ERRO "+parserDef[0]+"10: Nenhum token dependente de fixed é head de relação."
msg_Prule11 = "ERRO "+parserDef[0]+"11: Todo token head de case só pode ser PROPN, NOUN, PRON, ADJ, NUM, X, INTJ, SYM ou ADV."
msg_Prule12 = "ERRO "+parserDef[0]+"12: Nenhum token SCONJ pode ser dependente de nsubj, nsubj:pass, nsubj:outer, csubj, csubj:pass, csubj:outer e obj."
msg_Prule13 = "ERRO "+parserDef[0]+"13: Todo token dependente de cop só pode ter lema 'estar' ou 'ser'."
msg_Prule14 = "ERRO "+parserDef[0]+"14: Dois ou mais tokens dependentes de case não podem apontar para um mesmo token head."
msg_Prule15 = "ERRO "+parserDef[0]+"15: Nenhum token PRON pode ser dependente de mark, exceto se for head de fixed."
msg_Prule16 = "ERRO "+parserDef[0]+"16: Todo token dependente de aux só pode ter lema = 'ser', 'estar', 'ter', 'haver', 'ir' e 'vir' caso seja vir+Ger ou vir+'a'+Inf."
msg_Prule17 = "ERRO "+parserDef[0]+"17: Todo token que é ponto final não pode ter como head um token que não é head de outras relações."
msg_Prule18 = "ERRO "+parserDef[0]+"18: Todo token dependente de nummod só pode ser head de advmod, nummod, flat, conj e case."
msg_Prule19 = "ERRO "+parserDef[0]+"19: Todo token VERB dependente de xcomp nunca é head de uma relação de sujeito: nsubj, nsubj:outer e nsubj:pass."
msg_Prule20 = "ERRO "+parserDef[0]+"20: Nenhum token ADJ pode ser head de det."
msg_Prule21 = "ERRO "+parserDef[0]+"21: Todo token dependente de aux, aux:pass ou cop tem que ter ser AUX (o inverso não é verdadeiro)."
msg_Prule22 = "ERRO "+parserDef[0]+"22: Todo token VERB não pode ser head de case."
msg_Prule23 = "ERRO "+parserDef[0]+"23: Todo token head de obl só pode ser VERB, ADJ, ADV ou X. Exceção: também pode ser AUX se o verbo estiver elíptico (o token head de AUX não é VERB)."
msg_Prule24 = "ERRO "+parserDef[0]+"24: Todo token dependente de advmod é ADV, ADJ ou qualquer token que seja head de fixed."
msg_Prule25 = "ERRO "+parserDef[0]+"25: Todo token dependente de nummod é NUM (o inverso não é verdadeiro)."
msg_Prule26 = "ERRO "+parserDef[0]+"26: Todo token dependente de nmod é PROPN, NOUN, NUM, INTJ, SYM, X ou PRON (o inverso não é verdadeiro)."
msg_Prule27 = "ERRO "+parserDef[0]+"27: Todo token PUNCT é dependente de punct e vice-versa."
msg_Prule28 = "ERRO "+parserDef[0]+"28: Todo token ADP que não é head de fixed e cujo token head é um verbo no infinitivo (VerbForm=Inf) deve ser dependente de mark."
msg_Prule29 = "ERRO "+parserDef[0]+"29: Nenhum token PROPN ou NOUN pode ser dependente de appos de um token PROPN ou NOUN. Exceção: se o token head for separado por pontuação do token dependente."
msg_Prule30 = "ERRO "+parserDef[0]+"30: Nenhum token head de case pode ser dependente de obj."
msg_Prule31 = "ERRO "+parserDef[0]+"31: Nenhum token head de case pode ser dependente de iobj."
msg_Prule32 = "ERRO "+parserDef[0]+"32: Todos tokens 'muito', 'muitos', 'muita', 'muitas' que forem ADJ devem ser dependentes de amod. Exceção: caso seja dependente de xcomp ou head de cop."
msg_Prule33 = "ERRO "+parserDef[0]+"33: Todos tokens 'pouco', 'poucos', 'pouca', 'poucas' que forem ADJ devem ser dependentes de amod. Exceção: caso seja dependente de xcomp ou head de cop."
msg_Prule34 = "ERRO "+parserDef[0]+"34: Todos tokens 'onde', 'quando', 'como' que forem ADV, e não forem head de cop ou fixed, devem ser dependentes de advmod, fixed ou conj (se estiverem coordenadas com outro ADV)."
msg_Prule35 = "ERRO "+parserDef[0]+"35: Todo token dependente de expl só pode ser PRON."
msg_Prule36 = "ERRO "+parserDef[0]+"36: Nenhum token head de cop é VERB."
msg_Prule37 = "ERRO "+parserDef[0]+"37: Não deve haver Deprel projetivas (cruzamento de arcos) para nenhum token."
msg_Prule38 = "ERRO "+parserDef[0]+"38: Uma sentença só pode ter um token root e ele deve ser bem formado (head 0, Deprel 'root')"
msg_Prule39 = "ERRO "+parserDef[0]+"39: Nenhum token é head de mais de um nsubj."
msg_Prule40 = "ERRO "+parserDef[0]+"40: Nenhum token é head de mais de um nsubj:pass."
msg_Prule41 = "ERRO "+parserDef[0]+"41: Nenhum token é head de mais de um nsubj:outer."
msg_Prule42 = "ERRO "+parserDef[0]+"42: Nenhum token é head de mais de um csubj."
msg_Prule43 = "ERRO "+parserDef[0]+"43: Nenhum token é head de mais de um obj."
msg_Prule44 = "ERRO "+parserDef[0]+"44: Nenhum token é head de mais de um xcomp."
msg_Prule45 = "ERRO "+parserDef[0]+"45: Nenhum token é head de mais de um ccomp."
msg_Prule46 = "ERRO "+parserDef[0]+"46: Nenhum token é head de mais de um case."
msg_Prule47 = "ERRO "+parserDef[0]+"47: Todo token dependente de appos tem seu head à esquerda."
msg_Prule48 = "ERRO "+parserDef[0]+"48: Todo token dependente de mark tem seu head à direita."
msg_Prule49 = "ERRO "+parserDef[0]+"49: Todo token dependente de case tem seu head à direita."
msg_Prule50 = "ERRO "+parserDef[0]+"50: Todo token dependente de fixed tem seu head à esquerda."
msg_Prule51 = "ERRO "+parserDef[0]+"51: Todo token dependente de flat:name tem seu head à esquerda."
msg_Prule52 = "ERRO "+parserDef[0]+"52: Nenhum token pode ser simultaneamente head de nsubj e head de nsubj:pass, nsubj e csubj ou nsubj:pass e csubj."
msg_Prule53 = "ERRO "+parserDef[0]+"53: Todo token dependente de flat:foreign tem seu head à esquerda."
msg_Prule54 = "ERRO "+parserDef[0]+"54: Todo token SCONJ só pode ser dependente de mark, fixed, conj ou discourse. Exceção: se for a palavra 'quanto' pode ser dependente de advcl."
msg_Prule55 = "ERRO "+parserDef[0]+"55: Todo token head de nsubj:pass deve ter feature Voice=Pass. Exceção: se o verbo for head de expl:pass."
msg_Prule56 = "ERRO "+parserDef[0]+"56: Todo token head de obl:agent deve ter feature Voice=Pass."
msg_Prule57 = "ERRO "+parserDef[0]+"57: Todo token head de aux:pass deve ter feature Voice=Pass."
msg_Prule58 = "ERRO "+parserDef[0]+"58: Todo token head e dependente de flat:foreign deve ser X."
msg_Prule59 = "ERRO "+parserDef[0]+"59: Todo token head e dependente de flat:name deve ser PROPN ou X."
msg_Prule60 = "ERRO "+parserDef[0]+"60: Todo token head e dependente de flat deve ser NUM."
msg_Prule61 = "ERRO "+parserDef[0]+"61: Todo token head de aux ou aux:pass, que não for simultaneamente head de cop, deve ser VERB."
#########################
####   AVISOS
#########################
msg_Prule62 = "AVISO "+parserDef[0]+"62: Normalmente, dois ou mais tokens dependentes de cop não podem apontar para um mesmo token head, exceto se o head for head de um nsubj:outer."
msg_Prule63 = "AVISO "+parserDef[0]+"63: Normalmente, dois ou mais tokens dependentes de mark não podem apontar para um mesmo token head, exceto se o head for head de um nsubj:outer."
msg_Prule64 = "AVISO "+parserDef[0]+"64: Normalmente, todo token dependente de flat:name só pode ser head de cc, case, det, punct, expl, nmod (se o dependente for um número cardinal - NUM NumType=Card) ou amod (se o dependente for um número ordinal - ADJ NumType=Ord)."
msg_Prule65 = "AVISO "+parserDef[0]+"65: Normalmente, um token dependente de nmod só pode ter como head tokens PROPN, NOUN, NUM, SYM, X e PRON."
msg_Prule66 = "AVISO "+parserDef[0]+"66: Normalmente, todo token PUNCT final tem como head o token root."
msg_Prule67 = "AVISO "+parserDef[0]+"67: Normalmente, pontuações pareadas (aspas, parênteses, colchetes, chaves) tem o mesmo head."
msg_Prule68 = "AVISO "+parserDef[0]+"68: Normalmente, nenhum token pode ser simultaneamente head de obj e head de ccomp."
msg_Prule69 = "AVISO "+parserDef[0]+"69: Normalmente, nenhum token ADJ pode ser head ou dependente de appos."

#########################
####   REGRAS
#########################
def check01(b,dump):
    '''Todo dependente de det é DET (o inverso não é verdadeiro)'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "det") and (b[4][i][3] != "DET"):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule01), sep="\t", file=dump)
    return acc

def check02(b,dump):
    '''Todo dependente de amod é ADJ (o inverso não é verdadeiro)'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "amod") and (b[4][i][3] != "ADJ"):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule02), sep="\t", file=dump)
    return acc

def check03(b,dump):
    '''Todo dependente de iobj é PRON, Case=Dat e "me", "te", "se", "lhe", "nos", "vos", "lhes" (o inverso não é verdadeiro)'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "iobj") and \
                ((b[4][i][3] != "PRON") or ("Case=Dat" not in b[4][i][5]) or (b[4][i][2] not in ["me", "te", "se", "lhe", "nos", "vos", "lhes"])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule03), sep="\t", file=dump)
    return acc

def check04(b,dump):
    '''Todo dependente de obj que é PRON, Case=Acc e "me", "te", "se", "o", "a", "nos", "vos", "os", "as", "lo", "la", "los", "las", "no", "na", "nos", "nas" '''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if ((b[4][i][7] == "obj") and (b[4][i][3] == "PRON") and ("Case=Acc" in b[4][i][5])) and \
                (b[4][i][2] not in ["me", "te", "se", "o", "a", "nos", "vos", "os", "as", "lo", "la", "los", "las", "no", "na", "nos", "nas"]):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0],msg_Prule04 ), sep="\t", file=dump)
    return acc

def check05(b,dump):
    '''Nenhum ADP é head de relação - Exceções: pode ser head da relação fixed (e se for de fixed, pode ser de punct, cc e conj também), pode ser head de conj se o dependente for ADP, pode ser head de cc se o token ADP for dependente de conj.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "ADP"):
                target = b[4][i][0]
                wronghead, puncthead, fixedhead = False, False, False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] not in ["fixed", "punct", "conj", "cc"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "fixed"):
                        fixedhead = True
                    elif (tk[6] == target) and (tk[7] == "punct"):
                        puncthead = True
                    elif (tk[6] == target) and (tk[7] == "conj") and (tk[3] not in ["ADP"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "cc") and (b[4][i][7] != "conj"):
                        wronghead = True
                        break
                if (wronghead or (puncthead and not fixedhead)):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule05), sep="\t", file=dump)
    return acc

def check06(b,dump):
    '''Nenhum CCONJ é head de relação - Exceção: pode ser head da relação fixed (e se for de fixed, pode ser de punct também), pode ser head de conj dependente de CCONJ.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "CCONJ"):
                target = b[4][i][0]
                wronghead, puncthead, fixedhead = False, False, False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] not in ["fixed", "punct", "conj"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "fixed"):
                        fixedhead = True
                    elif (tk[6] == target) and (tk[7] == "punct"):
                        puncthead = True
                    elif (tk[6] == target) and (tk[7] in ["conj"]) and (tk[3] not in ["CCONJ"]):
                        wronghead = True
                        break
                if (wronghead and (not puncthead or not fixedhead)):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule06), sep="\t", file=dump)
    return acc

def check07(b,dump):
    '''Nenhum SCONJ é head de relação - Exceções: pode ser head da relação fixed (e se for de fixed, pode ser de punct, cc e conj também), pode ser head de conj se o dependente for SCONJ, pode ser head de cc se o token SCONJ for dependente de conj.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "SCONJ"):
                target = b[4][i][0]
                wronghead, puncthead, fixedhead = False, False, False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] not in ["fixed", "punct", "conj", "cc"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "fixed"):
                        fixedhead = True
                    elif (tk[6] == target) and (tk[7] == "punct"):
                        puncthead = True
                    elif (tk[6] == target) and (tk[7] in ["conj"]) and (tk[3] not in ["SCONJ"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "cc") and (b[4][i][7] != "conj"):
                        wronghead = True
                        break
                if (wronghead or (puncthead and not fixedhead)):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule07), sep="\t", file=dump)
    return acc

def check08(b,dump):
    '''Nenhum DET é head de relação - Exceções: pode ser head da relação fixed (e se for de fixed, pode ser de punct, cc e conj também), pode ser head de conj se o dependente for DET, pode ser head de cc se o token DET for dependente de conj.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "DET"):
                target = b[4][i][0]
                wronghead, puncthead, fixedhead = False, False, False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] not in ["fixed", "punct", "conj", "cc"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "fixed"):
                        fixedhead = True
                    elif (tk[6] == target) and (tk[7] == "punct"):
                        puncthead = True
                    elif (tk[6] == target) and (tk[7] in ["conj"]) and (tk[3] not in ["DET"]):
                        wronghead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "cc") and (b[4][i][7] != "conj"):
                        wronghead = True
                        break
                if (wronghead or (puncthead and not fixedhead)):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule08), sep="\t", file=dump)
    return acc

def check09(b,dump):
    '''Um token AUX não pode ser head de relação (exceto punct) se for dependente de aux, aux:pass ou cop.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "AUX") and (b[4][i][7] in ["aux", "aux:pass", "cop"]):
                target = b[4][i][0]
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] != "punct"):
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule09), sep="\t", file=dump)
                        break
    return acc

def check10(b,dump):
    '''Nenhum token dependente de fixed é head de relação.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "fixed"):
                target = b[4][i][0]
                head = False
                for tk in b[4]:
                    if (tk[6] == target):
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule10), sep="\t", file=dump)
                        break
    return acc

def check11(b,dump):
    '''O head de case só pode ser "PROPN", "NOUN", "PRON", "ADJ", "NUM", "X", "INTJ", "SYM", "ADV" '''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "case"):
                target = b[4][i][6]
                wrongHead = False
                for tk in b[4]:
                    if (tk[0] == target) and (tk[3] not in ["PROPN", "NOUN", "PRON", "ADJ", "NUM", "X", "INTJ", "SYM", "ADV"]):
                        wrongHead = True
                        break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule11), sep="\t", file=dump)
    return acc

def check12(b,dump):
    '''Regra 12  : Nenhum token SCONJ pode ser dependente de nsubj, nsubj:pass, nsubj:outer, csubj, csubj:pass, csubj:outer e obj.''' 
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "SCONJ"):
                if (b[4][i][7] in  ["nsubj", "nsubj:pass", "nsubj:outer", "csubj", "csubj:pass", "csubj:outer", "obj"]):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule12), sep="\t", file=dump)
    return acc

def check13(b,dump):
    '''O dependente de cop só pode ter lema = estar ou ser'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "cop") and (b[4][i][2] not in ["ser", "estar"]):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule13), sep="\t", file=dump)
    return acc

def check14(b,dump):
    '''Dois ou mais tokens dependentes de case não podem apontar para um mesmo token head.'''
    acc = 0
    heads = []
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "case"):
                if (b[4][i][6] in heads):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule14), sep="\t", file=dump)
                else:
                    heads.append(b[4][i][6])
    return acc

def check15(b,dump):
    '''Nenhum token PRON pode ser dependente de mark, exceto se for head de fixed.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "PRON"):
                if (b[4][i][7] in ["mark"]):
                    headfixed = False
                    for tk in b[4]:
                        if (tk[6] == b[4][i][0]) and (tk[7] == "fixed"):
                            headfixed = True
                            break
                    if (not headfixed):
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule15), sep="\t", file=dump)
    return acc

def check16(b,dump):
    '''Todo token dependente de aux só pode ter lema = 'ser', 'estar', 'ter', 'haver', 'ir' e 'vir' caso seja vir+Ger ou vir+'a'+Inf.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "aux") and (b[4][i][2] not in ["ser", "estar", "ter", "haver", "ir", "vir"]):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule16), sep="\t", file=dump)
            elif ((b[4][i][7] == "aux") and (b[4][i][2] == "vir")) and \
                 not ((b[4][i+1][3] in ["VERB", "AUX"]) and ("VerbForm=Ger" in b[4][i+1][5])) and \
                 not ((b[4][i+1][2] == "a") or (b[4][i+2][3] in ["VERB", "AUX"]) and ("VerbForm=Ger" in b[4][i+2][5])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule16), sep="\t", file=dump)
    return acc

def check17(b,dump):
    '''O ponto final não pode ter como head um token que não é head de outras relações" '''
    acc = 0
    headTimes = 0
    for i in range(len(b[4])):
        if (b[4][i][6] == b[4][-1][6]):
            headTimes += 1 
    if (headTimes < 2):
        acc += 1
        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule17), sep="\t", file=dump)
    return acc

def check18(b,dump):
    '''Todo token dependente de nummod só pode ser head de advmod, nummod, flat, conj e case.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nummod"):
                target = b[4][i][0]
                wrongHead = False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] not in ["advmod", "nummod", "flat", "conj", "case"]):
                        wrongHead = True
                        break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule18), sep="\t", file=dump)
    return acc

def check19(b,dump):
    '''Todo token VERB dependente de xcomp nunca é head de uma relação de sujeito: nsubj, nsubj:outer e nsubj:pass.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "xcomp"):
                target = b[4][i][0]
                wrongHead = False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] in ["nsubj", "nsubj:outer", "nsubj:pass"]):
                        wrongHead = True
                        break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule19), sep="\t", file=dump)
    return acc

def check20(b,dump):
    '''Nenhum token ADJ pode ser head de det.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "det"):
                target = b[4][i][6]
                wrongHead = False
                for tk in b[4]:
                    if (tk[0] == target) and (tk[3] == "ADJ"):
                        wrongHead = True
                        break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule20), sep="\t", file=dump)
    return acc

def check21(b,dump):
    '''Todo dependente da deprel aux, aux:pass ou cop tem que ter POS = AUX (o inverso não é verdadeiro) '''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] in ["aux", "aux:pass" "cop"]) and (b[4][i][3] != "AUX"):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule21), sep="\t", file=dump)
    return acc

def check22(b,dump):
    '''Todo token VERB não pode ser head de case.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "case"):
                target = b[4][i][6]
                wrongHead = False
                for tk in b[4]:
                    if (tk[0] == target) and (tk[3] in ["VERB", "AUX"]):
                        wrongHead = True
                        break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule22), sep="\t", file=dump)
    return acc

def check23(b,dump):
    '''Todo token head de obl só pode ser VERB, ADJ, ADV ou X. Exceção: também pode ser AUX se o verbo estiver elíptico (o token head de AUX não é VERB).'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "obl"):
                target = b[4][i][6]
                wrongHead = False
                for tk in b[4]:
                    if (tk[0] == target) and (tk[3] not in ["VERB", "ADJ", "ADV", "AUX", "X"]):
                        wrongHead = True
                        break
                    elif (tk[0] == target) and (tk[3] == "AUX"):
                        for ttk in b[4]:
                            if (ttk[0] == tk[6]):
                                if (ttk[3] == "VERB"):
                                    wrongHead = True
                                break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule23), sep="\t", file=dump)
    return acc

def check24(b,dump):
    '''Todo token dependente de advmod é ADV, ADJ ou qualquer token que seja head de fixed.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "advmod") and (b[4][i][3] not in ["ADV", "ADJ"]):
                target = b[4][i][0]
                headFixed = False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] == "fixed"):
                        headFixed = True
                        break
                if not headFixed:
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule24), sep="\t", file=dump)
    return acc

def check25(b,dump):
    '''Todo token dependente de nummod é NUM (o inverso não é verdadeiro).'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nummod") and (b[4][i][3] != "NUM"):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule25), sep="\t", file=dump)
    return acc

def check26(b,dump):
    '''Todo token dependente de nmod é PROPN, NOUN, NUM, SYM, INTJ, X ou PRON (o inverso não é verdadeiro).'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nmod") and (b[4][i][3] not in ["PROPN", "NOUN", "NUM", "SYM", "INTJ", "X", "PRON"]):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule26), sep="\t", file=dump)
    return acc

def check27(b,dump):
    '''Todo token PUNCT é dependente de punct e vice-versa.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if ((b[4][i][3] == "PUNCT") and (b[4][i][7] != "punct")) or \
               ((b[4][i][3] != "PUNCT") and (b[4][i][7] == "punct")):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule27), sep="\t", file=dump)
    return acc

def check28(b,dump):
    '''Todo token ADP que não é head de fixed e cujo token head é um verbo no infinitivo (VerbForm=Inf) deve ser dependente de mark.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "ADP"):
                for tk in b[4]:
                    wrong = False
                    if (tk[6] == b[4][i][0]) and (tk[7] == "fixed"):
                        wrong = False
                        break
                    if (tk[0] == b[4][i][6]) and ("VerbForm=Inf" in tk[5]) and (b[4][i][7] != "mark"):
                        wrong = True
                if (wrong):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule28), sep="\t", file=dump)
    return acc

def check29(b,dump):
    '''Nenhum token PROPN ou NOUN pode ser dependente de appos de um token PROPN ou NOUN. Exceção: se o token head for separado por token PUNCT do token dependente.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] in ["NOUN", "PROPN"]) and (b[4][i][7] == "appos"):
                for j in range(len(b[4])):
                    if (b[4][j][0] == b[4][i][6]) and (b[4][j][3] in ["NOUN", "PROPN"]):
                        wrong = True
                        if (i < j):
                            for k in range(i+1,j):
                                if (b[4][k][3] == "PUNCT"):
                                    wrong = False
                                    break
                        else:
                            for k in range(j+1,i):
                                if (b[4][k][3] == "PUNCT"):
                                    wrong = False
                                    break
                        if (wrong):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule29), sep="\t", file=dump)
                        break
    return acc

def check30(b,dump):
    '''Nenhum token head de case pode ser dependente de obj.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "case"):
                for tk in b[4]:
                    if (tk[0] == b[4][i][6]):
                        if (tk[7] == "obj"):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], tk[0], msg_Prule30), sep="\t", file=dump)
                        break
    return acc

def check31(b,dump):
    '''Nenhum token head de case pode ser dependente de iobj.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "case"):
                for tk in b[4]:
                    if (tk[0] == b[4][i][6]):
                        if (tk[7] == "iobj"):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], tk[0], msg_Prule31), sep="\t", file=dump)
                        break
    return acc

def check32(b,dump):
    '''Todos tokens 'muito', 'muitos', 'muita', 'muitas' que forem ADJ devem ser dependentes de amod. Exceção: caso seja dependente de xcomp ou head de cop.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "ADJ") and (b[4][i][2] == "muito"):
                if (b[4][i][7] not in ["amod", "xcomp"]):
                    wrong = True
                    for tk in b[4]:
                        if (tk[6] == b[4][i][0]) and (tk[7] == "cop"):
                            wrong = False
                    if (wrong):
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule32), sep="\t", file=dump)
    return acc

def check33(b,dump):
    '''Todos tokens 'pouco', 'poucos', 'pouca', 'poucas' que forem ADJ devem ser dependentes de amod. Exceção: caso seja dependente de xcomp ou head de cop.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "ADJ") and (b[4][i][2] == "pouco"):
                if (b[4][i][7] not in ["amod", "xcomp"]):
                    wrong = True
                    for tk in b[4]:
                        if (tk[6] == b[4][i][0]) and (tk[7] == "cop"):
                            wrong = False
                    if (wrong):
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule33), sep="\t", file=dump)
    return acc

def check34(b,dump):
    '''Todos tokens 'onde', 'quando', 'como' que forem ADV, e não forem head de cop ou fixed, devem ser dependentes de advmod, fixed ou conj (se estiverem coordenadas com outro ADV).'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "ADV") and (b[4][i][2] in ["onde", "quando", "como"]):
                headcopfix, conjADV = False, False
                for tk in b[4]:
                    if (tk[6] == b[4][i][0]) and (tk[7] in ["cop", "fixed"]):
                        headcopfix = True
                    if (tk[0] == b[4][i][6]) and (tk[3] == "ADV"):
                        conjADV = True
                if (b[4][i][7] != "advmod") and (b[4][i][7] != "fixed") and (not headcopfix) and (not conjADV):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule34), sep="\t", file=dump)
    return acc

def check35(b,dump):
    '''Todo token dependente de expl só pode ser PRON.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][7] == "expl") and (b[4][i][3] != "PRON"):
            acc += 1
            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule35), sep="\t", file=dump)
    return acc

def check36(b,dump):
    '''Nenhum token head de cop é VERB.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][7] == "cop") and (b[4][i][3] == "VERB"):
            acc += 1
            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule36), sep="\t", file=dump)
    return acc

def check37(b,dump):
    '''Não deve haver Deprel projetivas (cruzamento de arcos) para nenhum token '''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]) and (b[4][i][7] != "root") and (b[4][i][6] != "0"):
            if (b[4][i][0].isdigit()):
                tkID = eval(b[4][i][0])
            else:
                tkID = 0
            if (b[4][i][6].isdigit()):
                tkHead  = eval(b[4][i][6])
            else:
                tkhead = 0
            if (tkID < tkHead):
                for j in range(i+1,len(b[4])):
                    if (b[4][j][0] == b[4][i][6]):
                        break
                    elif ("-" not in b[4][j][0]):
                        if (b[4][j][6].isdigit()):
                            middle = eval(b[4][j][6])
                        else:
                            middle = 0
                        if (middle < tkID) or (middle > tkHead):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule37), sep="\t", file=dump)
                            break
            elif (tkID > tkHead):
                for j in range(i-1,0,-1):
                    if (b[4][j][0] == b[4][i][6]):
                        break
                    elif ("-" not in b[4][j][0]):
                        if (b[4][j][6].isdigit()):
                            middle = eval(b[4][j][6])
                        else:
                            middle = 0
                        if (middle > tkID) or (middle < tkHead):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule37), sep="\t", file=dump)
                            break
    return acc

def check38(b,dump):
    '''Uma sentença só pode ter um root e ele deve ser bem formado (head 0, Deprel 'root') '''
    acc = 0
    count, x = 0, 0
    for i in range(len(b[4])):
        if (b[4][i][7] == "root") and (b[4][i][6] == "0"):
            count += 1
            if (count > 1):
                x = i
        elif ((b[4][i][7] == "root") and (b[4][i][6] != "0")) or \
             ((b[4][i][7] != "root") and (b[4][i][6] == "0")):
            acc += 1
            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule38), sep="\t", file=dump)
    if (count != 1):
        acc += 1
        print("{}\t{}\t{}".format(b[0], b[4][x][0], msg_Prule38), sep="\t", file=dump)
    return acc

def check39(b,dump):
    '''Nenhum token é head de mais de um nsubj.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nsubj"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule39), sep="\t", file=dump)
    return acc

def check40(b,dump):
    '''Nenhum token é head de mais de um nsubj:pass.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nsubj:pass"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule40), sep="\t", file=dump)
    return acc

def check41(b,dump):
    '''Nenhum token é head de mais de um nsubj:outer.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nsubj:outer"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule41), sep="\t", file=dump)
    return acc

def check42(b,dump):
    '''Nenhum token é head de mais de um csubj.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "csubj"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule42), sep="\t", file=dump)
    return acc

def check43(b,dump):
    '''Nenhum token é head de mais de um obj.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "csubj"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule43), sep="\t", file=dump)
    return acc

def check44(b,dump):
    '''Nenhum token é head de mais de um xcomp.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "csubj"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule44), sep="\t", file=dump)
    return acc

def check45(b,dump):
    '''Nenhum token é head de mais de um ccomp.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "csubj"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule45), sep="\t", file=dump)
    return acc

def check46(b,dump):
    '''Nenhum token é head de mais de um case.'''
    acc = 0
    deps = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "case"):
                if (b[4][i][6].isdigit()):
                    deps[eval(b[4][i][6])-1] += 1
    for i in range(len(deps)):
        if (deps[i] > 1):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule46), sep="\t", file=dump)
    return acc

def check47(b,dump):
    '''Todo token dependente de appos tem seu head à esquerda.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][6].isdigit()) and (b[4][i][0].isdigit()):
            if (b[4][i][7] == "appos") and (eval(b[4][i][6]) > eval(b[4][i][0])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule47), sep="\t", file=dump)
    return acc

def check48(b,dump):
    '''Todo token dependente de mark tem seu head à direita.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][6].isdigit()) and (b[4][i][0].isdigit()):
            if (b[4][i][7] == "mark") and (eval(b[4][i][6]) < eval(b[4][i][0])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule48), sep="\t", file=dump)
    return acc

def check49(b,dump):
    '''Todo token dependente de case tem seu head à direita.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][6].isdigit()) and (b[4][i][0].isdigit()):
            if (b[4][i][7] == "case") and (eval(b[4][i][6]) < eval(b[4][i][0])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule49), sep="\t", file=dump)
    return acc

def check50(b,dump):
    '''Todo token dependente de fixed tem seu head à esquerda.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][6].isdigit()) and (b[4][i][0].isdigit()):
            if (b[4][i][7] == "fixed") and (eval(b[4][i][6]) > eval(b[4][i][0])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule50), sep="\t", file=dump)
    return acc

def check51(b,dump):
    '''Todo token dependente de flat:name tem seu head à esquerda.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][6].isdigit()) and (b[4][i][0].isdigit()):
            if (b[4][i][7] == "flat:name") and (eval(b[4][i][6]) > eval(b[4][i][0])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule51), sep="\t", file=dump)
    return acc

def check52(b,dump):
    '''Nenhum token pode ser simultaneamente head de nsubj e head de nsubj:pass, nsubj e csubj ou nsubj:pass e csubj.'''
    acc = 0
    nsubj = [0]*b[2]
    npass = [0]*b[2]
    csubj = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]) and (b[4][i][6].isdigit()):
            if (b[4][i][7] == "nsubj"):
                nsubj[eval(b[4][i][6])-1] += 1
            elif (b[4][i][7] == "nsubj:pass"):
                npass[eval(b[4][i][6])-1] += 1
            elif (b[4][i][7] == "csubj"):
                csubj[eval(b[4][i][6])-1] += 1
    for i in range(b[2]):
        if ((nsubj[i] > 0) and (npass[i] > 0)) or ((nsubj[i] > 0) and (csubj[i] > 0)) or ((npass[i] > 0) and (csubj[i] > 0)):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule52), sep="\t", file=dump)
    return acc

def check53(b,dump):
    '''Todo token dependente de flat:foreign tem seu head à esquerda.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][6].isdigit()) and (b[4][i][0].isdigit()):
            if (b[4][i][7] == "flat:foreign") and (eval(b[4][i][6]) > eval(b[4][i][0])):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule53), sep="\t", file=dump)
    return acc

def check54(b,dump):
    '''Todo token SCONJ só pode ser dependente de mark, fixed, conj ou discourse. Exceção: se for a palavra 'quanto' pode ser dependente de advcl.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][3] == "SCONJ") and (b[4][i][7] not in ["mark", "fixed", "conj", "discourse"]):
            if (b[4][i][2] != "quanto") or (b[4][i][7] != "advcl"):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule54), sep="\t", file=dump)
    return acc

def check55(b,dump):
    '''Todo token head de nsubj:pass deve ter feature Voice=Pass. Exceção: se o verbo for head de expl:pass.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][7] == "nsubj:pass"):
            missingpass, explpass = False, False
            for tk in b[4]:
                if (tk[0] == b[4][i][6]) and ("Voice=Pass" not in tk[5]):
                    missingpass = True
                if (tk[6] == b[4][i][6]) and (tk[7] == "expl:pass"):
                    explpass = True
            if (missingpass) and (not explpass):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule55), sep="\t", file=dump)
    return acc

def check56(b,dump):
    '''Todo token head de obl:agent deve ter feature Voice=Pass.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][7] == "obl:agent"):
            for tk in b[4]:
                if (tk[0] == b[4][i][6]) and ("Voice=Pass" not in tk[5]):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule56), sep="\t", file=dump)
    return acc

def check57(b,dump):
    '''Todo token head de aux:pass deve ter feature Voice=Pass.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][7] == "aux:pass"):
            for tk in b[4]:
                if (tk[0] == b[4][i][6]) and ("Voice=Pass" not in tk[5]):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule57), sep="\t", file=dump)
    return acc

def check58(b,dump):
    '''Todo token head ou dependente de flat:foreign deve ser X.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "flat:foreign"):
                if (b[4][i][3] != "X"):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule58), sep="\t", file=dump)
            else:
                for tk in b[4]:
                    if (tk[6] == b[4][i][0]) and (tk[7] == "flat:foreign"):
                        if (b[4][i][3] != "X"):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule58), sep="\t", file=dump)
                        break
    return acc

def check59(b,dump):
    '''Todo token head ou dependente de flat:name deve ser PROPN ou X.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "flat:name"):
                if (b[4][i][3] != "PROPN") and (b[4][i][3] != "X"):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule59), sep="\t", file=dump)
            else:
                for tk in b[4]:
                    if (tk[6] == b[4][i][0]) and (tk[7] == "flat:name"):
                        if (b[4][i][3] != "PROPN") and (b[4][i][3] != "X"):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule59), sep="\t", file=dump)
                        break
    return acc

def check60(b,dump):
    '''Todo token head ou dependente de flat deve ser NUM.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "flat"):
                if (b[4][i][3] != "NUM"):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule60), sep="\t", file=dump)
            else:
                for tk in b[4]:
                    if (tk[6] == b[4][i][0]) and (tk[7] == "flat"):
                        if (b[4][i][3] != "NUM"):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule60), sep="\t", file=dump)
                        break
    return acc

def check61(b,dump):
    '''Todo token head de aux ou aux:pass, que não for simultaneamente head de cop, deve ser VERB.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] in ["aux", "aux:pass"]):
                for tk in b[4]:
                    if (tk[0] == b[4][i][6]):
                        if (tk[3] != "VERB"):
                            wrong = True
                            for tkk in b[4]:
                                if (tkk[6] == tk[0]) and (tkk[7] == "cop"):
                                    wrong = False
                                    break
                            if (wrong):
                                acc += 1
                                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule61), sep="\t", file=dump)
                        break
    return acc

#########################
####   AVISOS
#########################
def check62(b,dump):
    '''Normalmente, dois ou mais tokens dependentes de cop não podem apontar para um mesmo token head, exceto se o head for head de um nsubj:outer.'''
    acc = 0
    heads = []
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "cop"):
                if (b[4][i][6] in heads):
                    headNSUBJouter = False
                    for j in range(len(b[4])):
                        if (b[4][j][7] == "nsubj:outer") and (b[4][j][6] == b[4][i][6]):
                            headNSUBJouter = True
                            break
                    if not headNSUBJouter:
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule62), sep="\t", file=dump)
                else:
                    heads.append(b[4][i][6])
    return acc

def check63(b,dump):
    '''Normalmente, dois ou mais tokens dependentes de mark não podem apontar para um mesmo token head, exceto se o head for head de um nsubj:outer.'''
    acc = 0
    heads = []
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "mark"):
                if (b[4][i][6] in heads):
                    headNSUBJouter = False
                    for j in range(len(b[4])):
                        if (b[4][j][7] == "nsubj:outer") and (b[4][j][6] == b[4][i][6]):
                            headNSUBJouter = True
                            break
                    if not headNSUBJouter:
                        acc += 1
                        print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule63), sep="\t", file=dump)
                else:
                    heads.append(b[4][i][6])
    return acc

def check64(b,dump):
    '''Normalmente, todo token dependente de flat:name só pode ser head de cc, case, det, punct, expl, nmod (se o dependente for um número cardinal - NUM NumType=Card) ou amod (se o dependente for um número ordinal - ADJ NumType=Ord).'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "flat:name"):
                target = b[4][i][0]
                wrongHead = False
                for tk in b[4]:
                    if (tk[6] == target) and (tk[7] not in ["cc", "case", "det", "punct", "expl", "nmod", "amod", "advcl"]):
                        wrongHead = True
                        break
                    elif (tk[6] == target) and (tk[7] == "nmod"):
                        if (tk[3] != "NUM") or ("NumType=Card" not in tk[5]):
                            wrongHead = True
                            break
                    elif (tk[6] == target) and (tk[7] == "amod"):
                        if (tk[3] != "ADJ") or ("NumType=Ord" not in tk[5]):
                            wrongHead = True
                            break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule64), sep="\t", file=dump)
    return acc

def check65(b,dump):
    '''Normalmente, um nmod só pode ter como head "PROPN", "NOUN", "NUM", "SYM", "X", "PRON" '''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "nmod"):
                target = b[4][i][6]
                wrongHead = False
                for tk in b[4]:
                    if (tk[0] == target) and (tk[3] not in ["PROPN", "NOUN", "NUM", "SYM", "X", "PRON"]):
                        wrongHead = True
                        break
                if (wrongHead):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule65), sep="\t", file=dump)
    return acc

def check66(b,dump):
    '''Normalmente, todo token PUNCT final tem como head o token root.'''
    acc = 0
    for i in range(len(b[4])):
        if (b[4][i][0] == b[4][-1][6]):
            if (b[4][i][7] != "root"):
                acc += 1
                print("{}\t{}\t{}".format(b[0], b[4][-1][0], msg_Prule66), sep="\t", file=dump)
            break
    return acc

def check67(b,dump):
    '''Normalmente, pontuações pareadas (aspas, parênteses, colchetes, chaves) tem o mesmo head.'''
    acc = 0
    pairedA = ['"', "'", "(", "[", "{"]
    pairedB = ['"', "'", ")", "]", "}"]
    visited = []
    idxA, idxB, currentA, currentB = -1, -1, -1, -1
    for i in range(len(b[4])):
        if (b[4][i][0] not in visited) and (b[4][i][1] in pairedA):
            A = b[4][i][1]
            idxA = i
            if (b[4][i][0].isdigit()):
                currentA = eval(b[4][i][0])
            else:
                currentA = 0
            B = pairedB[pairedA.index(A)]
            for j in range(i+1,len(b[4])):
                if (b[4][j][1] == B):
                    idxB = j
                    if (b[4][j][0].isdigit()):
                        currentB = eval(b[4][j][0])
                    else:
                        currentB = 0
                    break
            if (currentA != -1) and (currentB != -1):
                for k in range(idxA+1,idxB):
                    if ("-" not in b[4][k][0]) and (b[4][k][6].isdigit()):
                        if (eval(b[4][k][6]) < currentA) or (eval(b[4][k][6]) > currentB):
                            if (b[4][idxA][6] != b[4][k][0]) or (b[4][idxB][6] != b[4][k][0]):
                                acc += 1
                                print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule67), sep="\t", file=dump)
                            visited.append(b[4][idxA][0])
                            visited.append(b[4][idxB][0])
                            idxA, idxB, currentA, currentB = -1, -1, -1, -1
                            break
    return acc

def check68(b,dump):
    '''Normalmente, nenhum token pode ser simultaneamente head de obj e head de ccomp.'''
    acc = 0
    obj = [0]*b[2]
    ccomp = [0]*b[2]
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][7] == "obj"):
                if (b[4][i][6].isdigit()):
                    obj[eval(b[4][i][6])-1] += 1
            elif (b[4][i][7] == "ccomp"):
                if (b[4][i][6].isdigit()):
                    ccomp[eval(b[4][i][6])-1] += 1
    for i in range(b[2]):
        if (obj[i] > 0) and (ccomp[i] > 0):
            acc += 1
            print("{}\t{}\t{}".format(b[0], i+1, msg_Prule68), sep="\t", file=dump)
    return acc

def check69(b,dump):
    '''Normalmente, nenhum token ADJ pode ser head ou dependente de appos.'''
    acc = 0
    for i in range(len(b[4])):
        if ("-" not in b[4][i][0]):
            if (b[4][i][3] == "ADJ"):
                if (b[4][i][7] == "appos"):
                    acc += 1
                    print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule69), sep="\t", file=dump)
                else:
                    for tk in b[4]:
                        if (tk[6] == b[4][i][0]) and (tk[7] == "appos"):
                            acc += 1
                            print("{}\t{}\t{}".format(b[0], b[4][i][0], msg_Prule69), sep="\t", file=dump)
                            break
    return acc



def check(i,b,dump):
    if (i==0):
        return check01(b,dump)
    elif (i==1):
        return check02(b,dump)
    elif (i==2):
        return check03(b,dump)
    elif (i==3):
        return check04(b,dump)
    elif (i==4):
        return check05(b,dump)
    elif (i==5):
        return check06(b,dump)
    elif (i==6):
        return check07(b,dump)
    elif (i==7):
        return check08(b,dump)
    elif (i==8):
        return check09(b,dump)
    elif (i==9):
        return check10(b,dump)
    elif (i==10):
        return check11(b,dump)
    elif (i==11):
        return check12(b,dump)
    elif (i==12):
        return check13(b,dump)
    elif (i==13):
        return check14(b,dump)
    elif (i==14):
        return check15(b,dump)
    elif (i==15):
        return check16(b,dump)
    elif (i==16):
        return check17(b,dump)
    elif (i==17):
        return check18(b,dump)
    elif (i==18):
        return check19(b,dump)
    elif (i==19):
        return check20(b,dump)
    elif (i==20):
        return check21(b,dump)
    elif (i==21):
        return check22(b,dump)
    elif (i==22):
        return check23(b,dump)
    elif (i==23):
        return check24(b,dump)
    elif (i==24):
        return check25(b,dump)
    elif (i==25):
        return check26(b,dump)
    elif (i==26):
        return check27(b,dump)
    elif (i==27):
        return check28(b,dump)
    elif (i==28):
        return check29(b,dump)
    elif (i==29):
        return check30(b,dump)
    elif (i==30):
        return check31(b,dump)
    elif (i==31):
        return check32(b,dump)
    elif (i==32):
        return check33(b,dump)
    elif (i==33):
        return check34(b,dump)
    elif (i==34):
        return check35(b,dump)
    elif (i==35):
        return check36(b,dump)
    elif (i==36):
        return check37(b,dump)
    elif (i==37):
        return check38(b,dump)
    elif (i==38):
        return check39(b,dump)
    elif (i==39):
        return check40(b,dump)
    elif (i==40):
        return check41(b,dump)
    elif (i==41):
        return check42(b,dump)
    elif (i==42):
        return check43(b,dump)
    elif (i==43):
        return check44(b,dump)
    elif (i==44):
        return check45(b,dump)
    elif (i==45):
        return check46(b,dump)
    elif (i==46):
        return check47(b,dump)
    elif (i==47):
        return check48(b,dump)
    elif (i==48):
        return check49(b,dump)
    elif (i==49):
        return check50(b,dump)
    elif (i==50):
        return check51(b,dump)
    elif (i==51):
        return check52(b,dump)
    elif (i==52):
        return check53(b,dump)
    elif (i==53):
        return check54(b,dump)
    elif (i==54):
        return check55(b,dump)
    elif (i==55):
        return check56(b,dump)
    elif (i==56):
        return check57(b,dump)
    elif (i==57):
        return check58(b,dump)
    elif (i==58):
        return check59(b,dump)
    elif (i==59):
        return check60(b,dump)
    elif (i==60):
        return check61(b,dump)
    elif (i==61):
        return check62(b,dump)
    elif (i==62):
        return check63(b,dump)
    elif (i==63):
        return check64(b,dump)
    elif (i==64):
        return check65(b,dump)
    elif (i==65):
        return check66(b,dump)
    elif (i==66):
        return check67(b,dump)
    elif (i==67):
        return check68(b,dump)
    elif (i==68):
        return check69(b,dump)



def checkSent(b, dump, rep):
    total, warn = 0, 0
    acc = []
    for i in range(parserDef[1]):
        acc.append(check(i,b,dump))
        if (acc[i] > 0):
            rep.writeSent(parserDef[0], i+1, b)
        if (i < parserDef[2]):
            total += acc[i]
        else:
            warn += acc[i]
    return acc, total, warn
