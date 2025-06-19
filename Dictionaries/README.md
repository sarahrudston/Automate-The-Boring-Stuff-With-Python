<h2>Practice Questions</h2>

1. What does the code for an empty dictionary look like?<br>
*{} represents an empty dictionary.*

2. What does a dictionary value with a key `foo` and a value `42` look like?<br>
*{'foo': 42} represents a dictionary with a key of 'foo' and a value of 42.*

3. What is the main difference between a dictionary and a list?<br>
*In lists, items are ordered and can be referred to by their placement value eg spam[1]. Dictionaries are unordered - it doesn't matter what order the key-value pairs are typed.*

4. What happens if you try to access `spam['foo']` if `spam` is `{'bar': 100}`?<br>
*If you try to access `spam['foo']` and the `spam` dictionary doesn't contain a key called 'foo', a KeyError will be thrown.*

5. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.keys()`?<br>
*There is no substantive difference - you can use `'cat' in spam` as a shorter version of `'cat' in spam.keys()`.*

6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.values()'`?<br>
*`'cat' in spam` is checking whether there is a key in `spam` called 'cat'. `'cat' in spam.values()` is checking whether there is a value in `spam` called 'cat'.*

7. What is the shortcut for the following code?<br>
`if 'color not in spam:`<br>
    `spam['color'] = 'black'`<br>
*The shortcut for the above code is `spam.setdefault('color', 'black')`*

8. What module and function can be used to "pretty print" dictionary values?<br>
*The `pprint` module and function can be used to print dictionary values in a more readable way.*