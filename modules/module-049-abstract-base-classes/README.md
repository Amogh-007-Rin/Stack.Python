# Module 049: Abstract Base Classes and Interfaces

> **Phase:** 5. OOP  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 048 (Dunder Methods)

## Learning Objectives
By the end of this module, you will be able to:
- Use the `abc` module to create abstract base classes
- Define abstract methods with `@abstractmethod`
- Explain why ABCs exist (enforcing interface contracts)
- Create concrete subclasses that implement abstract methods
- Define abstract properties
- Register virtual subclasses with `.register()`

## Why This Matters
Abstract Base Classes let you define **interfaces** — contracts that subclasses must fulfill. This ensures consistency across implementations and catches missing methods early.

## Concept Explanation

### The `abc` Module

`abc` stands for Abstract Base Classes. Use `ABC` as a parent and `@abstractmethod` to mark required methods:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area. Must be implemented by subclasses."""
        ...

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter. Must be implemented."""
        ...
```

### Concrete Subclasses

Any class that inherits from an ABC must implement all abstract methods, or it cannot be instantiated:

```python
class Circle(Shape):
    """Concrete circle class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(circle.area())        # 78.53975
print(circle.perimeter())   # 31.4159
```

```python
# This would raise TypeError:
# class Incomplete(Shape):
#     pass
# obj = Incomplete()  # Can't instantiate abstract class
```

### Why ABCs Exist

1. **Enforce contracts**: Subclasses *must* implement specified methods.
2. **Documentation**: Clearly states what methods are expected.
3. **Early error detection**: Fails at instantiation time, not at method call time.
4. **Polymorphism**: You can write functions that accept any `Shape`.

```python
def print_shape_info(shape: Shape):
    """Print area and perimeter of any Shape."""
    if not isinstance(shape, Shape):
        raise TypeError("Must be a Shape")
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
```

### Abstract Properties

You can also require properties in subclasses:

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    """Abstract employee class."""

    @property
    @abstractmethod
    def role(self):
        """Role must be defined as a property."""
        ...

    @abstractmethod
    def calculate_pay(self):
        """Calculate employee pay."""
        ...

class Manager(Employee):
    """Concrete manager class."""

    @property
    def role(self):
        return "Manager"

    def calculate_pay(self):
        return 80000

m = Manager()
print(m.role)  # Manager
```

### Registering Virtual Subclasses

`register()` lets you mark a class as a subclass without inheritance. This is useful for integration with third-party code.

```python
from abc import ABC

class Iterable(ABC):
    """Abstract iterable."""
    @abstractmethod
    def __iter__(self):
        ...

# Register an existing class
Iterable.register(list)
Iterable.register(tuple)

print(isinstance([1, 2, 3], Iterable))  # True
```

### ABCs in the Standard Library

Python uses ABCs extensively in `collections.abc`:

| ABC | Requires | Used by |
|-----|----------|---------|
| `Iterable` | `__iter__` | `for` loops |
| `Sequence` | `__getitem__`, `__len__` | Indexable collections |
| `Mapping` | `__getitem__`, `__len__`, `__iter__` | Dict-like objects |
| `Set` | `__contains__`, `__iter__`, `__len__` | Set-like objects |
| `Callable` | `__call__` | Callable objects |

## Common Pitfalls

1. **Forgetting `@abstractmethod`**: Without it, the method is just a regular method that can be left unimplemented.
2. **Instantiating an ABC**: Direct instantiation raises `TypeError`.
3. **Not implementing all abstract methods**: The class becomes abstract too and cannot be instantiated.
4. **Overusing ABCs**: For simple interfaces, duck typing may be sufficient.

## Hands-On Walkthrough

1. Create an ABC `Media` with abstract methods `play()` and `stop()`.
2. Implement `Audio(Media)` and `Video(Media)` with concrete versions.
3. Write a function that accepts any `Media` and calls `play()`.
4. Register a third-party class as a virtual subclass.
5. Use `collections.abc.Sequence` to check if a custom class behaves like a sequence.

## Key Takeaways

- ABCs define interfaces that subclasses must implement.  
- `@abstractmethod` marks methods that must be overridden.  
- Concrete subclasses must implement all abstract methods to be instantiable.  
- Abstract properties enforce property contracts.  
- `.register()` marks virtual subclasses without inheritance.  
- `collections.abc` provides ready-made ABCs for common protocols.

## Further Reading

- [Python docs: abc module](https://docs.python.org/3/library/abc.html)
- [Python docs: collections.abc](https://docs.python.org/3/library/collections.abc.html)
- [Real Python: Abstract Base Classes](https://realpython.com/python-abstract-base-classes/)

## Next Module

Continue to **Module 050: Milestone Project: Library/Inventory Management System**.
