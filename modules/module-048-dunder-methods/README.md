# Module 048: Dunder/Magic Methods (`__str__`, `__repr__`, `__eq__`)

> **Phase:** 5. OOP  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 047 (Polymorphism)

## Learning Objectives
By the end of this module, you will be able to:
- Differentiate `__str__` vs `__repr__`
- Implement `__eq__` and understand its relationship with `__hash__`
- Implement `__len__`, `__getitem__`, and `__contains__`
- Use `__call__` to make objects callable
- Use `__bool__` to define truthiness
- Make objects work with built-in functions

## Why This Matters
Dunder methods let your custom objects integrate seamlessly with Python's built-in functions and operators. They're the key to writing objects that feel "Pythonic."

## Concept Explanation

### `__str__` vs `__repr__`

- `__repr__` = unambiguous representation (for developers, ideally recreates the object)
- `__str__` = readable representation (for end users)

```python
class Point:
    """A 2D point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return unambiguous representation."""
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        """Return readable representation."""
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))   # Point(3, 4)
print(str(p))    # (3, 4)
print(p)         # (3, 4)  — calls str()
```

### `__eq__` and `__hash__`

`__eq__` defines equality. Python's default uses identity (`is`). When you define `__eq__`, you should also define `__hash__` if you want objects usable in sets/dict keys.

```python
class Book:
    """A book with ISBN-based equality."""

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def __repr__(self):
        return f"Book({self.title!r}, {self.isbn!r})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)

b1 = Book("Python 101", "123-456")
b2 = Book("Python 101", "123-456")
b3 = Book("Python 201", "789-012")

print(b1 == b2)      # True  (same ISBN)
print(b1 == b3)      # False
print(len({b1, b2, b3}))  # 2  (b1 and b2 hash same)
```

### `__len__`, `__getitem__`, `__contains__`

Make your objects work with `len()`, indexing, and `in`:

```python
class Playlist:
    """A playlist that supports common collection operations."""

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __contains__(self, song):
        return song in self.songs

pl = Playlist("Favorites")
pl.add("Song A")
pl.add("Song B")
print(len(pl))          # 2
print(pl[0])            # Song A
print("Song A" in pl)   # True
```

### `__call__`

Make an instance callable like a function:

```python
class Multiplier:
    """A callable multiplier."""

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

### `__bool__`

Define truthiness for your objects:

```python
class Account:
    """Account with custom truthiness."""

    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0

acc1 = Account(100)
acc2 = Account(0)

print(bool(acc1))  # True
print(bool(acc2))  # False

if acc1:
    print("Positive balance!")  # runs
```

### `str()` vs `repr()` Usage

| Function | Calls | Should return | Used by |
|----------|-------|---------------|---------|
| `str()` | `__str__` | Readable | `print()`, `f"{obj}"` |
| `repr()` | `__repr__` | Unambiguous | Debugging, logs, REPL |
| `__str__` falls back to `__repr__` | | | |

## Common Pitfalls

1. **Defining `__eq__` without `__hash__`**: Sets mutable objects' `__hash__` to `None`.
2. **Making `__repr__` return a string that doesn't recreate the object**: `repr()` should ideally be copy-pasteable.
3. **Forgetting `return NotImplemented` in `__eq__`**: Allows Python to try the other side's `__eq__`.
4. **Thinking `__str__` is always needed**: If only one is defined, `__str__` falls back to `__repr__`.

## Hands-On Walkthrough

1. Create a `class Time` with hours and minutes. Implement `__repr__`, `__str__`, `__eq__`, `__hash__`.
2. Add `__add__` to support `time1 + time2`.
3. Create a `class Deck` that implements `__len__`, `__getitem__`, `__contains__`.
4. Make a `class Greeter` callable with `__call__`.

## Key Takeaways

- `__repr__` is for developers (unambiguous); `__str__` is for users (readable).  
- Define `__eq__` and `__hash__` together for sensible equality and hashing.  
- `__len__`, `__getitem__`, and `__contains__` make objects collection-like.  
- `__call__` makes instances callable; `__bool__` defines truthiness.  
- Dunder methods integrate custom objects with Python's built-in functions.

## Further Reading

- [Python docs: Special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Real Python: Magic Methods](https://realpython.com/python-magic-methods/)

## Next Module

Continue to **Module 049: Abstract Base Classes and Interfaces**.
