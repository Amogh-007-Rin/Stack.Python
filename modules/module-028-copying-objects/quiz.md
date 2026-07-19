# Quiz: Copying Objects

1. After `a = [1, 2, 3]; b = a; b[0] = 99`, what is `a[0]`?
   - a) `1`
   - b) `99`
   - c) Error
   - d) `None`

2. What does `list.copy()` return?
   - a) A reference to the same list
   - b) A shallow copy of the list
   - c) A deep copy of the list
   - d) A tuple version of the list

3. What is a shallow copy?
   - a) Copies the object but not its nested objects
   - b) Copies everything recursively
   - c) Copies only the first element
   - d) Creates a reference

4. Which module provides `deepcopy()`?
   - a) `copy`
   - b) `deepcopy`
   - c) `collections`
   - d) `itertools`

5. After `copy.deepcopy(nested)`, modifying a nested list in the copy...
   - a) Also modifies the original
   - b) Does NOT modify the original
   - c) Raises an error
   - d) Depends on the nesting depth

6. Why might you choose shallow copy over deep copy?
   - a) Shallow copy is faster and uses less memory
   - b) Shallow copy is the only option for lists
   - c) Deep copy doesn't work on dicts
   - d) Shallow copy is more thorough

7. What is the output? `d = {"a": [1, 2]}; c = d.copy(); c["a"].append(3); print(d["a"])`
   - a) `[1, 2]`
   - b) `[1, 2, 3]`
   - c) `[3]`
   - d) Error

8. Does `copy.copy()` work on tuples?
   - a) Yes, and it creates a new tuple
   - b) Yes, but it returns the same tuple (immutable)
   - c) No, tuples can't be copied
   - d) It raises TypeError

9. What is the difference between `list.copy()` and `copy.copy(list)`?
   - a) They are equivalent for lists
   - b) `.copy()` is shallow, `copy.copy()` is deep
   - c) `.copy()` is deep, `copy.copy()` is shallow
   - d) `copy.copy()` doesn't work on lists

10. Which of the following creates a truly independent copy of `[[1, 2], [3, 4]]`?
    - a) `nested.copy()`
    - b) `list(nested)`
    - c) `nested[:]`
    - d) `copy.deepcopy(nested)`

**Answers:** 1-b, 2-b, 3-a, 4-a, 5-b, 6-a, 7-b, 8-b, 9-a, 10-d
