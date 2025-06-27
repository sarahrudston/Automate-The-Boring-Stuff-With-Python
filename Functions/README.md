<h2>Practice Questions for Functions</h2>

1. Why are functions advantageous to have in your programs?
*Functions group code that gets executed multiple times. Without using a function, you'd have to copy and paste the code each time you wanted to run it. It's better to avoid doing this because, if you ever want to update the code, you would need to remember to change it in every place you copied it.*

2. When does the code in a function execute: when the function is defined or when the function is called?
*When the function is called.*

3. What statement creates a function?
*A `def` statement creates a function.*

4. What is the difference between a function and a function call?
*The function is what's defined, using a `def` statement. The function call is the function's name followed by parantheses. There could also be arguments given in the parantheses. When the program executes and reaches the function call, it will jump to the first line in the function and execute the code.*

5. How many global scopes are there in a Python program? How many local scopes are there?
*There is only one global scope. A new local scope gets created whenever a program calls a function.*

6. What happens to variables in a local scope when the function call returns?
*They no longer exist in the program. When a function is called, the variables in it only exist during the function call.*

7. What is a return value? Can a return value be part of an expression?
*The return value is whatever the expression in the function evaluates to. You can use a function call in an expression because the call evaluates to the return value.*

8. If a function does not have a `return` statement, what is the return value of a call to that function?
*If there's no return value specified, the function will return `None`.*

9. How can you force a variable in a function to refer to the global variable?
*You can use the `global` statement within the function to force Python to refer to the global variable rather than creating a local variable. For example, `global eggs` within a function refers to the global variable of `eggs` not a local variable.*

10. What is the data type of `None`?
*The `None` value has the type of `NoneType`. It is the only value which has this type.*

11. What does the `import areallyourpetsnamederic` statement do?
*An `import` statement makes a module available for use in a Python script. So the above line of code would make the `areallyourpetsnamederic` module available within the script.*

12. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing `spam`?
*`spam.bacon()`*

13. How can you prevent a program from crashing when it gets an error?
14. What does in the `try` clause? What goes in the `except` clause?
*You can use a `try` clause to indicate which code could potentially have an error and then an `except` clause to hold the code which should run instead if an error happens.*

15. Write the following program in a file named *notrandomdice.py* and run it. Why does each function call return the same number?

import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

*Because the function doesn't define the `random_number` as a local variable, it instead refers to the global variable which is only called once in the code. That's why the same number is returned 4 times.*