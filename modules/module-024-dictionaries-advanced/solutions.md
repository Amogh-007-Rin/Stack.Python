# Solutions: Dictionaries: Advanced

## Exercise 1
```python
company = {
    "Engineering": ["Alice", "Bob"],
    "Marketing": ["Charlie", "Diana"],
    "Sales": ["Eve"]
}
print(company)
```

## Exercise 2
```python
data = {"users": {"alice": {"age": 30, "email": "alice@x.com"}}}
print(data["users"]["alice"]["email"])  # alice@x.com
```

## Exercise 3
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

## Exercise 4
```python
d = {"a": 1, "b": 2, "c": 3}
removed = d.pop("b")
print(removed)  # 2
print(d)        # {'a': 1, 'c': 3}
safe = d.pop("z", "Not found")
print(safe)     # Not found
```

## Exercise 5
```python
d = {"a": 1, "b": 2}
d.setdefault("d", 4)
print(d)  # {'a': 1, 'b': 2, 'd': 4}
d.setdefault("d", 99)
print(d)  # {'a': 1, 'b': 2, 'd': 4} — unchanged
```

## Exercise 6
```python
keys = ["name", "age", "city"]
result = dict.fromkeys(keys, None)
print(result)  # {'name': None, 'age': None, 'city': None}
```

## Exercise 7
```python
words = ["hello", "world", "python"]
lengths = {word: len(word) for word in words}
print(lengths)  # {'hello': 5, 'world': 5, 'python': 6}
```

## Exercise 8
```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = a | b
print(merged)  # {'x': 1, 'y': 3, 'z': 4}
```

## Exercise 9
```python
from collections import defaultdict

words = ["apple", "banana", "avocado", "cherry"]
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
print(dict(groups))
# {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}
```

## Exercise 10
```python
def invert_dict(d):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted

print(invert_dict({"a": 1, "b": 2, "c": 1}))
# {1: ['a', 'c'], 2: ['b']}
```
