# VerificaUD - Verificador de arquivos CoNLL-U para textos em Português
#
# Este programa recebe um arquivo CoNLL-U que contém um corpus
#   em Português e gera um relatório dos problemas encontrados de
#   acordo com regras de verificação definidas:
#         https://sol.sbc.org.br/index.php/stil/article/view/25485
#
# Opções:
#
# -h help
# 
# Exemplo de utilização:
#
# verificaUD -o report.txt corpus.conllu
#
# Lê o arquivo corpus.conllu e salva o resultado da verificação
#   no arquivo 'report.txt'
#
# last edit: 01/23/2024
# created by Lucelene Lopes - lucelene@gmail.com

import sys, os
sys.path.insert(0, 'packages')
from conlluFile import conlluFile
from tagger import checkTerm, taggerDef
from parser import checkSent, parserDef
from structure import goodNumbers, wellformedTree, structDef
from reporter import conlluReports

#################################################
### Captura de argumentos da linha de comando
#################################################
def parseOptions(arguments):
    # default options
    output_file, input_file = "report.conllu", ""
    i = 1
    while i < len(arguments):
        if (arguments[i][0] == "-"):
            # ajuda (help) - mostra ajuda, nada é executado
            if ((arguments[i][1] == "h") and (len(arguments[i])==2)) or \
               (arguments[i] == "-help"):
                print("Opções:\n-h ajuda",
                      "Exemplo de utilização:", \
                      "verificaUD -o report.conllu corpus.conllu", \
                      "Lê o arquivo corpus.conllu e salva o resultado da verificação", \
                      "no arquivo 'report.txt'", \
                      sep="\n")
                return None
            # opção de arquivo de saída (um nome de arquivo)
            elif ((arguments[i][1] == "o") and (len(arguments[i])==2)) or \
                 (arguments[i] == "-output"):
                output_file = arguments[i+1]
                i += 2
            # opções inválidas - nada é executado
            else:
                print("Opção {} inválida, demais opções ignoradas, por favor execute novamente".format(arguments[i]))
                return None
        # arquivo de entrada - só é incluído se existir
        else:
            if (os.path.isfile(arguments[i])):
                input_file = arguments[i]
                i += 1
            else:
                print("O arquivo {} não foi encontrado, por favor execute novamente".format(arguments[i]))
                return None
    return [output_file, input_file]

########################################
#  Nosso verificador STRUCT
#  input:
#     name     -  the name of the conllu file
#     report   -  the name of the textual output file
########################################
def struct(name, report, samples):
    dump = open(report, "w")
    base = conlluFile(name)
    s, t = base.getSandT()
    print("Base:", name, "- sentenças:", s, "- tokens:", t, "- STRUCT relat:", report)
    totalS, totalT = 0, 0
    for i in range(base.getS()):
        b = base.getSentByIndex(i)
        acc = goodNumbers(b, dump, samples)
        if (acc == 0):
            acc = wellformedTree(b, dump, samples)
        totalT += acc
        if (acc > 0):
            totalS += 1
    dump.close()
    print("Problemas da Estrutura de CoNLL-U (struct):", totalT)
    print("Sentenças sem problems {} ({:2.2f}%)".format(s-totalS, 100*(s-totalS)/s))
    print("Tokens sem problems {} ({:2.2f}%)".format(t-totalT, 100*(t-totalT)/t))
    return s, t, totalT, 0

########################################
#  Nosso verificador TAGGER
#  input:
#     name     -  the name of the conllu file
#     report   -  the name of the textual output file
########################################
def tagger(name, report, samples):
    dump = open(report, "w")
    base = conlluFile(name)
    s, t = base.getSandT()
    print("Base:", name, "- sentenças:", s, "- tokens:", t, "- TAGGER relat:", report)
    totalS, totalT = 0, 0
    for i in range(base.getS()):
        b = base.getSentByIndex(i)
        acc = 0
        for tk in b[4]:
            acc += checkTerm(tk, b[0], dump, samples)
        totalT += acc
        if (acc > 0):
            totalS += 1
    dump.close()
    print("Problemas de Formação Lexical (tagger):", totalT)
    print("Sentenças sem problems {} ({:2.2f}%)".format(s-totalS, 100*(s-totalS)/s))
    print("Tokens sem problems {} ({:2.2f}%)".format(t-totalT, 100*(t-totalT)/t))
    return s, t, totalT, 0

########################################
#  Nosso verificador PARSER
#  input:
#     name     -  the name of the conllu file
#     report   -  the name of the textual output file
########################################
def parser(name, report, samples):
    dump = open(report, "w")
    base = conlluFile(name)
    s, t = base.getSandT()
    print("Base:", name, "- sentenças:", s, "- tokens:", t, "- PARSER relat:", report)
    totalS, totalT, totalW = 0, 0, 0
    for i in range(base.getS()):
        b = base.getSentByIndex(i)
        rules, acc, warn = checkSent(b, dump, samples)
        totalT += acc
        totalW += warn
        if (acc+warn > 0):
            totalS += 1
            ####
            
    dump.close()
    print("Problemas de Dependência Relacional (parser):", totalT)
    print("Avisos de verificação de Dependência Relacional (parser):", totalW)
    print("Sentenças sem problems ou avisos {} ({:2.2f}%)".format(s-totalS, 100*(s-totalS)/s))
    print("Tokens sem problems {} ({:2.2f}%)".format(t-totalT, 100*(t-totalT)/t))
    print("Tokens sem problems ou avisos {} ({:2.2f}%)".format(t-(totalT+totalW), 100*(t-(totalT+totalW))/t))
    return s, t, totalT, totalW

########################################
#  mergeReport
########################################
def mergeReport(name, outfile, s, t, e_s, w_s, e_t, w_t, e_p, w_p):
    issues = []
    probS = []
    avisoS = []
    infile = open(name+"_struct.txt")
    for line in infile:
        issues.append(line[:-1])
        buf = line.split("\t")
        if (buf[0] not in probS):
            probS.append(buf[0])
    infile.close()
    infile = open(name+"_tagger.txt")
    for line in infile:
        issues.append(line[:-1])
        buf = line.split("\t")
        if (buf[0] not in probS):
            probS.append(buf[0])
    infile.close()
    infile = open(name+"_parser.txt")
    for line in infile:
        issues.append(line[:-1])
        if ("Normalmente" not in line):
            buf = line.split("\t")
            if (buf[0] not in probS):
                probS.append(buf[0])
        else:
            buf = line.split("\t")
            if (buf[0] not in avisoS):
                avisoS.append(buf[0])
    infile.close()
    issues.sort()
    print("Arquivo:", name[8:]+".conllu\n", file=outfile)
    print("sentencas:                   {:5>} (tokens: {})".format(s,t), file=outfile)
    print("sentencas sem erro:          {:5>}".format(s-len(probS)), file=outfile)
    print("sentencas sem erro ou aviso: {:5>}".format(s-len(probS)-len(avisoS)), file=outfile)
    print("erros estruturais: {:5>} - avisos: {:5>}".format(e_s, w_s), file=outfile)
    print("erros de tagger:   {:5>} - avisos: {:5>}".format(e_t, w_t), file=outfile)
    print("erros de parser:   {:5>} - avisos: {:5>}".format(e_p, w_p), file=outfile)
    
    print("\nErros e avisos encontrados:", file=outfile)
    for i in issues:
        buf = i.split("\t")
        print("{:15}\ttoken {:3}\t{}".format(buf[0], buf[1], buf[2]), file=outfile)

########################################
#  Do it all
########################################
def doIt(name, outfile):
    if (name[-7:] != ".conllu"):
        return "not a .conllu file"
    else:
        outputfile = name[:-7]
    samples = conlluReports("samples", [structDef,taggerDef,parserDef])
    print("Executando verificação estrutural...")
    s, t, e_s, w_s = struct(name, outputfile+"_struct.txt", samples)
    print("Executando verificação de tagger...")
    s, t, e_t, w_t = tagger(name, outputfile+"_tagger.txt", samples)
    print("Executando verificação de parser...")
    s, t, e_p, w_p = parser(name, outputfile+"_parser.txt", samples)
    samples.closeAll()
    mergeReport(outputfile, outfile, s, t, e_s, w_s, e_t, w_t, e_p, w_p)
    return e_s+e_t+e_p, w_s+w_t+w_p


########################################
#  Main function - verificaUD
########################################
def verificaUD():
    if (len(sys.argv) == 1):
        io_files = ["report.txt", "corpus.conllu"]
    else:
        io_files = parseOptions(sys.argv)
    if (io_files != None):
        print("Starting verification of", io_files[1])
        outfile = open(io_files[0], "w")
        e, w = doIt(io_files[1], outfile)
        outfile.close()
        print("Arquivo {} salvo com o relatório do arquivo {} contendo {} erros e {} avisos".format(io_files[0],io_files[1], e, w))
    else:
        print("Por favor, execute o programa novamente")

verificaUD()


