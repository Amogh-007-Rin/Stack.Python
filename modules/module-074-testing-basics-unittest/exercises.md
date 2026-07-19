# Exercises: Testing Basics: unittest

Use the code below for exercises:

```python
# calculator.py
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

## Exercise 1: First Test Case
Create a test class `TestCalculator` that tests `add` and `subtract`.

## Exercise 2: Test Division
Add tests for `divide`, including a test that it raises `ValueError` for division by zero.

## Exercise 3: setUp
Use `setUp` to create sample test data shared across multiple tests.

## Exercise 4: Parametrize-like Testing
Test `multiply` with several inputs using separate test methods or a loop.

## Exercise 5: Test Discovery
Organize tests in a `tests/` directory and run them with `python -m unittest discover`.

## Exercise 6: String Processing Tests
Write a test class for a function `reverse_string(s: str) -> str` that tests edge cases: empty string, single character, palindrome, normal string.
