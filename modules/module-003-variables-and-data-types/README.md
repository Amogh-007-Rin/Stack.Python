# Module 003: Variables and Data Types

> **Phase:** 1. Fundamentals  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 002: Your First Python Program](../module-002-your-first-python-program/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Assign values to variables using `=`
- Follow Python naming rules for variables
- Explain what dynamic typing means
- Identify the four basic data types: `int`, `float`, `str`, `bool`
- Use `type()` to check a value's data type

## Why This Matters
Variables are the building blocks of every program. They let you store, label, and reuse data. Understanding data types is critical because different types behave differently — you cannot add a number to a text string without converting first.

## Concept Explanation

### Variable Assignment

A variable is a named container that holds a value. Use the `=` sign to assign a value to a name:

```python
name = "Alice"
age = 25
height = 1.68
is_student = True
```

Think of it as: *name* ← *value*. The variable goes on the left, the value on the right.

Once assigned, you can use the variable's name anywhere you would use the value:

```python
name = "Alice"
age = 25
print(name)     # Output: Alice
print(age + 1)  # Output: 26
```

### Naming Rules

Python has strict rules for variable names:

| Rule | Example ✅ | Example ❌ |
|------|-----------|-----------|
| Must start with a letter or underscore | `name`, `_count` | `1name` |
| Can contain letters, digits, underscores | `user_name`, `data2` | `user-name` |
| Case-sensitive | `name` and `Name` are different | — |
| Cannot be a reserved keyword | — | `if`, `for`, `class`, `while` |

Python **keywords** (reserved words) include: `if`, `else`, `elif`, `for`, `while`, `def`, `class`, `import`, `from`, `return`, `True`, `False`, `None`, `and`, `or`, `not`, `in`, `is`, `with`, `as`, `try`, `except`, `finally`, `raise`, `yield`, `lambda`, `pass`, `break`, `continue`.

Use descriptive names — `student_count` is better than `sc`.

### Dynamic Typing

Python is **dynamically typed**. A variable can hold any type of value, and the type can change over time:

```python
value = 42          # value is an int
print(value)
value = "now text"  # value is now a str
print(value)
```

The same variable can hold an integer, then a string, then a float. This is flexible but requires care — it can lead to runtime errors if you assume a type that isn't there.

### Basic Data Types

Python has four fundamental data types you will use constantly:

#### `int` — Integer
Whole numbers, positive or negative, with no decimal point:
```python
count = 10
negative = -5
zero = 0
large = 1_000_000  # underscores for readability
```

#### `float` — Floating-point number
Numbers with a decimal point:
```python
pi = 3.14159
temperature = -2.5
scientific = 1.5e10  # 1.5 × 10^10
```

#### `str` — String
Text enclosed in quotes:
```python
greeting = "Hello"
name = 'Alice'
multi = "She said, \"Hi!\""
```

#### `bool` — Boolean
Only two values: `True` or `False`:
```python
is_sunny = True
is_raining = False
```

Note: `True` and `False` must be capitalized. `true` and `false` cause errors.

### The `type()` Function

Use `type()` to discover the data type of any value:

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

This is especially useful when debugging or when you are unsure what type a variable holds.

## Common Pitfalls

1. **Using unassigned variables**: `print(x)` where `x` has never been assigned causes `NameError`.
2. **Spelling `True` / `False` wrong**: `true` and `false` (lowercase) are not valid Python.
3. **Using a keyword as a variable name**: `if = 5` causes `SyntaxError`.
4. **Forgetting that `type()` returns a type object, not a string**: `type(x) == "int"` is False; use `type(x) == int` or `isinstance(x, int)`.
5. **Assuming division between two ints returns an int**: `10 / 3` returns `3.333...` (a float).

## Hands-On Walkthrough

Create a file `profile.py` that stores information about yourself using variables:

```python
# My profile
first_name = "Alex"
last_name = "Smith"
age = 30
height = 1.75
likes_python = True

print("First name:", first_name)
print("Last name:", last_name)
print("Age:", age)
print("Height:", height)
print("Likes Python:", likes_python)
```

Now add some `type()` calls to verify the types:

```python
print(type(first_name))
print(type(age))
print(type(height))
print(type(likes_python))
```

Expected output:
```
First name: Alex
Last name: Smith
Age: 30
Height: 1.75
Likes Python: True
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Experiment: change `age` to `30.0` and see `type(age)` change from `int` to `float`.

## Key Takeaways

- Use `=` to assign values to variables.
- Variable names: start with letter/underscore, contain letters/digits/underscores, case-sensitive.
- Python is dynamically typed — a variable's type can change.
- Four basic types: `int` (whole numbers), `float` (decimals), `str` (text), `bool` (True/False).
- `type()` reveals the type of any value or variable.
- `True` and `False` are capitalized keywords.
- Underscores in numbers (`1_000_000`) are ignored and improve readability.
- Division always returns a `float`.

## Further Reading
- [Python Data Types (docs.python.org)](https://docs.python.org/3/library/stdtypes.html)
- [Variables in Python (docs.python.org)](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)

## Next Module
Learn how to convert between types in [Module 004: Type Conversion and Casting](../module-004-type-conversion-and-casting/README.md).
