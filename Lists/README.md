<h2>Practice Questions</h2>

1. What is `[]`?
*[] represents an empty list.*

2. How would you assign the value 'hello' as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)
*You can assign the value 'hello' to the third value in this list using `spam[2] = 'hello'`. The second position in the list represents the third value.*

For the following three questions, let's say `spam` contains the list `['a', 'b', 'c', 'd']`.

3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?
*This method would evaluate to `'d'`, which is the value at position 3 in the list. To break this down, the `'3' * 2` calculation would return 33, as the `'3'` is a string. This is then cast as an integer and divided by 11, which returns 3. This is again cast to an integer and contained within the code which returns an index position in the list (`spam[3]`). `'d'` is at position 3 in the list.*

4. What does `spam[-1]` evaluate to?
*`spam[-1]` evaluates to `'d'`. You can use negative integers to return the list items. The integer value -1 refers to the last index in the list, which in this case is `'d'`.*

5. What does `spam[:2]` evaluate to?
*`spam[:2]` would evaluate to `['a', 'b']`. This is because we are slicing the list. If we leave out the first integer, it's the same as using 0 or the beginning of the list. The second integer, 2, shows the index where the slice ends. The slice goes up to, but doesn't include, the value at the second index.*

For the following three questions, let's say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`.

6. What does `bacon.index('cat')` evaluate to?
*`bacon.index('cat')` evaluates to 1. This is because, when we have multiple list items which are identical, the list index method will return the first index position of the requested item.*

7. What does `bacon.append(99)` make the list value in `bacon` look like?
*If we run `bacon.append(99)`, the new list will look like this: `[3.14, 'cat', 11, 'cat', True, 99]`.*

8. What does `bacon.remove('cat')` make the list value in `bacon` look like?
*If we run `bacon.remove('cat')`, the new list will look like this: `[3.14, 11, 'cat', True]`. This is because the `remove` method only removes the first instance of an item, even if there are multiple items in the list which are identical.*

9. What are the operators for list concatenation and list replication?
*`+` is the operator for list concatenation. For example, running `[1, 2, 3] + ['A', 'B', 'C']` will give us `[1, 2, 3, 'A', 'B', 'C']`. `*` is the operator for list replication. For example, running `['hello', 'hi', 'howdy'] * 3` gives us `['hello', 'hi', 'howdy', 'hello', 'hi', 'howdy', 'hello', 'hi', 'howdy']`.*

10. What is the difference between the `append()` and `insert()` list methods?
*The `append()` method will add an extra item to the end of a list. The `insert()` method allows you to enter a new list item at a particular index location (specifying first the location and then the value to insert). For example, if we have a list of `['cat', 'dog', 'frog']` in a variable called `pets` and we run `pets.append('cow')`, the list will look like this: `['cat', 'dog', 'frog', 'cow']`. But if we instead run `pets.insert(1, 'cow')`, then the list will look like this: `['cat', 'cow', 'dog', 'frog']`.*

11. What are two ways to remove values from a list?
*You can remove a value from a list using the `remove` method. So in the above example, if we run `pets.remove('dog')` on the original list, it will look like this: `['cat', 'frog']`. You can also use the `del` method to remove a list item at a particular index location. After running del, all the values in the list after the deleted value will be moved up one index. For example, if we run `del pets[1]` on the original list, it will look like this: ``['cat', 'frog']`.*

12. Name a few ways that list values are similar to string values.
*You can perform many of the same methods on lists as you can on strings. For example, indexing, slicing, using them with `for` loops, with `len()` and with the `in` and `not in` operators.*

13. What is the difference between lists and tuples?
*The major difference between lists and tuples is that tuples are immutable, meaning they can't be changed. You can't modify, append or remove a value in a tuple. Tuples are also typed with parantheses instead of square brackets which are used for lists.*

14. How do you type the tuple value that just has the integer 42 in it?
*If you want to type a tuple that just has the integer 42, you can type (42,). The trailing space is to show that this is a tuple value, not just an integer.*

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
*You can change a list to a tuple or a tuple to a list with the `list()` and `tuple()` functions. For example, `tuple(['cat', 'dog', 5])` will return a type of tuple, just as `list(('cat', 'dog', 5))` will return a type of list.*

16. Variables that "contain" list values don't actually contain lists directly. What do they contain instead?
*Variables that "contain" list values only contain the references to the lists themselves. Assigning a list to variable just creates the value in the computer's memory and stores a reference to it.*

17. What is the difference between `copy.copy()` and `copy.deepcopy()`?
*`copy.copy()` allows us to copy a list (for example, if we want to make changes to it without changing the original list). `copy.deepcopy()` allows us to copy a list that has other lists contained in it.*