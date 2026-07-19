# Module 047: Polymorphism

> **Phase:** 5. OOP  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 046 (Inheritance)

## Learning Objectives
By the end of this module, you will be able to:
- Explain polymorphism as "same interface, different behavior"
- Override methods to achieve polymorphic behavior
- Understand duck typing
- Use operator/function polymorphism (`len()` on different types)
- Describe protocol-based polymorphism

## Why This Matters
Polymorphism lets you write code that works on objects of different types as long as they support the expected interface. This is key to writing flexible, reusable code.

## Concept Explanation

### What is Polymorphism?

Polymorphism means "many forms." The same method call produces different behavior depending on the object type.

```
Same interface:   animal.speak()
Different forms:  Dog → "Woof!"   Cat → "Meow!"   Duck → "Quack!"
```

### Method Overriding (Inheritance-Based)

```python
class Animal:
    """Base animal class."""

    def speak(self):
        """Make a sound."""
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal):
    """Make any animal speak."""
    print(animal.speak())

make_sound(Dog())  # Woof!
make_sound(Cat())  # Meow!
```

The function `make_sound` doesn't care about the specific type — it only cares that the object has a `speak()` method.

### Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck." Python doesn't require explicit inheritance — it only checks if the required method exists.

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm pretending to be a duck!"

def make_it_quack(thing):
    """Call quack on anything that has it."""
    print(thing.quack())

make_it_quack(Duck())     # Quack!
make_it_quack(Person())   # I'm pretending to be a duck!
```

### Operator / Function Polymorphism

Many built-in functions work polymorphically:

```python
print(len("hello"))      # 5  (string)
print(len([1, 2, 3]))    # 3  (list)
print(len({"a": 1, "b": 2}))  # 2  (dict)

print("+" in "plus")     # True  (string containment)
print(3 in [1, 2, 3])    # True  (list containment)
```

### Protocol-Based Polymorphism

Python uses **protocols** — informal interfaces defined by special methods:

| Protocol | Method(s) | Used by |
|----------|----------|---------|
| Iterator | `__iter__`, `__next__` | `for`, `iter()` |
| Callable | `__call__` | `()` operator |
| Context manager | `__enter__`, `__exit__` | `with` statement |
| Sequence | `__getitem__`, `__len__` | `[]`, `len()` |

```python
class LoudList:
    """A list wrapper that announces its length."""

    def __init__(self, items):
        self._items = items

    def __len__(self):
        print(f"Counting {len(self._items)} items...")
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

loud = LoudList([10, 20, 30])
print(len(loud))   # Counting 3 items... \n 3
print(loud[1])     # 20
```

## Common Pitfalls

1. **Requiring explicit type checks**: Rely on duck typing instead of `isinstance()` unless necessary.
2. **Forgetting `raise NotImplementedError`**: Base methods should indicate they must be overridden.
3. **Overriding without calling `super()`**: Sometimes you want to extend, not replace, behavior.
4. **Assuming polymorphism requires inheritance**: Duck typing proves it doesn't.

## Hands-On Walkthrough

1. Define `class Rectangle` and `class Circle` both with `area()` method (no inheritance).
2. Write a function `print_area(shape)` that calls `.area()` on either.
3. Create an object with an `area()` method that's neither Rectangle nor Circle (duck typing).
4. Use `len()` on a custom class by implementing `__len__`.

## Key Takeaways

- Polymorphism: same interface, different behavior.  
- Method overriding is one way to achieve it; duck typing is another.  
- Built-in functions like `len()` are polymorphic — they work on any type with `__len__`.  
- Python protocols are informal contracts defined by special methods.  
- Duck typing means "if it has the method, it's the right type."

## Further Reading

- [Python docs: Polymorphism](https://docs.python.org/3/tutorial/classes.html#polymorphism)
- [Real Python: Duck Typing](https://realpython.com/python-duck-typing/)

## Next Module

Continue to **Module 048: Dunder/Magic Methods (`__str__`, `__repr__`, `__eq__`)**.
