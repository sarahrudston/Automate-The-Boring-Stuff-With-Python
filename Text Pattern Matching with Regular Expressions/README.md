<h2>Practice Questions</h2>

1. What is the function that returns `Regex` objects?
*re.compile()*

2. Why are raw strings often used when creating `Regex` objects?
*We write regex strings as raw strings because they often have backslashes. If we didn't use raw strings, we'd have to escape the backslashes every time.*

3. What does the `search()` method return?
*It returns a `Match` object.*

4. How do you get the actual strings that match the pattern from a `Match` object?
*You return the actual strings by using the `group()` method.*

5. In the regex created from `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, what does group 0 cover? Group 1? Group 2?
*Group 0 returns the entire matched text. Group 1 is whatever is in the first set of parantheses. Group 2 is whatever is in the second set of parantheses.*

6. Parantheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parantheses and period characters?
*You can escape characters you want to match in the regex using a backslash. Then the escaped characters will be interpreted as part of the pattern you are matching.*

7. The `findall()` method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
*If there are no groups in the regular expression the method will return a list of strings. But if there are groups in the regular expression, the method will return a list of tuples.*

8. What does the | character signify in regular expression?
*The | character is an alternation operator. It's used when you want to match one of multiple expressions. `r'Cat|Dog'` will match either `'Cat'` or `'Dog'`.*

9. What two things does the ? character signify in regular expressions?
*The ? character either means that the preceding qualifier as optional (for example `r'42?'` means match 4 but optionally also 2) or it can mean a lazy match of the previous qualifier (for example `r'(Ha){3,5}?'` will match `'HaHaHa'` but not `'HaHaHaHaHa'`, because it's only optionally looking for up to 5 matches).*

10. What is the difference between the `+` and `*` characters in regular expressions?
*The `+` character means match one or more of the preceding qualifier. The qualifier must appear at least once. The `*` character means match zero or more. This means the preceding qualifier can occur any number of times in the text or it can be completely absent.*

11. What is the difference between `{3}` and `{3,5}` in regular expressions?
*`{3}` will match 3 instances of the preceding qualifier. `{3,5}` can match three, four or five instances of the preceding qualifier.*

12. What do the `\d`, `\w` and `\s` shorthand character classes signify in regular expressions?
*The \d, \w, and \s match a digit, word, or space character, respectively.*

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
*The \D, \W, and \S match anything except a digit, word, or space character, respectively.*

14. What is the difference between the `.*` and `.*?` regular expressions?
*`.*` stands in for anything following the preceding qualifier. `.*?` does something similar but it'll only match the shortest possible string. For example, if you were searching for text including an opening and closing angle bracket, the first will match everything regardless of how many closing angle brackets there are. The second will only match up to the first closing angle bracket.*

15. What is the character class syntax to match all numbers and lowercase letters?
*The character class syntax to match all lowercase letters and number is `[a-z0-9]`.*

16. How do you make a regular expression case-insensitive?
*To make a regular expression case-insensitve you can pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`.*

17. What does the . character normally match? What does it match if `re.DOTALL` is passed as the second argument to `re.compile()`?
*The . character normally matches everything except a newline. If you use `re.DOTALL` it will instead match all characters including the newline character.*

18. If `num_re = re.compile(r'\d+')`, what will `num_re.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` return?
*It will return `'X drummers, X pipers, five rings, X hens'`. The `r'\d+'` regex looks for any instance of a number that appears at least once. The `sub` method then replaces whatever the regex finds with X. Because 'five' isn't a number, it doesn't get replaced in the text.*

19. What does passing `re.VERBOSE` as the second argument to `re.compile()` allow you to do?
*It tells `re.combine()` to ignore whitespace and comments inside a regex string. This allows you to spread complex regular expressions over multiple lines and use comments to label the components. It makes the regex easier to read and understand.*


