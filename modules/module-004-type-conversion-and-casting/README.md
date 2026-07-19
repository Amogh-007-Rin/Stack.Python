# Module 004: Type Conversion and Casting

> **Phase:** 1. Fundamentals  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 003: Variables and Data Types](../module-003-variables-and-data-types/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Convert between `int`, `float`, `str`, and `bool` using built-in functions
- Distinguish implicit conversion (automatic) from explicit conversion (casting)
- Anticipate and handle common conversion errors like `ValueError`
- Explain why "42" + 3 fails but `int("42") + 3` works

## Why This Matters
Real-world data rarely arrives in the type you need. User input comes as strings, files contain text, and APIs return JSON. Converting between types is a daily task in every Python developer's life.

## Concept Explanation

### Implicit Conversion (Automatic)

Python automatically converts between some types when it makes sense. This always happens in a **safe** direction — widening to avoid data loss:

```python
# int + float → float (no data loss)
result = 3 + 2.0
print(result)      # 5.0
print(type(result))  # <class 'float'>

# int + bool → int (True=1, False=0)
print(10 + True)   # 11
print(10 + False)  # 10
```

Python does **not** implicitly convert strings to numbers:

```python
print("42" + 3)  # TypeError: can only concatenate str (not "int") to str
```

This gives an error because Python refuses to guess your intent.

### Explicit Conversion (Casting)

You control conversion using the type functions as constructors:

| Function | Converts To | Example | Result |
|----------|-------------|---------|--------|
| `int(x)` | integer | `int("42")` | `42` |
| `float(x)` | float | `float("3.14")` | `3.14` |
| `str(x)` | string | `str(42)` | `"42"` |
| `bool(x)` | boolean | `bool(1)` | `True` |

#### `int()` — Convert to Integer

```python
print(int(3.99))     # 3 (truncates toward zero)
print(int("42"))     # 42
print(int(True))     # 1
print(int(False))    # 0
```

#### `float()` — Convert to Float

```python
print(float(3))      # 3.0
print(float("3.14")) # 3.14
print(float("1e3"))  # 1000.0
print(float(True))   # 1.0
```

#### `str()` — Convert to String

```python
print(str(42))       # "42"
print(str(3.14))     # "3.14"
print(str(True))     # "True"
```

#### `bool()` — Convert to Boolean

The bool conversion follows truthiness rules:
- Numbers: `0` is `False`, everything else is `True`
- Strings: empty string `""` is `False`, everything else is `True`
- `None` is always `False`

```python
print(bool(1))       # True
print(bool(0))       # False
print(bool(-5))      # True
print(bool(""))      # False
print(bool("Text"))  # True
print(bool(None))    # False
```

### Common Conversion Errors

```python
int("hello")   # ValueError: invalid literal for int() with base 10: 'hello'
int("3.14")    # ValueError: invalid literal for int() with base 10: '3.14'
float("3,14")  # ValueError (comma decimal not allowed in Python)
```

Always ensure the string has the right format before converting. Leading/trailing whitespace is fine:

```python
print(int("  42  "))  # 42
```

## Common Pitfalls

1. **Trying to convert "3.14" directly to int**: `int("3.14")` raises `ValueError`. Convert to float first: `int(float("3.14"))` → `3`.
2. **Forgetting that bool("False") is True**: Any non-empty string is `True`, including `"False"` and `"0"`.
3. **Assuming int() rounds**: `int(3.9)` yields `3`, not `4`. It truncates, not rounds.
4. **Concatenating string numbers without conversion**: `"Total: " + 42` fails. Use `"Total: " + str(42)`.
5. **Relying on implicit conversion**: Python rarely converts automatically. Always cast explicitly for clarity.

## Hands-On Walkthrough

Let's build a small program that demonstrates type conversion using a real scenario — a user's age input (from a file, simulated here):

```python
# Simulating data we read from somewhere
age_string = "25"
height_string = "1.75"
has_license = "True"

# Convert to proper types
age = int(age_string)
height = float(height_string)
license_bool = bool(has_license)

print("Age:", age, type(age))
print("Height:", height, type(height))
print("Has license:", license_bool, type(license_bool))

# Now we can do math
print("Next year you will be:", age + 1)

# String concatenation with str()
print("You are " + str(age) + " years old.")
```

Expected output:
```
Age: 25 <class 'int'>
Height: 1.75 <class 'float'>
Has license: True <class 'bool'>
Next year you will be: 26
You are 25 years old.
```

Now let's experiment with truncation vs rounding:

```python
print("int(3.99) =", int(3.99))  # 3, truncation
print("int(3.14) =", int(3.14))  # 3, truncation
print("int(-2.7) =", int(-2.7))  # -2, truncates toward zero
print("round(3.99) =", round(3.99))  # 4.0, rounding
```

## Key Takeaways

- Implicit conversion happens automatically in safe directions (int → float, int → bool).
- Explicit conversion uses `int()`, `float()`, `str()`, `bool()`.
- `int()` truncates toward zero — it does not round.
- `bool("")` and `bool(0)` are `False`; all other values are generally `True`.
- `int("3.14")` raises `ValueError` — convert to `float()` first.
- Strings with numbers can be converted if they contain valid numeric characters.
- Always convert input data explicitly before doing operations.
- Use `str()` to combine non-string values with strings using `+`.

## Further Reading
- [Built-in Functions: int(), float(), str(), bool() (docs.python.org)](https://docs.python.org/3/library/functions.html)
- [Truth Value Testing (docs.python.org)](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

## Next Module
Learn how to get input from users in [Module 005: Basic Input and Output](../module-005-basic-input-and-output/README.md).
