# Module 043: Constructors (`__init__`) and self

> **Phase:** 5. OOP  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 042 (Attributes and Methods)

## Learning Objectives
By the end of this module, you will be able to:
- Explain what a constructor is and when it runs
- Write parameterized constructors
- Use default values in `__init__`
- Understand what happens when a class has no `__init__`
- Explain why Python passes `self` implicitly

## Why This Matters
The constructor is where objects come to life. Understanding `__init__` and `self` is essential to designing classes that are convenient and safe to use.

## Concept Explanation

### `__init__` in Depth

`__init__` is called **automatically** right after the object is created. Its job is to set the initial state.

```python
class Book:
    """Represent a book."""

    def __init__(self, title, author, pages):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1  # default, not passed in
```

The object lifecycle:

```
1. __new__()     → allocates memory (rarely overridden)
2. __init__()    → initializes the object
3. ... use the object ...
4. __del__()     → cleanup (rarely overridden, unreliable)
```

### Parameterized Constructors

Pass arguments to customize each instance:

```python
class Point:
    """Represent a 2D point."""

    def __init__(self, x, y):
        """Initialize point with coordinates."""
        self.x = x
        self.y = y

p1 = Point(3, 4)
p2 = Point(-1, 2)
```

### Default Values in `__init__`

Provide sensible defaults:

```python
class Timer:
    """A simple countdown timer."""

    def __init__(self, duration=10, unit="seconds"):
        """Initialize timer with optional defaults."""
        self.duration = duration
        self.unit = unit
        self.remaining = duration

t1 = Timer()           # duration=10, unit="seconds"
t2 = Timer(30)         # duration=30, unit="seconds"
t3 = Timer(60, "minutes")  # duration=60, unit="minutes"
```

⚠️ **Mutable default trap**: Never use mutable objects (lists, dicts) as default arguments.

```python
class BadExample:
    def __init__(self, items=[]):  # BAD: shared list!
        self.items = items

class GoodExample:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

### What Happens Without `__init__`?

If you don't define `__init__`, Python uses the default from `object`. The instance is still created — you can add attributes later, but the class doesn't guarantee they exist.

```python
class Empty:
    pass

obj = Empty()
obj.name = "Added later"  # works, but fragile
```

### Python's Implicit `self`

When you call `instance.method(arg1)`, Python translates it to `Class.method(instance, arg1)`. That's why `self` is always the first parameter.

```python
class Demo:
    def show(self, msg):
        print(f"{self}: {msg}")

d = Demo()
d.show("hello")           # <__main__.Demo object at 0x...>: hello
Demo.show(d, "hello")     # equivalent explicit call
```

## Common Pitfalls

1. **Mutable default arguments**: Use `None` and initialize inside the method.
2. **Returning from `__init__`**: `__init__` must return `None` — returning anything else raises `TypeError`.
3. **Confusing `__init__` with `__new__`**: `__init__` initializes; `__new__` creates. You almost never need `__new__`.
4. **Calling the constructor wrong**: `obj = MyClass()` not `obj = MyClass.__init__()`.

## Hands-On Walkthrough

1. Write a `class Rectangle` with `__init__(self, width, height)`.
2. Add a method `area()` that returns `width * height`.
3. Create a class `Config` with default values for `host="localhost"` and `port=8080`.
4. Create instances with and without arguments and verify defaults.
5. Demonstrate the mutable default trap and fix it.

## Key Takeaways

- `__init__` runs automatically when an object is created.  
- Parameterized constructors let you customize each instance.  
- Default values make constructors flexible but avoid mutable defaults.  
- Without `__init__`, the class inherits `object.__init__`.  
- Python passes `self` implicitly — it's the instance itself.

## Further Reading

- [Python docs: __init__](https://docs.python.org/3/reference/datamodel.html#object.__init__)
- [Python docs: Mutable default argument](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)

## Next Module

Continue to **Module 044: Class Variables vs Instance Variables**.
