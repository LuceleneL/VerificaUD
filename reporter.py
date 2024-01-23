import os

class conlluReports:
    '''A class to manage several output conllu files in a given path,
       with a one level folder structure.
       This is defined by a python list with pairs to each  folder:
         - <folder name> <number of folder in it>
       THe limitations that each folder can have only up to 99 files in it. '''
    def __init__(self, path, fileStruct):
        self.path = path
        self.folders, self.nrFiles, self.prevFiles = [], [], []
        acc = 0
        for folder in fileStruct:
            self.folders.append(folder[0])
            self.nrFiles.append(folder[1])
            self.prevFiles.append(acc)
            acc += folder[1]
        self.totalFiles = acc
        self.filenames, self.files, self.acc = [], [], []
        for f in self.folders:
            if not os.path.exists(path+"/"+f):
                os.makedirs(path+"/"+f)
            fnamemodel = path+"/"+f+"/"+f+"00.conllu"
            for i in range(1,fileStruct[self.folders.index(f)][1]+1):
                fname = fnamemodel[:-9] + str(i // 10) + str(i % 10) + fnamemodel[-7:]
                self.files.append(open(fname, "w"))
                self.filenames.append(fname)
                self.acc.append(0)
    def writeSent(self, folder, folderNr, b):
        fileAddr = self.prevFiles[self.folders.index(folder)]+folderNr-1
        # for line in b[3]:
        #     print(line, file=self.files[fileAddr])
        print("# sent_id = "+b[0], file=self.files[fileAddr])
        print("# text = "+b[1], file=self.files[fileAddr])
        for tk in b[4]:
            print(tk[0], tk[1], tk[2], tk[3], tk[4], tk[5], tk[6], tk[7], tk[8], tk[9], sep="\t", file=self.files[fileAddr])
        print(file=self.files[fileAddr])
        self.acc[fileAddr] += 1
    def writeHeader(self, folder, folderNr, name):
        fileAddr = self.prevFiles[self.folders.index(folder)]+folderNr-1
        print("# newdoc id = "+name+"\n# newpar", file=self.files[fileAddr])
    def closeAll(self):
        outfile = open(self.path+"/report.tsv", "w")
        for i in range(self.totalFiles):
            self.files[i].close()
            print(self.filenames[i], self.acc[i], sep="\t", file=outfile)
        outfile.close()

        



