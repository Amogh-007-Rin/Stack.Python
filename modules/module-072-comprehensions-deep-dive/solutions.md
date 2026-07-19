# Solutions: Comprehensions Deep Dive

## Exercise 1: Basic List Comprehension
```python
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Exercise 2: Conditional List Comprehension
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parity = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(parity)  # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
```

## Exercise 3: Dict Comprehension
```python
ascii_map = {c: ord(c) for c in "hello"}
print(ascii_map)  # {'h': 104, 'e': 101, 'l': 108, 'o': 111}
```

## Exercise 4: Set Comprehension
```python
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16, 25}
```

## Exercise 5: Nested Comprehension
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

## Exercise 6: Generator Expression
```python
result = sum(x**2 for x in range(1, 1001))
print(result)  # 333833500
```

## Exercise 7: Nested Dict Comprehension
```python
table = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(table)
# {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}
```
