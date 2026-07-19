# Module 044: Class Variables vs Instance Variables

> **Phase:** 5. OOP  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 043 (Constructors and self)

## Learning Objectives
By the end of this module, you will be able to:
- Define class variables (shared across all instances)
- Define instance variables (unique to each instance)
- Modify class vs instance variables and understand the difference
- Decide when to use each
- Use `__dict__` to inspect attributes

## Why This Matters
Not all data in a class belongs to individual objects. Class variables let you share state across all instances — like a counter, a default setting, or a constant.

## Concept Explanation

### Class Variables

Defined **outside** any method, directly in the class body. They are shared by all instances.

```python
class Employee:
    """Represent an employee."""

    company = "TechCorp"          # class variable
    employee_count = 0            # class variable

    def __init__(self, name):
        """Initialize employee."""
        self.name = name          # instance variable
        Employee.employee_count += 1
```

```python
e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company)      # TechCorp
print(e2.company)      # TechCorp
print(Employee.company)  # TechCorp
```

### Instance Variables

Defined inside methods (usually `__init__`) with `self.attr`. Each instance has its own copy.

```python
class Employee:
    """Represent an employee."""

    company = "TechCorp"

    def __init__(self, name, salary):
        """Initialize employee with instance vars."""
        self.name = name
        self.salary = salary

e1 = Employee("Alice", 70000)
e2 = Employee("Bob", 80000)

print(e1.name)    # Alice
print(e2.name)    # Bob  (different!)
```

### Modifying Class vs Instance Variables

```python
class Employee:
    company = "TechCorp"

e1 = Employee()
e2 = Employee()

# Modify class variable via class
Employee.company = "NewCorp"
print(e1.company)  # NewCorp
print(e2.company)  # NewCorp

# Shadow: assign to instance creates new instance var
e1.company = "PersonalCo"
print(e1.company)  # PersonalCo  (instance var shadows class var)
print(e2.company)  # NewCorp     (still class var)
print(Employee.company)  # NewCorp
```

### When to Use Each

| Use case | Class Variable | Instance Variable |
|----------|---------------|-------------------|
| Constants / defaults | ✅ `MAX_SPEED = 120` | ❌ |
| Counters | ✅ `total_instances += 1` | ❌ |
| Shared configuration | ✅ `allowed_roles = ["admin"]` | ❌ |
| Unique object data | ❌ | ✅ `self.name = name` |
| Mutable shared state | ⚠️ Use with caution | ✅ |

### `__dict__` for Attribute Inspection

Every object has a `__dict__` that stores its attributes.

```python
class Point:
    """A 2D point."""

    origin_name = "O"

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.__dict__)        # {'x': 3, 'y': 4}
print(Point.__dict__)    # includes origin_name, __init__, etc.
```

## Common Pitfalls

1. **Modifying mutable class variables via one instance**: If a class variable is a list and you do `instance.list.append()`, it affects all instances.
2. **Shadowing**: Assigning `instance.class_var = value` creates a new instance variable instead of modifying the class variable.
3. **Forgetting `self`**: Instance methods must use `self.attr` to access instance variables.

## Hands-On Walkthrough

1. Create a `class Counter` with a class variable `count = 0` and an `__init__` that increments it.
2. Create three instances and print `Counter.count`.
3. Add an instance method that resets only that instance's tracking without affecting the class counter.
4. Inspect `__dict__` on both the class and an instance.

## Key Takeaways

- Class variables are shared across all instances; instance variables are per-object.  
- Access class variables via `ClassName.var` or `self.var` (if not shadowed).  
- Assigning to `self.var` creates an instance variable that may shadow a class variable.  
- Use class variables for shared state, constants, or defaults.  
- `__dict__` lets you inspect all attributes of an object.

## Further Reading

- [Python docs: Class and instance variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [Real Python: Class vs Instance Variables](https://realpython.com/python-class-variables/)

## Next Module

Continue to **Module 045: Encapsulation**.
