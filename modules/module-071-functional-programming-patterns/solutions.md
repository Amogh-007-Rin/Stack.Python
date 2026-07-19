# Solutions: Functional Programming Patterns

## Exercise 1: Pure Functions
```python
def add_to_total(total: int, value: int) -> int:
    return total + value
```

## Exercise 2: Map and Filter
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
squared_evens = list(map(lambda x: x**2, evens))
print(squared_evens)  # [4, 16, 36, 64, 100]
```

## Exercise 3: Reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

## Exercise 4: Partial Functions
```python
from functools import partial

def multiply(a: int, b: int) -> int:
    return a * b

double = partial(multiply, 2)
print(double(5))  # 10
```

## Exercise 5: Operator Module
```python
from operator import itemgetter

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
]
sorted_people = sorted(people, key=itemgetter('age'))
print(sorted_people)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

## Exercise 6: LRU Cache
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))  # 12586269025
```

## Challenge: Function Composition
```python
def compose(f, g):
    return lambda x: f(g(x))

def double(x: int) -> int:
    return x * 2

def square(x: int) -> int:
    return x ** 2

double_then_square = compose(square, double)
print(double_then_square(3))  # (3*2)^2 = 36
```
