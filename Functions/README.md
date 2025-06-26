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