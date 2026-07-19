# Module 011: Booleans and Truthiness

> **Phase:** 2. Control Flow & Data | **Estimated time:** 1.5 hours | **Milestone Project:** No

## Prerequisites
- [Module 001: Print & Comments](../module-001-print-and-comments/README.md)
- [Module 002: Variables & Data Types](../module-002-variables-and-data-types/README.md)
- [Module 005: Type Conversion](../module-005-type-conversion/README.md)
- [Module 007: Operators](../module-007-operators/README.md)

## Learning Objectives
- Understand the Boolean type (`bool`) and its two values: `True` and `False`
- Use the `bool()` function to convert other values to Booleans
- Identify which Python values are truthy vs falsy
- Combine Boolean values with `and`, `or`, and `not`
- Explain short-circuit evaluation behavior

## Why This Matters
Booleans are the foundation of decision-making in code. Every conditional check, loop condition, and filter ultimately reduces to a Boolean. Understanding truthiness — what Python considers "true" or "false" — helps you write cleaner conditions and avoid subtle bugs.

## Concept Explanation

### The `bool` Type

Python has a dedicated Boolean type with exactly two values:

```python
is_active = True
is_finished = False
```

`True` and `False` are the only two `bool` values. They are technically a subclass of integers — `True == 1` and `False == 0` — but you should never rely on that in practice.

```python
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>
print(True + 2)     # 3   (but don't do this!)
```

### The `bool()` Function

You can convert any value to a Boolean using `bool()`:

```python
print(bool(1))      # True
print(bool(0))      # False
print(bool("hi"))   # True
print(bool(""))     # False
print(bool([]))     # False
```

### Truthy and Falsy Values

Python considers the following values **falsy** — they convert to `False`:

| Falsy Value        | Reason                  |
|--------------------|-------------------------|
| `0`, `0.0`, `0j`   | Zero numeric values     |
| `""` (empty string)| No characters           |
| `[]` (empty list)  | No elements             |
| `None`             | Absence of a value      |
| `False`            | The Boolean false       |
| `()` (empty tuple) | No elements             |
| `{}` (empty dict)  | No key/value pairs      |

Everything else is **truthy**:

```python
print(bool("hello"))   # True (non-empty string)
print(bool(42))        # True (non-zero number)
print(bool(-1))        # True (negative numbers are truthy too)
print(bool([1, 2]))    # True (non-empty list)
print(bool("False"))   # True! The *string* "False" is non-empty
```

> **Key insight:** The string `"False"` is truthy because it's a non-empty string. Only the *empty string* `""` is falsy.

### Boolean Operators

#### `not` — Logical NOT

Flips `True` to `False` and vice versa:

```python
print(not True)   # False
print(not False)  # True
print(not 0)      # True   (0 is falsy, so not 0 is True)
print(not 42)     # False  (42 is truthy, so not 42 is False)
```

#### `and` — Logical AND

Returns `True` only if **both** sides are truthy:

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

With non-Boolean values, `and` returns the first falsy value, or the last value if all are truthy:

```python
print(0 and 42)      # 0    (0 is falsy, short-circuits)
print(3 and 7)       # 7    (both truthy, returns last)
print("" and "hi")   # ''   (empty string is falsy)
```

#### `or` — Logical OR

Returns `True` if **at least one** side is truthy:

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

With non-Boolean values, `or` returns the first truthy value, or the last value if all are falsy:

```python
print(0 or 42)      # 42   (0 is falsy, 42 is truthy)
print(3 or 7)       # 3    (3 is truthy, short-circuits)
print("" or "hi")   # 'hi' ("" is falsy, "hi" is truthy)
print(0 or "")      # ''   (both falsy, returns last)
```

### Short-Circuit Evaluation

Python evaluates `and` and `or` lazily — it stops as soon as the result is determined.

- For `A and B`: if `A` is falsy, Python doesn't evaluate `B` at all
- For `A or B`: if `A` is truthy, Python doesn't evaluate `B`

This matters when the right-side expression has side effects (like user input or calculations):

```python
def get_value():
    print("get_value() was called!")
    return 42

result = False and get_value()  # get_value() is NEVER called
print(result)                   # False

result = True or get_value()    # get_value() is NEVER called
print(result)                   # True
```

## Common Pitfalls

1. **Using `== True` unnecessarily** — Instead of `if x == True:`, just write `if x:`. Python's truthiness already handles it.

2. **Forgetting `"False"` is truthy** — The string `"False"` is not empty, so `bool("False")` is `True`. Only `""` is falsy.

3. **Overlooking that `0` and `0.0` are falsy** — Zero values convert to `False`, which is usually what you want, but it can surprise you when checking if a number variable is set.

4. **Confusing `and`/`or` return values** — These operators don't always return `True` or `False`. They return one of the operands based on truthiness.

5. **Assuming `and` evaluates both sides** — Short-circuit means the right side may never run. Don't put critical code there unless you're sure it will execute.

```python
# Pitfall example: Division by zero risk
x = 0
# This would crash: result = x != 0 and 10 / x
# This is safe because short-circuit prevents division when x == 0
result = x != 0 and 10 / x  # x != 0 is False, so 10/x never runs
print(result)                # False
```

## Hands-On Walkthrough

Let's build a simple login-like check using truthiness:

```python
# Simulate a user lookup
username = input("Enter username: ")  # Assume user types "alice"
password = input("Enter password: ")  # Assume user types "" (empty)

# Truthiness check: empty password is falsy
if not password:
    print("Password cannot be empty!")  # This runs
else:
    print("Checking credentials...")

# Real-world pattern: check if both fields are non-empty
if username and password:
    print(f"Logging in as {username}")
else:
    print("Both fields are required.")
```

Now let's use `bool()` to see what's truthy:

```python
test_values = [0, 1, 0.0, 3.14, "", "hello", None, [], [1, 2]]
for val in test_values:
    print(f"bool({val!r:8}) -> {bool(val)}")
# Output:
# bool(0       ) -> False
# bool(1       ) -> True
# bool(0.0     ) -> False
# bool(3.14    ) -> True
# bool(''      ) -> False
# bool('hello' ) -> True
# bool(None    ) -> False
# bool([]      ) -> False
# bool([1, 2]  ) -> True
```

## Key Takeaways

- `bool` has exactly two values: `True` and `False`
- Falsy values: `0`, `0.0`, `""`, `None`, `[]`, `()`, `{}`, and `False` itself
- Everything else is truthy — including negative numbers and the string `"False"`
- `not` flips truthiness; `and` returns the first falsy or last truthy; `or` returns the first truthy or last falsy
- Python short-circuits: `and` stops on the first falsy, `or` stops on the first truthy
- Use `bool(x)` to check the truthiness of any value explicitly
- Prefer implicit truthiness checks (`if x:`) over `if x == True:` or `if len(x) > 0:`
- Short-circuit evaluation can prevent errors like division by zero or calling methods on `None`

## Further Reading
- [Python docs: Built-in Types — Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python docs: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [PEP 285 — Adding a bool type](https://peps.python.org/pep-0285/)
- [Real Python: Python Booleans](https://realpython.com/python-boolean/)

## Next Module
[Module 012: Conditional Statements (if / elif / else)](../module-012-conditional-statements/README.md) — Learn how to make decisions in your code using `if` statements, branching with `elif`, and fallback with `else`.
