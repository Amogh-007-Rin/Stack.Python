# Quiz: Mutability vs Immutability

1. Which of the following is immutable?
   - a) `list`
   - b) `dict`
   - c) `str`
   - d) `set`

2. Which of the following is mutable?
   - a) `tuple`
   - b) `int`
   - c) `float`
   - d) `set`

3. What happens if you try to use a list as a dictionary key?
   - a) It works fine
   - b) Python raises `TypeError` because lists are unhashable
   - c) Python automatically converts it to a tuple
   - d) It raises `ValueError`

4. Can a tuple containing a list be used as a dictionary key?
   - a) Yes, always
   - b) No, because the tuple contains a mutable element
   - c) Yes, if the list is empty
   - d) Only in Python 3.10+

5. After `a = [1, 2]; b = a; b.append(3)`, what is `a`?
   - a) `[1, 2]`
   - b) `[1, 2, 3]`
   - c) `[1, 2, [3]]`
   - d) Error

6. Why can't you change a character in a string with `s[0] = "H"`?
   - a) Strings use 0-based indexing
   - b) Strings are immutable
   - c) Strings don't support indexing
   - d) You need to use `.replace()`

7. What is the output? `def f(x): x = x + 1; n = 10; f(n); print(n)`
   - a) `10`
   - b) `11`
   - c) Error
   - d) `None`

8. What is the output? `def f(lst): lst.append(4); nums = [1, 2, 3]; f(nums); print(nums)`
   - a) `[1, 2, 3]`
   - b) `[1, 2, 3, 4]`
   - c) `[4, 1, 2, 3]`
   - d) Error

9. Why are mutable types not allowed as dictionary keys?
   - a) They take too much memory
   - b) They can change, breaking the hash table's integrity
   - c) Python didn't implement it yet
   - d) They are too slow to compare

10. Is a `frozenset` mutable or immutable?
    - a) Mutable
    - b) Immutable
    - c) It depends on the elements
    - d) Neither

**Answers:** 1-c, 2-d, 3-b, 4-b, 5-b, 6-b, 7-a, 8-b, 9-b, 10-b
