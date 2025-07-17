<h2>Practice Questions</h2>

1. What is the difference between `shutil.copy()` and `shutil.copytree()`?<br>
*`shutil.copy()` will copy a single file and `shutil.copytree()` will copy the folder at the path source, along with all of its files and subfolders, to the path destination.*

2. What function is used to rename files?<br>
*`shutil.move()` can both move and rename the file if the desination path is not an existing folder.*
 
3. What is the difference between the delete functions in the `send2trash` and `shutil` modules? <br>
*The `shutil.rmtree()` function irreversibly deletes files and folders. The `send2trash()` function is safer because it will send folders and files to the computer's trash or recycling bin instead of permanently deleting them.*

4. `ZipFile` objects have a `close()` method just like `File` objects' `close()` method. What `ZipFile` method is equivalent to `File` objects' `open()` method?<br>
*You can open a ZipFile object by using `zipfile.ZipFile()` and then passing either 'w' for write mode or 'a' for append mode.*