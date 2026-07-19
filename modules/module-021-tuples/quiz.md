# Quiz: Tuples

1. How do you create an empty tuple?
   - a) `empty = ()`
   - b) `empty = tuple()`
   - c) Both a and b
   - d) `empty = []`

2. What happens if you try to modify a tuple after creation?
   - a) It succeeds silently
   - b) Python raises a `TypeError`
   - c) Python raises a `ValueError`
   - d) The tuple automatically converts to a list

3. Can a tuple be used as a dictionary key?
   - a) Yes, always
   - b) No, never
   - c) Only if all elements are immutable
   - d) Only if it has exactly two elements

4. What is the output? `t = (1, 2, 3); a, b, c = t; print(a, b, c)`
   - a) `(1, 2, 3)`
   - b) `1 2 3`
   - c) `[1, 2, 3]`
   - d) Error

5. Which of the following is NOT a valid tuple?
   - a) `(1,)`
   - b) `()`
   - c) `(1)`
   - d) `(1, 2, 3)`

6. What does `t.count(x)` do?
   - a) Removes all occurrences of x
   - b) Returns the number of times x appears
   - c) Returns the index of x
   - d) Checks if x is in t

7. How do you create a single-element tuple containing the integer 5?
   - a) `t = (5)`
   - b) `t = (5,)`
   - c) `t = tuple(5)`
   - d) `t = [5]`

8. What does `(1, 2, 3)[::-1]` return?
   - a) `(3, 2, 1)`
   - b) `[3, 2, 1]`
   - c) `(1, 2, 3)`
   - d) Error

9. Which module provides `namedtuple`?
   - a) `itertools`
   - b) `collections`
   - c) `functools`
   - d) `math`

10. What is the main difference between tuples and lists?
    - a) Tuples are faster for iteration
    - b) Tuples are immutable, lists are mutable
    - c) Lists can only hold one type
    - d) Tuples use square brackets

**Answers:** 1-c, 2-b, 3-c, 4-b, 5-c, 6-b, 7-b, 8-a, 9-b, 10-b
