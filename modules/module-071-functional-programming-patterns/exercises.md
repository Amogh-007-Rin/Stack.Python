# Exercises: Functional Programming Patterns

## Exercise 1: Pure Functions
Convert this impure function to a pure function:
```python
total = 0
def add_to_total(value):
    global total
    total += value
    return total
```

## Exercise 2: Map and Filter
Given a list of numbers, use map and filter to:
1. Filter out odd numbers
2. Square the remaining even numbers

## Exercise 3: Reduce
Use functools.reduce to find the product of all numbers in a list.

## Exercise 4: Partial Functions
Create a partial function `double` from a `multiply` function that always doubles its argument.

## Exercise 5: Operator Module
Use operator.itemgetter to sort a list of dictionaries by a specific key.

## Exercise 6: LRU Cache
Use functools.lru_cache to memoize a recursive Fibonacci function.

## Challenge: Function Composition
Write a `compose` function that takes two functions and returns their composition.
```python
def compose(f, g):
    return lambda x: f(g(x))
```
Then compose `double` and `square` to create `double_then_square`.
