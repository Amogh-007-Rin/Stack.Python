# Module 042: Attributes and Methods

> **Phase:** 5. OOP  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 041 (Introduction to OOP)

## Learning Objectives
By the end of this module, you will be able to:
- Define instance attributes using `self.attr`
- Write methods — functions defined inside a class
- Call methods on an instance
- Use `__init__` to initialize attributes
- Add and change attributes dynamically
- Distinguish between a method and a standalone function

## Why This Matters
Attributes store an object's data; methods define what an object can do. Together they form the core of every class you'll ever write.

## Concept Explanation

### Instance Attributes

Attributes are pieces of data attached to an instance. They are created by assigning to `self` inside methods (usually `__init__`).

```python
class Student:
    """Represent a student."""

    def __init__(self, name, student_id):
        """Initialize student attributes."""
        self.name = name
        self.student_id = student_id
        self.courses = []  # default value
```

### Methods

A **method** is a function defined inside a class. The first parameter is always `self`.

```python
class Student:
    """Represent a student."""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        """Enroll the student in a course."""
        self.courses.append(course)

    def display_info(self):
        """Show student info."""
        info = f"{self.name} (ID: {self.student_id})\nEnrolled: {', '.join(self.courses) if self.courses else 'None'}"
        return info
```

### Calling Methods

```python
alice = Student("Alice", "S1001")
alice.enroll("Python 101")
alice.enroll("Data Structures")
print(alice.display_info())
# Alice (ID: S1001)
# Enrolled: Python 101, Data Structures
```

### Adding / Changing Attributes Dynamically

Python objects are flexible — you can add attributes after creation:

```python
alice.gpa = 3.8       # new attribute added on the fly
alice.name = "Alice B."  # existing attribute changed
```

This flexibility is powerful but can lead to bugs — `__init__` documents what attributes an instance should have.

### Method vs Function

| Aspect | Function | Method |
|--------|----------|--------|
| Defined | Standalone with `def` | Inside a class with `def` |
| First parameter | Any parameters | `self` (the instance) |
| Called on | Directly | `instance.method()` |
| Access to instance | No | Yes, via `self` |

```python
def greet(name):          # function
    return f"Hello {name}"

class Person:
    def greet(self):      # method
        return f"Hello {self.name}"
```

## Common Pitfalls

1. **Forgetting `self` in method definition**: Causes a `TypeError` when called.
2. **Omitting parentheses in method call**: `obj.method` returns the method object, doesn't call it.
3. **Using class name instead of `self`**: Always refer to instance attributes via `self`.
4. **Assuming attribute exists**: Check with `hasattr()` or use `getattr(obj, attr, default)`.

## Hands-On Walkthrough

1. Write a `class BankAccount` with `__init__` that sets `owner` and `balance`.
2. Add methods `deposit(amount)` and `withdraw(amount)`.
3. Create an account, deposit 100, withdraw 30, and print the balance.
4. Add a new attribute `account_type` dynamically after creation.

## Key Takeaways

- Attributes store data; methods define behavior.  
- Use `self.attr = value` inside `__init__` to initialize attributes.  
- Methods are called on an instance: `instance.method()`.  
- Python lets you add attributes dynamically, but `__init__` is the canonical place.  
- Methods are functions that belong to a specific class instance.

## Further Reading

- [Python docs: Instance methods](https://docs.python.org/3/tutorial/classes.html#instance-objects)
- [Real Python: Attributes and Methods](https://realpython.com/python-attributes-and-methods/)

## Next Module

Continue to **Module 043: Constructors (`__init__`) and self**.
