# VerificaUD
 This repository has verificaUD.py program, a verifier for corpora in Portuguese encoded using CoNLL-U files (`.conllu`), the Universal Dependencies (UD) usual format.

 This program has also an online version with HTML interface available at: http://verificaud.icmc.usp.br

 Further information about this program can be obtained at: https://sol.sbc.org.br/index.php/stil/article/view/25485

 ## Reference
 To reference this program please refer to this publication:
 - LOPES, L.; DURAN, M. S.; PARDO, T. A. S. Verifica UD - A verifier for Universal Dependencies annotation in Portuguese. In: Proc. of the UDFest-BR 2023, 2023. DOI: https://doi.org/10.5753/stil.2023.25485

 ## Bibtex:
 @inproceedings{Lopes2023VerificaUD,
   author = 'LOPES, L. and DURAN, M. S. and PARDO, T. A. S.', 
   title = 'Verifica UD - A verifier for Universal Dependencies annotation in Portuguese',
   booktitle = 'Proc. of the UDFest-BR 2023',
   series = 'UDFest-BR',
   year = 2023,
   pages = '1-8',
   doi = 'https://doi.org/10.5753/stil.2023.25485',
   url = 'https://sol.sbc.org.br/index.php/stil/article/view/25485',
}

 # Contents
 The main files in this repository are:
- `README.md` - this read explanatory file;
- `verificaUD.py` - the Python 3 program;
- `structure.py` - the package with rules at the structural level;
- `tagger.py` - the package with rules at the tagger level;
- `parser.py` - the package with rules at the parser level;
- `reporter.py` - the package with a class to manage the errors and warning reports;
- `corpus.conllu` - the input file to be used as example.
- `report.txt` - the output file generated reading the example input file;

As this program uses a class to handle CoNLL-U files (`conlluFile`), the Python 3 file with this class (`conlluFile.py`) is included here.

# Acknowledgments
This work was carried out at the Center for Artificial Intelligence of the University of São Paulo (C4AI - [http://c4ai.inova.usp.br/](http://c4ai.inova.usp.br/)), with support by the São Paulo Research Foundation (FAPESP grant #2019/07665-4) and by the IBM Corporation. The project was also supported by the Ministry of Science, Technology and Innovation, with resources of Law N. 8.248, of October 23, 1991, within the scope of PPI-SOFTEX, coordinated by Softex and published as Residence in TIC 13, DOU 01245.010222/2022-44.

