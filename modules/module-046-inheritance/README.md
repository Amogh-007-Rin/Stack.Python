# Module 046: Inheritance

> **Phase:** 5. OOP  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 045 (Encapsulation)

## Learning Objectives
By the end of this module, you will be able to:
- Create a child class that inherits from a parent class
- Override methods in a subclass
- Use `super()` to call parent methods
- Use `isinstance()` and `issubclass()` for type checking
- Explain Method Resolution Order (MRO)
- Inherit from built-in types

## Why This Matters
Inheritance lets you define a general class and then create specialized versions. It's one of the most powerful mechanisms for code reuse and building hierarchical relationships.

## Concept Explanation

### Single Inheritance

A child class inherits all attributes and methods from its parent:

```python
class Animal:
    """Base class for animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Make a generic animal sound."""
        return f"{self.name} makes a sound."

class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self):
        """Override with a dog-specific sound."""
        return f"{self.name} says Woof!"

class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self):
        """Override with a cat-specific sound."""
        return f"{self.name} says Meow!"
```

### Overriding Methods

Child classes can **override** any method from the parent to provide specialized behavior:

```python
class Animal:
    def move(self):
        return "Moving..."

class Bird(Animal):
    def move(self):
        return "Flying..."

class Fish(Animal):
    def move(self):
        return "Swimming..."

print(Bird().move())   # Flying...
print(Fish().move())   # Swimming...
```

### Using `super()`

Call the parent's version of a method from the child:

```python
class Vehicle:
    """Base vehicle class."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        """Return vehicle description."""
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Vehicle):
    """Electric car extends Vehicle."""

    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh

    def description(self):
        """Extend parent description."""
        base = super().description()
        return f"{base} ({self.battery_kwh} kWh battery)"
```

### `isinstance()` and `issubclass()`

```python
animal = Animal("Generic")
dog = Dog("Rex")

print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True (inheritance!)
print(isinstance(animal, Dog))   # False

print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False
```

### Method Resolution Order (MRO)

Python determines which method to call using the C3 linearization. Use `ClassName.__mro__` to inspect the order.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### Inheriting from Built-in Types

```python
class MutableString(list):
    """A string-like class that supports mutation."""

    def __init__(self, initial=""):
        super().__init__(initial)

    def __str__(self):
        return "".join(self)

    def append(self, char):
        if len(char) != 1:
            raise ValueError("Only single characters allowed")
        super().append(char)

ms = MutableString("hello")
ms.append("!")
print(str(ms))  # hello!
```

## Common Pitfalls

1. **Forgetting `super().__init__()`**: Child `__init__` completely overrides parent unless you call `super()`.
2. **Deep inheritance hierarchies**: Prefer composition over inheritance for complex cases.
3. **Circular inheritance**: Python raises `TypeError` at class creation time.
4. **Misunderstanding MRO**: Diamond-shaped hierarchies can produce surprising results.

## Hands-On Walkthrough

1. Define a `class Shape` with `__init__(self, color)` and `area()` raising `NotImplementedError`.
2. Define `Circle(Shape)` and `Rectangle(Shape)` that implement `area()`.
3. Write a function that takes any Shape and prints its area.
4. Use `super()` in the child `__init__`.

## Key Takeaways

- Child classes inherit all parent attributes and methods.  
- Override methods to specialize behavior.  
- `super()` lets you call the parent's implementation.  
- `isinstance()` and `issubclass()` check type relationships.  
- MRO determines method lookup order in multiple inheritance.

## Further Reading

- [Python docs: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Python docs: super()](https://docs.python.org/3/library/functions.html#super)
- [Real Python: MRO](https://realpython.com/python-multiple-inheritance/)

## Next Module

Continue to **Module 047: Polymorphism**.
