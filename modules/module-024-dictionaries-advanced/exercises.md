# Exercises: Dictionaries: Advanced

## Exercise 1: Nested Dicts
Create a nested dictionary `company` with departments as keys and lists of employee names as values. Include at least 3 departments.

## Exercise 2: Accessing Nested Data
Given `data = {"users": {"alice": {"age": 30, "email": "alice@x.com"}}}`, write code to access Alice's email.

## Exercise 3: update()
Given `d1 = {"a": 1, "b": 2}` and `d2 = {"b": 3, "c": 4}`, use `.update()` to merge `d2` into `d1`. Print the result.

## Exercise 4: pop()
Remove the key `"b"` from `d = {"a": 1, "b": 2, "c": 3}` using `.pop()`. Store the removed value and print it. Then try to pop a non-existent key with a default.

## Exercise 5: setdefault()
Use `setdefault` to add `"d": 4` to a dict if `"d"` doesn't exist. Then try it again — notice it doesn't overwrite.

## Exercise 6: fromkeys()
Create a dictionary from the list `["name", "age", "city"]` with default value `None`.

## Exercise 7: Dict Comprehension
Given `words = ["hello", "world", "python"]`, create a dict comprehension mapping each word to its length.

## Exercise 8: Merging with | (3.9+)
Merge `a = {"x": 1, "y": 2}` and `b = {"y": 3, "z": 4}` using the `|` operator. Note which value wins for `"y"`.

## Exercise 9: defaultdict
Using `defaultdict(list)`, group a list of words by their first letter. Test with `["apple", "banana", "avocado", "cherry"]`.

## Exercise 10: Invert a Dict
Write a function `invert_dict(d)` that returns a new dict swapping keys and values. Handle the case where multiple keys have the same value by storing them in a list.
