import os, shutil, re, sys


def renameFiles(rootDir, ext):
    date_pattern = re.compile(r'''
                          (0[1-9]|1[0-2])- # matches 01-09 or 10-12 for month with a '-'
                          (0[1-9]|[12]\d|3[01])- # matches 01-31 for days
                          ((19|20)\d{2}) # matches the 19s and 20s for year
                          '''
                          + ext,  
                          re.VERBOSE
    )

    for filename in os.listdir(rootDir):
        match = date_pattern.search(filename)
        if match:
            month, day, year, _ = match.groups()
            newFilename = f'{filename[:match.start()]}{day}-{month}-{year}{filename[match.end():]}'
            print(newFilename)

            oldFilepath = os.path.join(rootDir, filename)
            newFilepath = os.path.join(rootDir, newFilename)

            shutil.move(oldFilepath, newFilepath)
            print(f'Renamed: {filename} -> {newFilename}')
            print()

renameFiles('.', '.txt')

