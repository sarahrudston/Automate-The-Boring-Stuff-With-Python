<h2>Practice Questions</h2>

1. What is a relative path relative to?<br>
*A relative path is relative to the program's current working directory.*

2. What does an absolute path start with?<br>
*An absolute path always begins with the root folder which is C:\ on Windows and / on macOS and Linux.*

3. What does `Path('C:/Users') / 'Al'` evaluate to on Windows?<br>
*It will return `C:/Users/Al`*

4. What does `'C:/Users' / 'Al'` evaluate to on Windows?<br>
*An error will be thrown. To join paths, one of the first two values in the expression must be a `Path` object. The / operator can be used on two `Path` objects or on a `Path` object and a string, but not on two strings.*

5. What do the `os.getcwd()` and `os.chdir()` functions do?<br>
*`os.getcwd()` returns the current working directory as a string. The `os.chdir()` function changes the current working directory.*

6. What are the . and .. folders?<br>
*A single period for a folder name is shorthand for 'this folder'. Two periods means 'the parent folder'.*

7. In *C:\bacon\eggs\spam.txt*, which part is the directory name, and which part is the base name?<br>
*In C:\bacon\eggs\spam.txt, the directory is C:\bacon\eggs and spam.txt is the base name.*

8. What three "mode" arguments can you pass to the `open()` function for plaintext files?<br>
*You can pass `'r'` for the read argument, `'w'` for the write argument and `'a'` for the append argument.*

9. What happens if an existing file is opened in write mode?<br>
*The contents of the file will be overwritten.*

10. What is the difference between the `read()` and `readlines()` methods?<br>
*The `read()` method returns the string contained in the file while the `readlines()` returns a list of string values from the file, one for each line of text.*

11. What data structure does a shelf value resemble?<br>
*A shelf value resembles a binary file.*