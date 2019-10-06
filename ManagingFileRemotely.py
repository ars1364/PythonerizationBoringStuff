import os, csv

outputFile = open('output.txt', 'w+')
finalFilesToRemove = []
with open('confFile.csv', 'r', newline='') as confFile:
    fileReader = csv.reader(confFile, delimiter='|')
    for row in fileReader:
        outputFile.write('\n' + 'fileReader.row0 = ' + row[0] + ' fileReader.row1 = ' + row[1])
        filePath = '\\\\{0}\\{1}\\'.format(row[0], row[1])
        outputFile.write('\n' + filePath)

        for r, d, f in os.walk(filePath):
            for file in f:
                outputFile.write('\n' + 'os.path= ' + os.path.join(r, file))
                fileSize = os.stat(os.path.join(r, file))
                outputFile.write('\n' + 'file size= ' + str(fileSize.st_size))
                if fileSize.st_size < 1024:
                    outputFile.write('\n' + 'os.path = ' + os.path.join(r, file))
                    finalFilesToRemove.append(os.path.join(r, file))
#
for f in finalFilesToRemove:
    os.remove(f)
    outputFile.write('\n' + 'finalFile {0} --> has been removed'.format(f))
outputFile.close()
