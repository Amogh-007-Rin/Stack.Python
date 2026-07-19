# Module 032: Function Arguments (Default, Keyword, *args, **kwargs)

> **Phase:** 4. Functions  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)

## Learning Objectives
By the end of this module, you will be able to:
- Distinguish between positional and keyword arguments
- Set default parameter values
- Use `*args` for variable-length positional arguments
- Use `**kwargs` for variable-length keyword arguments
- Follow argument ordering rules (positional, default, *args, **kwargs)
- Unpack arguments with `*` and `**` when calling functions

## Why This Matters
Functions need to be flexible. Default arguments let you make parameters optional. `*args` and `**kwargs` let you write functions that accept any number of inputs — essential for wrappers, decorators, and library code.

## Concept Explanation

### Positional vs Keyword Arguments

**Positional arguments** are matched by position:

```python
def power(base, exp):
    return base ** exp

print(power(2, 3))  # 8 — 2 is base, 3 is exp
```

**Keyword arguments** are matched by name:

```python
print(power(exp=3, base=2))  # 8 — order does not matter
```

### Default Parameter Values

Make a parameter optional by giving it a default:

```python
def greet(name, greeting="Hello"):
    """Greet someone with an optional greeting.

    Args:
        name: The person's name
        greeting: The greeting word (default "Hello")
    """
    print(f"{greeting}, {name}!")

greet("Alice")           # Hello, Alice!
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!
```

### `*args` — Variable Positional Arguments

The `*args` parameter captures extra positional arguments into a tuple:

```python
def sum_all(*args):
    """Sum any number of arguments.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        Sum of all arguments
    """
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
print(sum_all(5, 10))       # 15
```

### `**kwargs` — Variable Keyword Arguments

The `**kwargs` parameter captures extra keyword arguments into a dict:

```python
def print_info(**kwargs):
    """Print keyword arguments as key-value pairs.

    Args:
        **kwargs: Arbitrary keyword arguments
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

### Argument Ordering Rules

The correct order is:

```
def func(positional, default=x, *args, **kwargs):
```

1. **Positional parameters** (no default)
2. **Default parameters**
3. **`*args`** (variable positional)
4. **`**kwargs`** (variable keyword)

### Unpacking with `*` and `**` When Calling

You can unpack iterables into arguments with `*`:

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))  # 6 — unpacks list into a=1, b=2, c=3
```

You can unpack dicts into keyword arguments with `**`:

```python
def create_user(name, age, email):
    print(f"{name}, {age}, {email}")

data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
create_user(**data)
```

## Common Pitfalls

1. **Mutable default arguments**: Defaults are evaluated once at definition time, not each call.
2. **Mixing positional and keyword incorrectly**: Positional args must come before keyword args in a call.
3. **Forgetting `*args` is a tuple, `**kwargs` is a dict**: You can iterate over them but not modify.
4. **Putting `*args` before default parameters**: This causes the default to never be used positionally.

## Hands-On Walkthrough

1. Write a function `greet(name, greeting="Hello")` and call it with and without the greeting.
2. Add a function `multiply(*args)` that returns the product of all arguments.
3. Add a function `build_profile(name, age, **kwargs)` that prints a profile.
4. Experiment with unpacking: pass a list to `*args` and a dict to `**kwargs`.

## Key Takeaways

- Positional arguments match by position; keyword arguments match by name.
- Default parameters make arguments optional.
- `*args` captures extra positional args as a tuple; `**kwargs` captures extra keyword args as a dict.
- Order: positional → default → `*args` → `**kwargs`.
- Use `*` and `**` to unpack sequences/dicts when calling functions.
- Avoid mutable default arguments.

## Further Reading
- [Python docs: More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Python docs: Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python docs: Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)

## Next Module
Continue to **Module 033: Scope and Namespaces (the LEGB Rule)**.
