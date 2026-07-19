# Module 037: Decorators: Basics

> **Phase:** 4. Functions  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)
- Module 033 (Scope and Namespaces)
- Module 036 (Higher-Order Functions)

## Learning Objectives
By the end of this module, you will be able to:
- Understand functions as first-class objects
- Create nested functions (closures)
- Use the `@decorator` syntax
- Write simple decorators (timing, logging)
- Use `functools.wraps` to preserve metadata
- Apply multiple decorators

## Why This Matters
Decorators are one of Python's most powerful features. They let you modify or enhance functions without changing their code — perfect for logging, access control, caching, and timing.

## Concept Explanation

### Functions as First-Class Objects (Review)

```python
def greet(name):
    return f"Hello, {name}!"

f = greet  # assign to variable
print(f("Alice"))
```

### Nested Functions (Closures)

A function defined inside another can access the outer function's variables:

```python
def outer(msg):
    def inner(name):
        return f"{msg}, {name}!"
    return inner

hello = outer("Hello")
print(hello("Bob"))
```

### Decorator Syntax

A decorator is a function that takes another function and extends it:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")
```

### Simple Timing Decorator

```python
import time

def timer(func):
    """Measure and print the execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
```

### `functools.wraps`

Without `@wraps`, the decorated function loses its original name and docstring:

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring."""
        return func(*args, **kwargs)
    return wrapper
```

### Diagram: Decorator Wrapping

```
Original function:         greet("Alice") → "Hello, Alice!"

After @logger:             logger(greet) → wrapper("Alice")
                             1. log "calling greet"
                             2. greet("Alice") → "Hello, Alice!"
                             3. log "finished greet"
                             4. return result
```

### Multiple Decorators

```python
@decorator1
@decorator2
def func():
    pass
# Equivalent to: func = decorator1(decorator2(func))
```

## Common Pitfalls

1. **Forgetting `@wraps`**: Breaks introspection (help(), __name__, __doc__).
2. **Forgetting `*args, **kwargs`**: Decorator won't work with arbitrary arguments.
3. **Not returning the wrapper**: The decorator must return a function.
4. **Mutable closure variables**: Can cause surprising behavior.

## Hands-On Walkthrough

1. Write a decorator `@logger` that prints "Calling func_name" before a function runs.
2. Apply it to a simple function and test.
3. Add `@wraps` and verify `__name__` is preserved.
4. Stack two decorators: `@timer` and `@logger`.

## Key Takeaways

- Decorators wrap functions to add behavior without modifying the original.
- `@decorator` is syntactic sugar for `func = decorator(func)`.
- Always use `@wraps` to preserve function metadata.
- Decorators stack bottom-up (closest to function applied first).
- Use `*args, **kwargs` for maximum flexibility.

## Further Reading
- [Python docs: Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Real Python: Primer on Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python docs: functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)

## Next Module
Continue to **Module 038: Generators and yield**.
