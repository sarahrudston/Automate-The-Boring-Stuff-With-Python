import os, shutil
from pathlib import Path

def printFileSize(inputFolder):
    for folderName, subFolders, fileNames in os.walk(inputFolder):
        for fileName in fileNames:
            byte_size = os.path.getsize(folderName + '/' + fileName)
            mb_size = byte_size / (1024 * 1024)
            print(folderName, fileName, mb_size)
        
printFileSize(Path.home() / 'spam')