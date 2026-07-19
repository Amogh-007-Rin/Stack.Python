# Solutions: Tuples

## Exercise 1
```python
colors = ("red", "green", "blue")
print(colors[0])  # red
print(colors[-1])  # blue
```

## Exercise 2
```python
t = (10, 20, 30)
try:
    t[1] = 25
except TypeError as e:
    print(f"Cannot modify tuple: {e}")
```

## Exercise 3
```python
point = (4, 7)
x, y = point
print(x + y)  # 11
```

## Exercise 4
```python
def min_max(nums):
    return (min(nums), max(nums))

result = min_max([3, 1, 7, 2, 9])
print(result)  # (1, 9)
```

## Exercise 5
```python
locations = {
    (0, 0): "Origin",
    (1, 2): "School",
    (-1, 3): "Park"
}
print(locations[(1, 2)])  # School
```

## Exercise 6
```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grade"])
alice = Student("Alice", 20, "A")
bob = Student("Bob", 19, "B")
print(alice.name)  # Alice
print(bob.name)    # Bob
```

## Exercise 7
```python
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))   # 3
print(t.index(3))   # 3
```

## Exercise 8
```python
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums[:5])     # (1, 2, 3, 4, 5)
print(nums[3:8])    # (4, 5, 6, 7, 8)
print(nums[::2])    # (1, 3, 5, 7, 9)
```

## Exercise 9
```python
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
```

## Exercise 10
```python
matrix = ((1, 2, 3), (4, 5, 6))
print(matrix[1][1])  # 5
```
