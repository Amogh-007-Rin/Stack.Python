# Quiz: Dictionaries: Advanced

1. How do you access a value in a nested dict `data = {"a": {"b": 1}}`?
   - a) `data["a"]["b"]`
   - b) `data["a", "b"]`
   - c) `data.get("a.b")`
   - d) `data["a"]["c"]`

2. What does `.update()` do?
   - a) Replaces the entire dictionary
   - b) Merges another dict's keys/values into the current one
   - c) Updates all values to a default
   - d) Refreshes dictionary ordering

3. What does `.pop("key")` return?
   - a) The key
   - b) The value for that key
   - c) `True` if successful
   - d) The entire dictionary

4. What is the result? `d = {"a": 1}; d.setdefault("a", 99); print(d["a"])`
   - a) `99`
   - b) `1`
   - c) `None`
   - d) Error

5. What does `dict.fromkeys(["x", "y"], 0)` return?
   - a) `{"x": 0, "y": 0}`
   - b) `{"x": ["y"], "z": 0}`
   - c) `["x", "y", 0]`
   - d) `{0: "x", 0: "y"}`

6. Which creates `{1: "a", 4: "b", 9: "c"}` using comprehension?
   - a) `{x: chr(96+x) for x in [1, 4, 9]}`
   - b) `{x**2: chr(96+x) for x in [1, 4, 9]}`
   - c) `[x: chr(96+x) for x in [1, 4, 9]]`
   - d) `{x for x in [1, 4, 9]}`

7. What does the `|` operator do on dicts in Python 3.9+?
   - a) Computes the intersection of keys
   - b) Merges two dicts (right side wins conflicts)
   - c) Computes the symmetric difference
   - d) Filters the dictionary

8. Which module provides `defaultdict`?
   - a) `itertools`
   - b) `collections`
   - c) `functools`
   - d) `defaultdict` is built-in

9. What does `defaultdict(int)` return for a missing key?
   - a) `None`
   - b) `0`
   - c) `False`
   - d) `KeyError`

10. How do you safely remove a key from a dict without getting an error if it's missing?
    - a) `del d["key"]`
    - b) `d.pop("key")`
    - c) `d.pop("key", None)`
    - d) `d.remove("key")`

**Answers:** 1-a, 2-b, 3-b, 4-b, 5-a, 6-a, 7-b, 8-b, 9-b, 10-c
