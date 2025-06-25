<h2>Practice Questions</h2>

1. Which of the following are operators, and which are values?

* *Operator*
'hello' *Value*
-88.8 *Value*
- *Operator*
/ *Operator*
+ *Operator*
5 *Value*

2. Which of the following is a variable, and which is a string?

spam
'spam'

*spam with no quote marks is a variable and 'spam' with quote marks is a string.*

3. Name three data types.
*String, integer and boolean.*

4. What is an expression made up of? What do all expressions do?
*An expression evaluates values down to a single value using an operator. For example, 2 + 2 is an expression which evaluates to 4.*

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
*An assignment statement is used to store a value in a variable. This means it can be used in an expression later on.*

6. What does the variable `bacon` contain after the following code runs?

bacon = 20
bacon + 1

*The variable `bacon` will contain 20 after the code runs. `bacon` + 1 only runs an expression based on what's in the assignment statement. It doesn't change the assignment statement.*

7. What should the following two expressions evaluate to?

'spam' + 'spamspam' *'spamspamspam'*
'spam' * 3 *'spamspamspam'*

8. Why is `eggs` a valid variable name while 100 is invalid?
*Variable names cannot begin with integers.*

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
*The str(), int() and float() functions can be used to get the string, integer and floating-point numbers of a value. For example, str(29) will return '29' which is a string.*

10. Why does this expression cause an error? How can you fix it?

'I eat ' + 99 + ' burritos.'

*It's not possible to concatenate string values with integers. First, we should use the str() function to return the integer 99 as a string, like this: 'I eat ' + str(99) + ' burritos.'