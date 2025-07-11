<h2>Practice Questions</h2>

1. Write an `assert` statement that triggers an `AssertionError` if the variable `spam` is an integer less than `10`.<br>
*assert spam >= 10, 'The spam variable is less than 10.'*

2. Write an `assert` statement that triggers an `AssertionError` if the variables `eggs` and `bacon` contain strings that are the same as each other, even if their cases are different. (That is, `'hello'` and `'hello'` are considered the same, as are `'goodbye'` and `'GOODbye'`.)<br>
*assert eggs.lower() != bacon.lower() 'The eggs and bacon variables are the same!'*

3. Write an `assert` statement that *always* triggers an `AssertionError`.<br>
*assert 1 >= 2, 'Oh no!'*

4. What two lines must your program have to be able to call `logging.debug()`?<br>
*import logging*
*logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')*

5. What two lines must your program have to make `logging.debug()` send a logging message to a file named *programLog.txt*?<br>
*import logging*<br>
*logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')*

6. What are the five logging levels?<br>
*DEBUG, INFO, WARNING, ERROR and CRITICAL*

7. What line of code can you add to disable all logging messages in your program?<br>
*logging.basicConfig(level=logging.CRITICAL)*

8. Why is using logging messages better than using `print()` to display the same message?<br>
*If you use print calls too often in your code, you will need to remove all of them for each log message. It increases the risk of error because you might remove some print calls that you still need. Using `logging` is better because it's easy to disable all log messages with just one line of code.*

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?<br>
 *Step Over executes the next line of code, unless it's a function call. In that case, it'll process the function call quickly and then pause as soon as it returns. Step In will execute the next line of code and then pause again, including for function calls. Step Out executes the code at normal speed until it returns from the current function.*

 10. After you click Continue, when will the debugger stop?<br>
 *Continue will execute the program normally until it either terminates or reaches a breakpoint.*

 11. What is a breakpoint?<br>
 *A breakpoint forces the debugger to pause whenever the program execution reaches that line of code.*

 12. How do you set a breakpoint on a line of code in Mu?<br>
 *You can set a breakpoint in Mu by clicking the line number in the file editor.*
