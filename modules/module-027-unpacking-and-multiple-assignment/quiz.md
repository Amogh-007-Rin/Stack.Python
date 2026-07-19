# Quiz: Unpacking and Multiple Assignment

1. What does `a, b = (1, 2)` do?
   - a) Creates a tuple
   - b) Assigns `a=1`, `b=2`
   - c) Raises an error
   - d) Assigns `a=(1,2)`, `b=None`

2. How do you swap two variables `x` and `y` in one line?
   - a) `swap(x, y)`
   - b) `x, y = y, x`
   - c) `x = y; y = x`
   - d) `x ^= y; y ^= x; x ^= y`

3. What is the result of `first, *rest = [1, 2, 3, 4]`?
   - a) `first=1, rest=[2, 3, 4]`
   - b) `first=1, rest=2`
   - c) `first=[1], rest=[2, 3, 4]`
   - d) Error

4. What does `a, *b, c = (1, 2, 3, 4)` produce?
   - a) `a=1, b=[2, 3], c=4`
   - b) `a=1, b=2, c=4`
   - c) `a=1, b=[2], c=4`
   - d) Error

5. What does `_` conventionally mean in unpacking?
   - a) It's the last element
   - b) A throwaway value to ignore
   - c) A wildcard matching anything
   - d) It creates a variable named underscore

6. What is the output? `for a, b in [(1, 2), (3, 4)]: print(a + b)`
   - a) `3 7`
   - b) `(1, 2) (3, 4)`
   - c) `1 2 3 4`
   - d) `12 34`

7. Can you unpack a string?
   - a) Yes, strings are iterable
   - b) No, strings are not sequences
   - c) Only with list()
   - d) Only if it's a single character

8. What does `a, b = b, a` actually do?
   - a) Assigns `a` to `b` then `b` to `a` (single swap)
   - b) Creates a tuple `(b, a)` and unpacks it
   - c) Raises a syntax error
   - d) Nothing; it's a no-op

9. How do you unpack only the first and last elements of a list of unknown length?
   - a) `first, *_, last = lst`
   - b) `first, last = lst`
   - c) `first, *last = lst`
   - d) `first, _, last = lst`

10. What is the output? `a, b, *c = range(5); print(c)`
    - a) `[2, 3, 4]`
    - b) `[3, 4]`
    - c) `(3, 4)`
    - d) `[0, 1]`

**Answers:** 1-b, 2-b, 3-a, 4-a, 5-b, 6-a, 7-a, 8-b, 9-a, 10-a
