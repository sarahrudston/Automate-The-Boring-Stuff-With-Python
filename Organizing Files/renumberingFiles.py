import os, shutil
from pathlib import Path
import re

def getFilesWithPrefix(folderPath, prefix):

    fileRegex = re.compile(prefix + '(\\d+)(.\\w+)')
    fileList = sorted( [file for file in os.listdir(folderPath) if fileRegex.match(file)])
    return fileList

def fillGaps(folderPath, prefix):
    fileList = getFilesWithPrefix(folderPath, prefix)
    fileRegex = re.compile(prefix + '(\\d+)(.\\w+)')

    start = int(fileRegex.search(fileList[0]).group(1)) # Files sorted in ascending order
    count = start
    maxLength = len(fileRegex.search(fileList[-1]).group(1))

    for file in fileList:
        mo = fileRegex.search(file)
        fileNum = int(mo.group(1))

        if fileNum != count:
            newFileName = prefix + '0' * (maxLength - len(str(count))) + str(count) + mo.group(2)
            oldPath = os.path.join(folderPath, file)
            newPath = os.path.join(folderPath, newFileName)
            shutil.move(oldPath, newPath)
    
        count += 1

fillGaps('.', 'spam')