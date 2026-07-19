# Module 041: Introduction to OOP: Classes and Objects

> **Phase:** 5. OOP  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Modules 031-040 (all function concepts, generators, iterators)

## Learning Objectives
By the end of this module, you will be able to:
- Explain what OOP is and how it differs from procedural programming
- Define a class as a blueprint and an object as an instance
- Write a simple class definition using `class ClassName:`
- Create instances of a class
- Describe the purpose of `__init__` and `self`
- Understand why OOP helps organize code

## Why This Matters
Object-Oriented Programming is a paradigm shift. Instead of writing functions that operate on data, you bundle data and behavior together into objects. This makes code more modular, reusable, and easier to reason about as programs grow.

## Concept Explanation

### What is OOP?

Procedural programming organizes code around **functions** that operate on **data**. OOP organizes code around **objects** that contain both data and behavior.

```
Procedural:   data → function → result
Object:       object.data + object.method() → result
```

### Class as Blueprint, Object as Instance

A **class** is a blueprint. An **object** (or instance) is a concrete thing built from that blueprint.

```
┌─────────────────────┐
│     Class           │   ← Blueprint / Template
│  (Dog)              │
│                     │
│  Attributes:        │
│    - name           │
│    - breed          │
│                     │
│  Methods:           │
│    - bark()         │
│    - fetch()        │
└─────────────────────┘
          │
          │  instantiate
          ▼
┌─────────────────────┐   ┌─────────────────────┐
│  Object (instance)   │   │  Object (instance)   │
│  fido = Dog()        │   │  spot = Dog()        │
│  fido.name = "Fido"  │   │  spot.name = "Spot"  │
│  fido.breed = "Lab"  │   │  spot.breed = "Pug"  │
└─────────────────────┘   └─────────────────────┘
```

### Defining a Simple Class

```python
class Dog:
    """A simple Dog class."""

    def __init__(self, name):
        """Initialize dog with a name."""
        self.name = name

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says Woof!")


fido = Dog("Fido")
fido.bark()  # Fido says Woof!
```

### `__init__` and `self`

- `__init__` is the **constructor** method — it runs automatically when you create an instance.
- `self` refers to the **current instance**. It's how methods access the instance's own data.

### Why OOP Matters

- **Encapsulation**: bundle data + methods together
- **Reusability**: define once, create many instances
- **Organization**: group related code logically
- **Modeling**: match real-world entities directly in code

## Common Pitfalls

1. **Forgetting `self`**: All instance methods must have `self` as the first parameter.
2. **Calling class methods without instantiation**: You must create an instance first.
3. **Thinking `self` is a keyword**: It's a convention — you could name it anything, but never do.
4. **Confusing class vs instance**: The class is the blueprint; the instance is the actual object.

## Hands-On Walkthrough

1. Define a `class Car` with an `__init__` that takes `make`, `model`, and `year`.
2. Add a method `describe()` that prints "This is a [year] [make] [model]".
3. Create two Car instances with different values.
4. Create a class without `__init__` and add attributes manually — observe how it works.

## Key Takeaways

- OOP bundles data and behavior into objects.  
- A **class** is a blueprint; an **object** is an instance of that blueprint.  
- `__init__` initializes new objects; `self` references the current instance.  
- OOP helps organize and scale code as projects grow.

## Further Reading

- [Python docs: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)

## Next Module

Continue to **Module 042: Attributes and Methods**.
