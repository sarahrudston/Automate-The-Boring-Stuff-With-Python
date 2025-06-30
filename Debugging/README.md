<h2>Practice Questions</h2>

1. Write an `assert` statement that triggers an `AssertionError` if the variable `spam` is an integer less than `10`.<br>
*assert spam >= 10, 'The spam variable is less than 10.'*

2. Write an `assert` statement that triggers an `AssertionError` if the variables `eggs` and `bacon` contain strings that are the same as each other, even if their cases are different. (That is, `'hello'` and `'hello'` are considered the same, as are `'goodbye'` and `'GOODbye'`.)<br>
*assert eggs.lower() != bacon.lower() 'The eggs and bacon variables are the same!'*

3. Write an `assert` statement that *always* triggers an `AssertionError`.<br>
*assert 1 >= 2, 'Oh no!'*