# Module 036: Higher-Order Functions (map, filter, reduce)

> **Phase:** 4. Functions  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)
- Module 034 (Lambda Functions)

## Learning Objectives
By the end of this module, you will be able to:
- Use `map()` to transform iterables with a function
- Use `filter()` to select elements with a predicate
- Use `functools.reduce()` to accumulate values
- Treat functions as first-class objects (pass as arguments, return them)
- Use `sorted()` with a custom `key` function

## Why This Matters
Higher-order functions (functions that take or return other functions) are the foundation of functional programming in Python. They allow concise, declarative data processing without explicit loops.

## Concept Explanation

### Functions as First-Class Objects

In Python, functions are objects. You can assign them to variables, pass them as arguments, and return them from other functions:

```python
def square(x):
    return x * x

f = square       # assign to variable
print(f(5))      # call through variable

def apply(func, values):
    return [func(v) for v in values]

print(apply(square, [1, 2, 3]))  # [1, 4, 9]
```

### `map()` — Transform Each Element

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
# [2, 4, 6, 8]
```

### `filter()` — Select Elements by Predicate

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4, 6]
```

### `functools.reduce()` — Accumulate

```python
from functools import reduce
total = reduce(lambda a, b: a + b, [1, 2, 3, 4])
# 10
```

### `sorted()` with Key

```python
words = ["python", "java", "c", "javascript"]
sorted(words, key=len)
# ['c', 'java', 'python', 'javascript']
```

### Returning Functions

```python
def make_multiplier(n):
    """Return a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))  # 10
```

## Common Pitfalls

1. **Forgetting to convert `map()`/`filter()` to a list**: They return iterators, not lists.
2. **Using `reduce()` when a built-in exists**: `sum()`, `min()`, `max()` are clearer.
3. **Overusing lambdas**: Named functions are more readable for complex logic.
4. **Modifying the original list**: `map()` and `filter()` create new iterables.

## Hands-On Walkthrough

1. Create a list of numbers and use `map()` with a lambda to cube each.
2. Use `filter()` to keep only positive numbers from `[-3, -1, 0, 2, 5]`.
3. Use `reduce()` to find the maximum in a list.
4. Write a function `make_power(exp)` that returns a function raising its argument to `exp`.

## Key Takeaways

- `map(func, iterable)` — transforms each element.
- `filter(predicate, iterable)` — keeps elements where predicate is True.
- `functools.reduce(func, iterable)` — accumulates values.
- Functions are first-class: pass them, return them, assign them.
- `sorted(iterable, key=func)` — sort with custom key.

## Further Reading
- [Python docs: map](https://docs.python.org/3/library/functions.html#map)
- [Python docs: filter](https://docs.python.org/3/library/functions.html#filter)
- [Python docs: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

## Next Module
Continue to **Module 037: Decorators: Basics**.
