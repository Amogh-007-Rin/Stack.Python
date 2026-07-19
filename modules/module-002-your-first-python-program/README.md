# Module 002: Your First Python Program

> **Phase:** 1. Fundamentals  |  **Estimated time:** 1 hour  |  **Milestone Project:** No

## Prerequisites
- [Module 001: Setting Up Your Environment](../module-001-setting-up-your-environment/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Use the `print()` function to display text
- Write single-line and multi-line comments with `#`
- Create string literals with single and double quotes
- Pass multiple arguments to `print()`
- Perform basic arithmetic inside `print()`
- Create and run a `.py` file

## Why This Matters
Every program you will ever write communicates something. The `print()` function is your first tool for making Python talk back to you. Mastering the basics of output and code organization sets the stage for everything that follows.

## Concept Explanation

### The `print()` Function

`print()` is a built-in Python function that displays output to the screen. You pass values inside the parentheses:

```python
print("Hello, World!")
# Output: Hello, World!
```

The text inside quotes is called a **string literal**. You can use single quotes or double quotes — Python treats them the same:

```python
print('Single quotes work too')
print("Double quotes work as well")
```

### Multiple Arguments to `print()`

You can pass several items to `print()` separated by commas. They will be printed with a space between each:

```python
print("Hello", "Python", "World!")
# Output: Hello Python World!
```

### Simple Arithmetic in `print()`

You can put math expressions directly inside `print()`. Python evaluates the expression and prints the result:

```python
print(2 + 3)
# Output: 5

print(10 - 4)
# Output: 6

print(3 * 7)
# Output: 21

print(8 / 2)
# Output: 4.0
```

Notice: division always produces a float (number with a decimal point).

### Comments

Comments are notes for humans that Python ignores. Use the `#` symbol:

```python
# This is a comment
print("Hello")  # This is also a comment after code

# You can have
# multi-line comments
# by starting each line with #
```

Use comments to explain *why* your code does something, not what it does (the code itself should show the what).

### Running a .py File

Save your code in a file with the `.py` extension, then run it from the terminal:

```
python3 myprogram.py
```

Every line in the file executes in order, top to bottom.

## Common Pitfalls

1. **Forgetting quotes**: `print(Hello)` causes a `NameError` because `Hello` is not defined. Always quote strings.
2. **Mixing quote types inconsistently**: Start and end with the same quote — `print("hello')` causes a `SyntaxError`.
3. **Missing parentheses**: `print "Hello"` is Python 2 syntax. In Python 3, parentheses are required.
4. **Commas inside strings**: `print("Hello, World")` is fine; commas *between* arguments are separators.
5. **Thinking print() returns a value**: `print()` displays text but returns `None`.

## Hands-On Walkthrough

Let's build a small program step by step.

1. Create a file called `greetings.py`.
2. Add a comment at the top:
   ```python
   # My first program - greetings
   ```
3. Add a print statement with multiple arguments:
   ```python
   print("Welcome", "to", "Python", "3.12!")
   ```
4. Add some arithmetic:
   ```python
   print("The answer to 2 + 3 is", 2 + 3)
   ```
5. Add another print:
   ```python
   print("Goodbye!")
   ```
6. Save the file and run it:
   ```
   python3 greetings.py
   ```

Full file content:
```python
# My first program - greetings
print("Welcome", "to", "Python", "3.12!")
print("The answer to 2 + 3 is", 2 + 3)
print("Goodbye!")
```

Expected output:
```
Welcome to Python 3.12!
The answer to 2 + 3 is 5
Goodbye!
```

## Key Takeaways

- `print()` displays output to the screen.
- Strings must be enclosed in matching quotes (single or double).
- Multiple arguments to `print()` are separated by commas and printed with spaces.
- Arithmetic expressions inside `print()` are evaluated first, then printed.
- Comments start with `#` and are ignored by Python.
- Every `.py` file runs top to bottom.
- Division (`/`) always returns a float.
- Missing parentheses cause errors in Python 3.

## Further Reading
- [Built-in Functions: print() (docs.python.org)](https://docs.python.org/3/library/functions.html#print)
- [Python Basics: Comments (docs.python.org)](https://docs.python.org/3/tutorial/introduction.html#comments)

## Next Module
Learn how to store and work with data in [Module 003: Variables and Data Types](../module-003-variables-and-data-types/README.md).
