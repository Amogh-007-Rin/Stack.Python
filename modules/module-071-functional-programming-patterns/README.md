# Module 071: Functional Programming Patterns in Python

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2 hours

## Learning Objectives

- Understand functional programming concepts: pure functions, no side effects, immutability
- Apply map, filter, and reduce for data transformations
- Create partial functions with functools.partial
- Compose functions to build complex operations
- Use the operator module for cleaner code
- Leverage functools module utilities

## Topics Covered

1. Pure functions and side effect avoidance
2. Immutability principles
3. map(), filter(), and reduce() in depth
4. functools.partial for partial application
5. Function composition techniques
6. operator module (add, itemgetter, attrgetter)
7. functools.lru_cache, functools.singledispatch

## Prerequisites

Modules 000-070 covering basics, data structures, functions, OOP, error handling, file I/O, JSON, context managers, modules/packages, venv/pip, stdlib, regex, dates, and logging.

## Key Concepts

```python
# Pure function: no side effects, same input -> same output
def add_one(x: int) -> int:
    return x + 1

# map with lambda
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))

# Partial function
from functools import partial

def power(base: int, exp: int) -> int:
    return base ** exp

square = partial(power, exp=2)
```

## Resources

- Python docs: functools
- Python docs: operator
- "Functional Programming HOWTO" in Python docs
