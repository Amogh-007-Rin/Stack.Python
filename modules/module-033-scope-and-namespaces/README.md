# Module 033: Scope and Namespaces (the LEGB Rule)

> **Phase:** 4. Functions  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)
- Module 032 (Function Arguments)

## Learning Objectives
By the end of this module, you will be able to:
- Explain the LEGB rule (Local, Enclosing, Global, Built-in)
- Use the `global` keyword to modify global variables
- Use the `nonlocal` keyword to modify enclosing scope variables
- Visualize Python's namespace hierarchy
- Trace how Python looks up variable names
- Understand variable shadowing

## Why This Matters
Scope rules determine which variables your code can see. Misunderstanding scope leads to confusing bugs like "why doesn't my function see that variable?" or "why did my variable change globally?"

## Concept Explanation

### The LEGB Rule

Python looks up variable names in this order:

```
L — Local        (inside the current function)
E — Enclosing    (any enclosing function, e.g., outer function)
G — Global       (top-level of the module)
B — Built-in     (Python's built-in names like print, len)
```

### Diagram: LEGB Lookup

```
┌─────────────────────────────────────┐
│           Built-in                  │
│   print, len, range, int, ...       │
│  ┌───────────────────────────────┐  │
│  │         Global                │  │
│  │   x = 10, PI = 3.14          │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │   Enclosing (outer)     │  │  │
│  │  │   y = 20                │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │    Local (inner)  │  │  │  │
│  │  │  │    z = 30         │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘

Lookup:  inner → outer → global → built-in
```

### Local Scope

Variables defined inside a function are local:

```python
def my_func():
    x = 5  # local — not accessible outside
    print(x)
```

### Global Scope

Variables defined at the module top level are global:

```python
y = 10  # global

def show_y():
    print(y)  # can read global

show_y()  # 10
```

### The `global` Keyword

To *modify* a global variable inside a function, use `global`:

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

### The `nonlocal` Keyword

To modify a variable in an enclosing (outer) scope, use `nonlocal`:

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
    inner()
    print(x)  # 15
```

### Shadowing

When a local variable has the same name as a global one, it "shadows" it:

```python
x = 100

def shadow():
    x = 200  # shadows the global x
    print(x)  # 200

shadow()
print(x)  # 100 — global unchanged
```

## Common Pitfalls

1. **Trying to modify a global without `global`**: Creates a new local instead (or raises UnboundLocalError).
2. **Forgetting `nonlocal` in nested functions**: Creates a new local instead of modifying the enclosing variable.
3. **Accidental shadowing**: A local variable hides a global one with the same name.
4. **Too many globals**: Makes code hard to reason about — prefer passing parameters.

## Hands-On Walkthrough

1. Create a global variable `count = 0`.
2. Write a function `increment()` that uses `global` to add 1.
3. Write an outer function with an inner function that uses `nonlocal`.
4. Experiment with shadowing — create a local variable with the same name as a global.

## Key Takeaways

- LEGB: Local → Enclosing → Global → Built-in.
- `global` lets you modify module-level variables inside a function.
- `nonlocal` lets you modify enclosing function variables.
- Shadowing is when a local name hides an outer name.
- Minimize global variables for cleaner code.

## Further Reading
- [Python docs: Naming and Binding](https://docs.python.org/3/reference/executionmodel.html#naming-and-binding)
- [Real Python: Python Scope & the LEGB Rule](https://realpython.com/python-scope-legb-rule/)

## Next Module
Continue to **Module 034: Lambda Functions**.
