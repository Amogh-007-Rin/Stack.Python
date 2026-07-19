# Module 034: Lambda Functions

> **Phase:** 4. Functions  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)
- Module 032 (Function Arguments)

## Learning Objectives
By the end of this module, you will be able to:
- Write lambda functions with the `lambda` keyword
- Know when lambdas are appropriate (short callbacks)
- Understand the limitations of lambdas (single expression only)
- Use lambdas with `sorted()` and `key=`
- Use lambdas with `map()` and `filter()` briefly

## Why This Matters
Lambdas allow you to write small, throwaway functions inline without a `def` statement. They are essential for callbacks, sorting with custom keys, and functional programming patterns.

## Concept Explanation

### Lambda Syntax

```python
lambda arguments: expression
```

A lambda is a function without a name that evaluates a single expression:

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

This is equivalent to:

```python
def square(x):
    return x ** 2
```

### When to Use Lambdas

Use lambdas for **short, simple operations** passed directly as arguments:

- Sorting with custom keys
- Callbacks for GUI/event handling
- Short transformations with `map()` and `filter()`

### Limitations

- **Single expression only** — no statements, no assignments, no loops.
- No docstrings — hard to self-document.
- Harder to debug — no name in tracebacks.

### Sorting with `key=lambda`

```python
students = [("Alice", 85), ("Bob", 72), ("Charlie", 90)]
students.sort(key=lambda s: s[1])  # sort by grade
print(students)  # [('Bob', 72), ('Alice', 85), ('Charlie', 90)]
```

### Lambda with `map()` and `filter()`

```python
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

### Lambda with Conditional Expression

```python
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20
```

## Common Pitfalls

1. **Trying to use statements**: `lambda x: return x + 1` is invalid — `return` is a statement.
2. **Overusing lambdas**: If it's more than one expression, use `def`.
3. **Capturing loop variables**: Lambdas in loops capture by reference, not by value.

## Hands-On Walkthrough

1. Write a lambda that returns the absolute value and test it.
2. Sort a list of strings by their length using `sorted()` with `key=lambda`.
3. Use `map()` with a lambda to convert temperatures from Celsius to Fahrenheit.
4. Use `filter()` with a lambda to keep only positive numbers from a list.

## Key Takeaways

- Lambda: `lambda args: expression` — anonymous, inline, single expression.
- Best for short callbacks (sorting, mapping, filtering).
- Cannot contain statements (no `return`, `if/else` blocks, loops).
- If it's complex, use `def` instead.

## Further Reading
- [Python docs: Lambda Expressions](https://docs.python.org/3/reference/expressions.html#lambda)
- [Real Python: Python Lambda Functions](https://realpython.com/python-lambda/)

## Next Module
Continue to **Module 035: Recursion**.
