# Quiz: Dictionaries: Basics

1. Which of the following creates an empty dictionary?
   - a) `d = {}`
   - b) `d = dict()`
   - c) Both a and b
   - d) `d = []`

2. How do you access the value for key `"name"` safely (returning `None` if missing)?
   - a) `d["name"]`
   - b) `d.get("name")`
   - c) `d("name")`
   - d) `d.name`

3. What happens if you access a missing key with `[]`?
   - a) Returns `None`
   - b) Raises `KeyError`
   - c) Returns `False`
   - d) Raises `ValueError`

4. How do you add a new key-value pair to a dictionary?
   - a) `d.add(key, value)`
   - b) `d[key] = value`
   - c) `d.append(key, value)`
   - d) `d.insert(key, value)`

5. Which method returns all key-value pairs as tuples?
   - a) `.keys()`
   - b) `.values()`
   - c) `.items()`
   - d) `.pairs()`

6. How do you check if a key exists in a dictionary?
   - a) `d.contains(key)`
   - b) `key in d`
   - c) `d.has_key(key)`
   - d) `d.exists(key)`

7. What does `len(d)` return for a dictionary?
   - a) The number of keys
   - b) The number of values
   - c) The number of key-value pairs
   - d) All of the above (they are the same)

8. Which of the following can be a dictionary key?
   - a) A list
   - b) A dictionary
   - c) A tuple
   - d) A set

9. What is the output? `d = {"a": 1, "b": 2}; print(d.get("c", 0))`
   - a) `None`
   - b) `0`
   - c) `KeyError`
   - d) `False`

10. What does `for k in d:` iterate over?
    - a) Keys
    - b) Values
    - c) Items
    - d) All of the above

**Answers:** 1-c, 2-b, 3-b, 4-b, 5-c, 6-b, 7-c, 8-c, 9-b, 10-a
