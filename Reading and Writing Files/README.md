<h2>Practice Questions</h2>

1. What is a relative path relative to?
*A relative path is relative to the program's current working directory.*

2. What does an absolute path start with?
*An absolute path always begins with the root folder which is C:\ on Windows and / on macOS and Linux.*

3. What does `Path('C:/Users') / 'Al'` evaluate to on Windows?
*It will return `C:/Users/Al`*

4. What does `'C:/Users' / 'Al'` evaluate to on Windows?
*An error will be thrown. To join paths, one of the first two values in the expression must be a `Path` object. The / operator can be used on two `Path` objects or on a `Path` object and a string, but not on two strings.*

5. What do the `os.getcwd()` and `os.chdir()` functions do?
*`os.getcwd()` returns the current working directory as a string. The `os.chdir()` function changes the current working directory.*

6. What are the . and .. folders?
*A single period for a folder name is shorthand for 'this folder'. Two periods means 'the parent folder'.*

7. In *C:\bacon\eggs\spam.txt*, which part is the directory name, and which part is the base name?