import os, shutil
from pathlib import Path
import re

#TODO: Get all files with prefix

prefix = 'spam'
folderPath = '.' 

fileRegex = re.compile(prefix + '(\d+)(.\w+)')
fileList = sorted( [file for file in os.listdir(folderPath) if fileRegex.match(file)])

start = int(fileRegex.search(fileList[0]).group[1]) #