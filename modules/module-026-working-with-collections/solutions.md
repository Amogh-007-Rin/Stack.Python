# Solutions: Working with Collections

## Exercise 1
```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## Exercise 2
```python
pairs = [("x", 1), ("y", 2), ("z", 3)]
letters, numbers = zip(*pairs)
print(letters)  # ('x', 'y', 'z')
print(numbers)  # (1, 2, 3)
```

## Exercise 3
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
```

## Exercise 4
```python
for i, fruit in enumerate(fruits, start=10):
    print(f"{i}: {fruit}")
```

## Exercise 5
```python
from itertools import count

evens = []
for n in count(0, 2):
    if n >= 20:
        break
    evens.append(n)
print(evens)  # [0, 2, 4, ..., 18]
```

## Exercise 6
```python
from itertools import cycle

rps = ["rock", "paper", "scissors"]
count = 0
for item in cycle(rps):
    if count >= 5:
        break
    print(item)
    count += 1
```

## Exercise 7
```python
from itertools import chain

combined = list(chain([1, 2], [3, 4], [5, 6]))
print(combined)  # [1, 2, 3, 4, 5, 6]
```

## Exercise 8
```python
from itertools import product

for p in product(["A", "B"], [1, 2, 3]):
    print(p)
# ('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3)
```

## Exercise 9
```python
from itertools import permutations

for p in permutations(["a", "b", "c"], 2):
    print(p)
# ('a','b'), ('a','c'), ('b','a'), ('b','c'), ('c','a'), ('c','b')
```

## Exercise 10
```python
from itertools import combinations

for c in combinations(["a", "b", "c"], 2):
    print(c)
# ('a','b'), ('a','c'), ('b','c')
# Order does not matter — fewer results than permutations
```
