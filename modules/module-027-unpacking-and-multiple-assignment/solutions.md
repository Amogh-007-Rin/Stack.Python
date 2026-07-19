# Solutions: Unpacking and Multiple Assignment

## Exercise 1
```python
point = (10, 20)
x, y = point
print(x, y)  # 10 20
```

## Exercise 2
```python
data = ["Alice", 30, "Engineer"]
name, age, job = data
print(name, age, job)
```

## Exercise 3
```python
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5
```

## Exercise 4
```python
nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5
```

## Exercise 5
```python
nums = [1, 2, 3, 4, 5]
first, *rest = nums
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

## Exercise 6
```python
data = ("Alice", 30, "NYC", "555-1234")
name, _, city, _ = data
print(name, city)  # Alice NYC
```

## Exercise 7
```python
def split_name(full_name):
    parts = full_name.split()
    return parts[0], parts[1]

first, last = split_name("Alice Johnson")
print(first, last)  # Alice Johnson
```

## Exercise 8
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
for name, score in students:
    print(f"{name}: {score}")
```

## Exercise 9
```python
nested = (1, (2, 3), 4)
a, (b, c), d = nested
print(a, b, c, d)  # 1 2 3 4
```

## Exercise 10
```python
items = ["a", "b", "c", "d", "e"]
first, second, *rest = items
print(first, second, rest)
# a b ['c', 'd', 'e']

# To drop middle:
first, *_, last = items
print(first, last)  # a e
```
