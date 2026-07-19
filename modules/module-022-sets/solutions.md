# Solutions: Sets

## Exercise 1
```python
fruits = {"apple", "banana", "cherry"}
dupes = set(["a", "b", "c", "a", "b"])
print(fruits)
print(dupes)  # {'a', 'b', 'c'} — duplicates removed
```

## Exercise 2
```python
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(99)  # no error
try:
    s.remove(99)
except KeyError as e:
    print(f"KeyError: {e}")
popped = s.pop()
print("Popped:", popped)
s_copy = s.copy()
print(s_copy)
```

## Exercise 3
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)         # {1, 2, 3, 4, 5, 6}
print(A.union(B))    # {1, 2, 3, 4, 5, 6}
```

## Exercise 4
```python
print(A & B)             # {3, 4}
print(A.intersection(B)) # {3, 4}
```

## Exercise 5
```python
print(A - B)  # {1, 2}
print(B - A)  # {5, 6}
```

## Exercise 6
```python
print(A ^ B)                   # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
```

## Exercise 7
```python
squares = {x**2 for x in range(10) if x % 2 == 0}
print(squares)  # {0, 64, 4, 36, 16}
```

## Exercise 8
```python
fs = frozenset([1, 2, 3, 2, 1])
try:
    fs.add(4)
except AttributeError as e:
    print(f"Error: {e}")
d = {fs: "frozenset key"}
print(d)
```

## Exercise 9
```python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
unique = sorted(set(names))
print(unique)  # ['Alice', 'Bob', 'Charlie', 'David']
```

## Exercise 10
```python
import random

nums = [random.randint(1, 20) for _ in range(100)]
unique = set(nums)
missing = set(range(1, 21)) - unique
print(f"Unique numbers: {len(unique)}")
print(f"Missing: {sorted(missing)}")
```
