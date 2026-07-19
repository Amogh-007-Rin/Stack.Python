# Module 036: Solutions

## Exercise 1
```python
nums_str = ["1", "2", "3"]
nums_int = list(map(int, nums_str))
print(nums_int)  # [1, 2, 3]
```

## Exercise 2
```python
nums = [-3, -1, 0, 2, 5, -4]
negatives = list(filter(lambda x: x < 0, nums))
print(negatives)  # [-3, -1, -4]
```

## Exercise 3
```python
from functools import reduce
nums = [2, 3, 5, 7]
product = reduce(lambda a, b: a * b, nums)
print(product)  # 210
```

## Exercise 4
```python
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda w: w.count("a"))
print(sorted_words)  # ['cherry', 'date', 'apple', 'banana']
```

## Exercise 5
```python
def make_power(exp):
    """Return a function that raises its argument to exp.

    Args:
        exp: The exponent

    Returns:
        Function that computes x ** exp
    """
    def power(x):
        return x ** exp
    return power

square = make_power(2)
cube = make_power(3)
print(square(5))  # 25
print(cube(3))    # 27
```

## Exercise 6
```python
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # [11, 22, 33]
```

## Exercise 7
```python
words = ["apple", "banana", "cherry"]
result = list(map(str.upper, filter(lambda w: len(w) > 5, words)))
print(result)  # ['BANANA', 'CHERRY']
```

## Exercise 8
```python
def my_reduce(func, iterable, initial=None):
    """Custom reduce function.

    Args:
        func: Function of two arguments
        iterable: Sequence to reduce
        initial: Optional starting value

    Returns:
        Reduced value
    """
    it = iter(iterable)
    if initial is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("empty sequence with no initial")
    else:
        value = initial
    for item in it:
        value = func(value, item)
    return value

print(my_reduce(lambda a, b: a + b, [1, 2, 3, 4]))  # 10
```

## Exercise 9
```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda p: p["age"], reverse=True)
print(sorted_people)
```

## Exercise 10
```python
def compose(f, g):
    """Return h(x) = f(g(x)).

    Args:
        f: Outer function
        g: Inner function

    Returns:
        Composed function
    """
    def h(x):
        return f(g(x))
    return h

def double(x):
    return x * 2

def add_one(x):
    return x + 1

h = compose(double, add_one)
print(h(5))  # double(add_one(5)) = double(6) = 12
```
