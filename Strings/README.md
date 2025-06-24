<h2>Practice Questions</h2>

1. What are escape characters?
*An escape character is a character that lets you use characters which are otherwise impossible to put into a string (such as a single quote, which would normally tell Python that a string has ended). Escape characters start with a backslash and then the character you want to add to a string.*

2. What do the \n and \t escape characters represent?
*The \n escape character means new line. The \t escape character means tab.*

3. How can you put a \ backslash character in a string?
*You need to enter it twice, like this \\.*

4. The string value "Howl's Moving Castle" is a valid string. Why isn't it a problem that the single quote character in the word Howl's isn't escape?
*Using double quotes around a string lets Python know that the single quite is part of the string and not marking the end of a string.*

5. If you don't want to put \n in your string, how can you write a string with newlines in it?
*You can use a multiline string, beginning with three single quotes or three double quotes instead. Any quotes, tabs, or newlines in between the triple quotes are treated as part of the same string.*

6. What do the following expressions evaluate to?

- 'Hello, world!'[1] *e*
- 'Hello, world!'[0:5] *Hello*
- 'Hello, world!'[:5] *Hello*
- 'Hello, world!'[3:] *lo, world!*

7. What do the following expressions evaluate to?

- 'Hello'.upper() *HELLO*
- 'Hello'.upper().isupper() *True*
- 'Hello'.upper().islower() *False*

8. What do the following expressions evaluate to?

- 'Remember, remember, the fifth of November.'.split() *('Remember,', 'remember,', 'the', 'fifth', 'of', 'November')*
- '-'.join('There can only be one.'.split()) *'There-can-only-be-one.'*

9. What string methods can you use to right-justify, left-justify and centre a string?
*The rjust() and ljust() methods use spaces to justify text to the right or left. To centre a string, we can use the center() method.*

10. How can you trim whitespace characters from the beginning or end of a string?
*The rstrip() and lstrip() methods strip off the whitespaces from the right and left ends of a string. The strip() method will trim all whitespaces from both the beginning and end of a string.*