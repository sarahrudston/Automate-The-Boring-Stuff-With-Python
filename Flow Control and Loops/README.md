<h2>Practice Questions for Flow Control</h2>

When I started working through this book, I was using the 2nd edition up to Chapter 6 and then I started working from the 3rd edition. In the 3rd edition, Flow Control and Loops are separate chapters. That's why there's two sections for practice questions here.

1. What are the two values of the Boolean data type? How do you write them?
*The Boolean data type has two values: `True` and `False`. You write them without quote marks and they always start with a capital letter.*

2. What are the three Boolean operators?
*The three Boolean operators are `and`, `or`, and `not`.*

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
| Expression | Evaluates to |
| ----------- | ------------ |
| True and True | True |
| True and False | False |
| False and True | False |
| False and False | False |

4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5) *False*
not (5 > 4) *False*
(5 > 4) or (3 == 5) *True*
not ((5 > 4) or (3 == 5)) *False*
(True and True) and (True == False) *False*
(not False) or (not True) *True*

5. What are the six comparison operators?
*The six comparison operators are `==` which means equal to, `!=` which means not equal to, `<` which means less than, `>` which means greater than, `<=` which means less than or equal to and `>=` which means greater than or equal to.*

6. What is the difference between the equal to operator and the assignment operator?
*The assignment operator is `=` and the equal to operator is `==`.*

7. Explain what a condition is and where you would use one.
*Conditions are the same thing as expressions except they always evaluate to `True` or `False`. You use them for flow control, which means 'if this condition is true, do this thing, or else do this other thing.'*

8. Identify the three blocks in this code:

`spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('Done')`

*You can tell when a block begins and ends from the indentation of the lines of code. Here, a new block begins at line three, the second at line 5 and the third at line 7.*

<h2>Practice Questions for Loops</h2>

1. What keys can you press if your Python program is stuck in an infinite loop?
*You can use CTRL-C to break an infinite loop.*

2. What is the difference between break and continue?
*A `break` statement will immediately exit the `while` loop. A `continue` statement will jump back to the top of the `while` loop and start again.*

3. What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a `for` loop?
*`range(10)` will run the `for` loop 5 times. `range(0, 10)` will run the `for` loop starting at 0 and going up to (but not including) 10. `range(0, 10, 1)` will run the `for` loop from 0 up to (but not including) 10 with an increment of 1.*

4. Write a short program that prints the numbers 1 to 10 using a `for` loop. Then, write an equivalent program that prints the numbers 1 to 10 using a `while` loop.
*See practice exercise files.*

5. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing `spam`?
*`spam.bacon()`*