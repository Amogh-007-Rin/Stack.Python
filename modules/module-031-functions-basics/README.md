# Module 031: Functions: Basics (def, return, Parameters)

> **Phase:** 4. Functions  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Modules 000-030 (all fundamentals)

## Learning Objectives
By the end of this module, you will be able to:
- Define functions using the `def` keyword
- Use the `return` statement to send values back to the caller
- Distinguish between parameters and arguments
- Call functions with positional arguments
- Understand basic function scope (local vs global)
- Write Google-style docstrings for functions
- Follow Python naming conventions for functions

## Why This Matters
Functions are the building blocks of any non-trivial program. Instead of writing the same code over and over, you wrap it in a function and call it by name. Functions make code reusable, testable, and readable.

## Concept Explanation

### Defining a Function

Use the `def` keyword, a name, parentheses, and a colon:

```python
def greet():
    """Print a greeting message."""
    print("Hello, world!")
```

Call it by using the name followed by parentheses:

```python
greet()  # Hello, world!
```

### The `return` Statement

Functions can send a value back to the caller with `return`:

```python
def add_one(x):
    """Add one to x and return the result.

    Args:
        x: The number to increment

    Returns:
        x + 1
    """
    return x + 1

result = add_one(5)  # result = 6
```

Without `return`, a function returns `None` implicitly.

### Parameters vs Arguments

- **Parameter**: The variable listed in the function definition.
- **Argument**: The value you pass when calling the function.

```python
def square(n):       # n is a parameter
    return n * n

print(square(4))     # 4 is an argument
```

### Function Scope Intro

Variables created inside a function are **local** — they don't exist outside:

```python
def spam():
    eggs = 10  # local variable
    print(eggs)

spam()         # 10
print(eggs)    # NameError!
```

### Docstrings (Google Style)

```python
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the product.

    Args:
        a: First factor
        b: Second factor

    Returns:
        Product of a and b
    """
    return a * b
```

### ASCII Diagram: Function Flow

```
┌─────────┐     Call greet()     ┌──────────────┐
│  Caller  │ ──────────────────▶  │  greet()     │
│          │                     │              │
│          │ ◀────────────────── │  print(...)  │
└─────────┘     return None      │  return None │
                                 └──────────────┘
```

### Function Naming Conventions

- Use `snake_case` for function names
- Use descriptive verbs: `calculate_total`, `get_user_name`
- Avoid abbreviations: `get_user` not `get_usr`
- Follow PEP 8 — lowercase with underscores

## Common Pitfalls

1. **Forgetting parentheses** when calling: `greet` vs `greet()` — the first refers to the function object, not the result.
2. **Forgetting `return`**: Without it, the function returns `None`.
3. **Modifying global variables inside a function** without `global` (covered in Module 033).
4. **Printing instead of returning**: Use `return` so callers can use the result.

## Hands-On Walkthrough

1. Define a simple function `greet(name)` that returns a string.
2. Call it with different names.
3. Define `add(a, b)` that returns the sum.
4. Experiment with local variables — try to access one outside the function.

## Key Takeaways

- `def` defines a function; `return` sends a result back.
- Parameters are placeholders; arguments are actual values.
- Variables inside functions are local by default.
- Use Google-style docstrings to document every function.
- Name functions with `snake_case` and descriptive verbs.

## Further Reading
- [Python docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide — Docstrings](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)

## Next Module
Continue to **Module 032: Function Arguments (Default, Keyword, *args, **kwargs)**.
