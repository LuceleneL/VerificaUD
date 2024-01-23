from conlluFile import conlluFile

taggerDef = ["T", 37, 29]   # identifier of the tagger problems, total number of rules, number of strict rules (not warning)
#########################
####   REGRAS
#########################
msg_Trule01 = "ERRO "+taggerDef[0]+"01: Palavra concatenada não pode ter atributos para lema, PoS e features."
msg_Trule02 = "ERRO "+taggerDef[0]+"02: Nenhum token ADP não abreviado pode ter features."
msg_Trule03 = "ERRO "+taggerDef[0]+"03: Todo token ADP abreviado só pode ter feature 'Abbr=Yes'."
msg_Trule04 = "ERRO "+taggerDef[0]+"04: Nenhum token CCONJ não abreviado pode ter features."
msg_Trule05 = "ERRO "+taggerDef[0]+"05: Todo token CCONJ abreviado só pode ter feature 'Abbr=Yes'."
msg_Trule06 = "ERRO "+taggerDef[0]+"06: Nenhum token SCONJ não abreviado pode ter features."
msg_Trule07 = "ERRO "+taggerDef[0]+"07: Todo token SCONJ abreviado só pode ter feature 'Abbr=Yes'."
msg_Trule08 = "ERRO "+taggerDef[0]+"08: Nenhum token INTJ não abreviado pode ter features."
msg_Trule09 = "ERRO "+taggerDef[0]+"09: Todo token INTJ abreviado só pode ter feature 'Abbr=Yes."
msg_Trule10 = "ERRO "+taggerDef[0]+"10: Nenhum token X não abreviado pode ter features exceto 'Foreign=Yes'."
msg_Trule11 = "ERRO "+taggerDef[0]+"11: Todo token X abreviado só pode ter feature 'Abbr=Yes' ou 'Foreign=Yes'."
msg_Trule12 = "ERRO "+taggerDef[0]+"12: Nenhum token ADV não abreviado pode ter features."
msg_Trule13 = "ERRO "+taggerDef[0]+"13: Todo token ADV abreviado só pode ter feature 'Abbr=Yes."
msg_Trule14 = "ERRO "+taggerDef[0]+"14: Todo token NUM textual deve ter feature 'NumType=Card/Frac', e pode ter apenas 'Gender=Fem/Masc'."
msg_Trule15 = "ERRO "+taggerDef[0]+"15: Todo token NUM numérico deve ter lema igual ao termo."
msg_Trule16 = "ERRO "+taggerDef[0]+"16: Todo token NUM numérico deve ter features 'NumType=Card'."
msg_Trule17 = "ERRO "+taggerDef[0]+"17: Todo token NOUN pode ter apenas features 'Gender=Fem/Masc', 'Number=Sing/Plur' e 'Abbr=Yes'."
msg_Trule18 = "ERRO "+taggerDef[0]+"18: Todo token ADJ pode ter apenas features 'Gender=Fem/Masc', 'Number=Sing/Plur', 'Abbr=Yes', 'VerbForm=Part' e 'NumType=Ord'."
msg_Trule19 = "ERRO "+taggerDef[0]+"19: Todo token VERB ou AUX devem ter features 'VerbForm=Inf/Ger/Part/Fin' e de acordo com o tempo verbal podem ter apenas 'Mood= =Ind/Sub/Cnd/Imp', 'Tense=Pres/Past/Fut/Imp/Pqp', 'Gender=Fem/Masc', 'Number=Sing/Plur', 'Person=1/2/3', 'Voice=Pass' e 'Abbr=Yes'."
msg_Trule20 = "ERRO "+taggerDef[0]+"20: Todo token DET deve ter features 'PronType=Art/Dem/Ind/Rel/Int/Prs' e de acordo com o tipo pode ter apenas 'Definite=Def/Ind', 'Gender=Fem/Masc', 'Number=Sing/Plur', 'Person=1/2/3' e 'Poss=Yes'."
msg_Trule21 = "ERRO "+taggerDef[0]+"21: Todo token PRON deve ter features 'PronType=Dem/Ind/Rel/Int/Prs' e de acordo com o tipo pode ter apenas 'Case=Acc/Dat/Nom', 'Gender=Fem/Masc', 'Number=Sing/Plur', 'Person=1/2/3' e 'Poss=Yes'."
msg_Trule22 = "ERRO "+taggerDef[0]+"22: Todo token PROPN não deve ter features."
msg_Trule23 = "ERRO "+taggerDef[0]+"23: Todo token PROPN deve ter lema igual ao termo."
msg_Trule24 = "ERRO "+taggerDef[0]+"24: Todo token PUNCT não deve ter features."
msg_Trule25 = "ERRO "+taggerDef[0]+"25: Todo token PUNCT deve ter lema igual ao termo."
msg_Trule26 = "ERRO "+taggerDef[0]+"26: Todo token SYM não deve ter features."
msg_Trule27 = "ERRO "+taggerDef[0]+"27: Todo token SYM deve ter lema igual ao termo."
msg_Trule28 = "ERRO "+taggerDef[0]+"28: A PoS tag PART não deve ser utilizada para a anotação em Portugês."
msg_Trule29 = "ERRO "+taggerDef[0]+"29: A PoS tag {} não faz parte das etiquetas válida para UD."

msg_Trule30 = "AVISO "+taggerDef[0]+"30: Palavra desconhecida para a classe fechada ADP."
msg_Trule31 = "AVISO "+taggerDef[0]+"31: Palavra desconhecida para a classe fechada AUX."
msg_Trule32 = "AVISO "+taggerDef[0]+"32: Palavra desconhecida para a classe fechada ADV."
msg_Trule33 = "AVISO "+taggerDef[0]+"33: Palavra desconhecida para a classe fechada CCONJ."
msg_Trule34 = "AVISO "+taggerDef[0]+"34: Palavra desconhecida para a classe fechada DET."
msg_Trule35 = "AVISO "+taggerDef[0]+"35: Palavra desconhecida para a classe fechada PRON."
msg_Trule36 = "AVISO "+taggerDef[0]+"36: Palavra desconhecida para a classe fechada SCONJ."
msg_Trule37 = "AVISO "+taggerDef[0]+"37: Palavra desconhecida para a classe fechada NUM."

def checkTerm(tk, SID, dump, samples):
    acc = 0
    if ("-" in tk[0]):
        if (tk[2] != "_") or (tk[3] != "_") or (tk[5] != "_"):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule01), file=dump)
    elif (tk[3] == "ADP"):
        if (tk[1].lower() == tk[2]):
            if (tk[5] != "_"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule02), file=dump)
        else:
            if (tk[5] != "Abbr=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule03), file=dump)
    elif (tk[3] == "CCONJ"):
        if (tk[1].lower() == tk[2]):
            if (tk[5] != "_"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule04), file=dump)
        else:
            if (tk[5] != "Abbr=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule05), file=dump)
    elif (tk[3] == "SCONJ"):
        if (tk[1].lower() == tk[2]):
            if (tk[5] != "_"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule06), file=dump)
        else:
            if (tk[5] != "Abbr=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule07), file=dump)
    elif (tk[3] == "INTJ"):
        if (tk[1].lower() == tk[2]):
            if (tk[5] != "_"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule08), file=dump)
        else:
            if (tk[5] != "Abbr=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule09), file=dump)
    elif (tk[3] == "X"):
        if (tk[1] == tk[2]):
            if (tk[5] != "_") and (tk[5] != "Foreign=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule10), file=dump)
        else:
            if (tk[5] != "Abbr=Yes") and (tk[5] != "Abbr=Yes|Foreign=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule11), file=dump)
    elif (tk[3] == "ADV"):
        if (tk[1].lower() == tk[2]):
            if (tk[5] != "_"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule12), file=dump)
        else:
            if (tk[5] != "Abbr=Yes"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule13), file=dump)
    elif (tk[3] == "NUM"):
        if (tk[1].isalpha()):
            if (tk[5] not in ["NumType=Card",
                              "Gender=Fem|NumType=Card",
                              "Gender=Masc|NumType=Card",
                              "Gender=Fem|NumType=Frac",
                              "Gender=Masc|NumType=Frac"]):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule14), file=dump)
        else:
            if (tk[1] != tk[2]):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule15), file=dump)
            if (tk[5] != "NumType=Card"):
                acc += 1
                print("{}\t{}\t{}".format(SID, tk[0], msg_Trule16), file=dump)
    elif (tk[3] == "NOUN"):
        if (tk[5].replace("Abbr=Yes|", "").replace("Foreign=Yes|", "") not in ["Gender=Fem|Number=Sing",
                          "Gender=Fem|Number=Plur",
                          "Gender=Masc|Number=Sing",
                          "Gender=Masc|Number=Plur",
                          "Number=Sing",
                          "Number=Plur",
                          "Gender=Fem",
                          "Gender=Masc",
                          "_",
                          "Abbr=Yes",
                          "Foreign=Yes"]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule17), file=dump)
    elif (tk[3] == "ADJ"):
        if (tk[5].replace("Abbr=Yes|", "").replace("Foreign=Yes|", "") not in ["Gender=Fem|Number=Sing",
                          "Gender=Fem|Number=Plur",
                          "Gender=Masc|Number=Sing",
                          "Gender=Masc|Number=Plur",
                          "Number=Sing",
                          "Number=Plur",
                          "Gender=Fem",
                          "Gender=Masc",
                          "_",
                          "Abbr=Yes",
                          "Foreign=Yes",
                          "Gender=Fem|Number=Sing|NumType=Ord",
                          "Gender=Fem|Number=Plur|NumType=Ord",
                          "Gender=Masc|Number=Sing|NumType=Ord",
                          "Gender=Masc|Number=Plur|NumType=Ord",
                          "Number=Sing|NumType=Ord",
                          "Number=Plur|NumType=Ord",
                          "Gender=Fem|NumType=Ord",
                          "Gender=Masc|NumType=Ord",
                          "Gender=Fem|Number=Sing|VerbForm=Part",
                          "Gender=Fem|Number=Plur|VerbForm=Part",
                          "Gender=Masc|Number=Sing|VerbForm=Part",
                          "Gender=Masc|Number=Plur|VerbForm=Part",
                          "Number=Sing|VerbForm=Part",
                          "Number=Plur|VerbForm=Part",
                          "Gender=Fem|VerbForm=Part",
                          "Gender=Masc|VerbForm=Part",
                          "VerbForm=Part"]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule18), file=dump)
    elif (tk[3] in ["VERB", "AUX"]):
        if (tk[5].replace("Abbr=Yes|", "") not in ["VerbForm=Inf",
                          "Number=Sing|Person=1|VerbForm=Inf",
                          "Number=Sing|Person=2|VerbForm=Inf",
                          "Number=Sing|Person=3|VerbForm=Inf",
                          "Number=Plur|Person=1|VerbForm=Inf",
                          "Number=Plur|Person=2|VerbForm=Inf",
                          "Number=Plur|Person=3|VerbForm=Inf",
                          "VerbForm=Ger",
                          "Gender=Fem|Number=Sing|VerbForm=Part",
                          "Gender=Fem|Number=Plur|VerbForm=Part",
                          "Gender=Masc|Number=Sing|VerbForm=Part",
                          "Gender=Masc|Number=Plur|VerbForm=Part",
                          "Gender=Fem|Number=Sing|VerbForm=Part|Voice=Pass",
                          "Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass",
                          "Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass",
                          "Gender=Masc|Number=Plur|VerbForm=Part|Voice=Pass",
                          "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=2|Tense=Past|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=1|Tense=Past|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=2|Tense=Past|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=2|Tense=Imp|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=1|Tense=Pqp|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=2|Tense=Pqp|VerbForm=Fin",
                          "Mood=Ind|Number=Sing|Person=3|Tense=Pqp|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=1|Tense=Pqp|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=2|Tense=Pqp|VerbForm=Fin",
                          "Mood=Ind|Number=Plur|Person=3|Tense=Pqp|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=1|Tense=Past|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=2|Tense=Past|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=3|Tense=Past|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=1|Tense=Past|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=2|Tense=Past|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=3|Tense=Past|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin",
                          "Mood=Sub|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=2|Tense=Fut|VerbForm=Fin",
                          "Mood=Sub|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin",
                          "Mood=Cnd|Number=Sing|Person=1|VerbForm=Fin",
                          "Mood=Cnd|Number=Sing|Person=2|VerbForm=Fin",
                          "Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin",
                          "Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin",
                          "Mood=Cnd|Number=Plur|Person=2|VerbForm=Fin",
                          "Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin",
                          "Mood=Imp|Number=Sing|Person=1|VerbForm=Fin",
                          "Mood=Imp|Number=Sing|Person=2|VerbForm=Fin",
                          "Mood=Imp|Number=Sing|Person=3|VerbForm=Fin",
                          "Mood=Imp|Number=Plur|Person=1|VerbForm=Fin",
                          "Mood=Imp|Number=Plur|Person=2|VerbForm=Fin",
                          "Mood=Imp|Number=Plur|Person=3|VerbForm=Fin"]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule19), file=dump)
    elif (tk[3] == "DET"):
        if (tk[5] not in ["Definite=Def|Gender=Fem|Number=Sing|PronType=Art",
                          "Definite=Def|Gender=Fem|Number=Plur|PronType=Art",
                          "Definite=Def|Gender=Masc|Number=Sing|PronType=Art",
                          "Definite=Def|Gender=Masc|Number=Plur|PronType=Art",
                          "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art",
                          "Definite=Ind|Gender=Fem|Number=Plur|PronType=Art",
                          "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art",
                          "Definite=Ind|Gender=Masc|Number=Plur|PronType=Art",
                          "Gender=Fem|Number=Sing|PronType=Dem",
                          "Gender=Fem|Number=Plur|PronType=Dem",
                          "Gender=Masc|Number=Sing|PronType=Dem",
                          "Gender=Masc|Number=Plur|PronType=Dem",
                          "Number=Sing|PronType=Dem",
                          "Number=Plur|PronType=Dem",
                          "Gender=Fem|Number=Sing|PronType=Ind",
                          "Gender=Fem|Number=Plur|PronType=Ind",
                          "Gender=Masc|Number=Sing|PronType=Ind",
                          "Gender=Masc|Number=Plur|PronType=Ind",
                          "Number=Sing|PronType=Ind",
                          "Number=Plur|PronType=Ind",
                          "PronType=Ind",
                          "Gender=Fem|Number=Sing|PronType=Rel",
                          "Gender=Fem|Number=Plur|PronType=Rel",
                          "Gender=Masc|Number=Sing|PronType=Rel",
                          "Gender=Masc|Number=Plur|PronType=Rel",
                          "Gender=Fem|Number=Sing|PronType=Int",
                          "Gender=Fem|Number=Plur|PronType=Int",
                          "Gender=Masc|Number=Sing|PronType=Int",
                          "Gender=Masc|Number=Plur|PronType=Int",
                          "Number=Sing|PronType=Int",
                          "Number=Plur|PronType=Int",
                          "Gender=Fem|Number=Sing|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Sing|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Plur|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Plur|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Sing|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Sing|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Plur|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Plur|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Plur|Person=3|Poss=Yes|PronType=Prs"]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule20), file=dump)
    elif (tk[3] == "PRON"):
        if (tk[5] not in ["Gender=Fem|Number=Sing|PronType=Dem",
                          "Gender=Fem|Number=Plur|PronType=Dem",
                          "Gender=Masc|Number=Sing|PronType=Dem",
                          "Gender=Masc|Number=Plur|PronType=Dem",
                          "Number=Sing|PronType=Dem",
                          "Number=Plur|PronType=Dem",
                          "Gender=Fem|Number=Sing|Person=3|PronType=Dem",
                          "Gender=Fem|Number=Plur|Person=3|PronType=Dem",
                          "Gender=Masc|Number=Sing|Person=3|PronType=Dem",
                          "Gender=Masc|Number=Plur|Person=3|PronType=Dem",
                          "Gender=Fem|Number=Sing|PronType=Ind",
                          "Gender=Fem|Number=Plur|PronType=Ind",
                          "Gender=Masc|Number=Sing|PronType=Ind",
                          "Gender=Masc|Number=Plur|PronType=Ind",
                          "Number=Sing|PronType=Ind",
                          "Number=Plur|PronType=Ind",
                          "PronType=Ind",
                          "Gender=Fem|Number=Plur|PronType=Rel",
                          "Gender=Masc|Number=Plur|PronType=Rel",
                          "Number=Sing|PronType=Rel",
                          "Number=Plur|PronType=Rel",
                          "PronType=Rel",
                          "Gender=Fem|Number=Sing|PronType=Int",
                          "Gender=Fem|Number=Plur|PronType=Int",
                          "Gender=Masc|Number=Sing|PronType=Int",
                          "Gender=Masc|Number=Plur|PronType=Int",
                          "Number=Sing|PronType=Int",
                          "Number=Plur|PronType=Int",
                          "PronType=Int",
                          "Gender=Fem|Number=Sing|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Sing|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Plur|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Plur|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Sing|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Sing|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Plur|Person=1|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Plur|Person=2|Poss=Yes|PronType=Prs",
                          "Gender=Masc|Number=Plur|Person=3|Poss=Yes|PronType=Prs",
                          "Number=Sing|Person=2|PronType=Prs",
                          "Number=Plur|Person=2|PronType=Prs",
                          "Case=Acc|Gender=Fem|Number=Plur|Person=3|PronType=Prs",
                          "Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
                          "Case=Acc|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
                          "Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
                          "Case=Acc|Number=Plur|Person=1|PronType=Prs",
                          "Case=Acc|Number=Plur|Person=2|PronType=Prs",
                          "Case=Acc|Number=Sing|Person=1|PronType=Prs",
                          "Case=Acc|Number=Sing|Person=2|PronType=Prs",
                          "Case=Acc|Person=3|PronType=Prs",
                          "Case=Dat|Number=Plur|Person=1|PronType=Prs",
                          "Case=Dat|Number=Plur|Person=2|PronType=Prs",
                          "Case=Dat|Number=Plur|Person=3|PronType=Prs",
                          "Case=Dat|Number=Sing|Person=1|PronType=Prs",
                          "Case=Dat|Number=Sing|Person=2|PronType=Prs",
                          "Case=Dat|Number=Sing|Person=3|PronType=Prs",
                          "Case=Dat|Person=3|PronType=Prs",
                          "Case=Nom|Gender=Fem|Number=Plur|Person=2|PronType=Prs",
                          "Case=Nom|Gender=Fem|Number=Plur|Person=3|PronType=Prs",
                          "Case=Nom|Gender=Fem|Number=Sing|Person=2|PronType=Prs",
                          "Case=Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs",
                          "Case=Nom|Gender=Masc|Number=Plur|Person=2|PronType=Prs",
                          "Case=Nom|Gender=Masc|Number=Plur|Person=3|PronType=Prs",
                          "Case=Nom|Gender=Masc|Number=Sing|Person=2|PronType=Prs",
                          "Case=Nom|Gender=Masc|Number=Sing|Person=3|PronType=Prs",
                          "Case=Nom|Number=Plur|Person=1|PronType=Prs",
                          "Case=Nom|Number=Plur|Person=2|PronType=Prs",
                          "Case=Nom|Number=Sing|Person=1|PronType=Prs",
                          "Case=Nom|Number=Sing|Person=2|PronType=Prs",
                          "Case=Nom|Person=3|PronType=Prs"]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule21), file=dump)
    elif (tk[3] == "PROPN"):
        if (tk[5] != "_"):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule22), file=dump)
        if (tk[1] != tk[2]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule23), file=dump)
    elif (tk[3] == "PUNCT"):
        if (tk[5] != "_"):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule24), file=dump)
        if (tk[1] != tk[2]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule25), file=dump)
    elif (tk[3] == "SYM"):
        if (tk[5] != "_"):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule26), file=dump)
        if (tk[1] != tk[2]):
            acc += 1
            print("{}\t{}\t{}".format(SID, tk[0], msg_Trule27), file=dump)
    elif (tk[3] == "PART"):
        acc += 1
        print("{}\t{}\t{}".format(SID, tk[0], msg_Trule28), file=dump)
    else:
        print("{}\t{}\t{}".format(SID, tk[0], msg_Trule29.format(tk[3])), file=dump)
    return acc


