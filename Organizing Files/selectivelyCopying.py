import os, shutil
from pathlib import Path

h = Path.home()

def selectiveCopy(inputFolder, ext, outputFolder):
    resultFolder = os.path.abspath(outputFolder)

    for folder_name, subfolders, filenames in os.walk(inputFolder):

        for filename in filenames:
            if filename.endswith(ext):
                print(f"Found {filename} with extension {ext}. Copying to {resultFolder}.")
                filepath = os.path.join(os.path.abspath(folder_name), filename)

                if not os.path.exists(resultFolder):
                    os.makedirs(resultFolder)
                    
                if os.path.dirname(filepath) != resultFolder:
                    shutil.copy(filepath, resultFolder)
                    print(f'Copied {filepath} to {resultFolder}')
        
selectiveCopy(h / 'spam', 'TXT', h / 'spam3')
        
    