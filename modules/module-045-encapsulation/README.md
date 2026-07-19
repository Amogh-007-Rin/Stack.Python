# Module 045: Encapsulation

> **Phase:** 5. OOP  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 044 (Class vs Instance Variables)

## Learning Objectives
By the end of this module, you will be able to:
- Explain the concept of encapsulation
- Use `_protected` naming convention
- Use `__name` mangling for private-like attributes
- Implement getter/setter patterns
- Understand why encapsulation matters for maintainable code

## Why This Matters
Encapsulation hides internal details and exposes only what's necessary. This prevents accidental misuse and makes it safe to change internals without breaking external code.

## Concept Explanation

### What is Encapsulation?

Encapsulation means **bundling data with the methods that operate on it** and **restricting direct access** to internal state.

```
┌──────────────────────────────┐
│         Object               │
│                              │
│  ╔══════════╗    public API  │
│  ║ data     ║  ←──────────  │
│  ║          ║  methods      │
│  ╚══════════╝               │
│       ▲  internal state     │
│       │  (hidden)           │
└───────┴──────────────────────┘
```

### Naming Conventions

Python uses **conventions** rather than strict access control. Everything is public — trust is assumed.

| Convention | Syntax | Meaning |
|-----------|--------|---------|
| Public | `self.name` | Part of the public API |
| Protected | `self._name` | Internal use (convention only) |
| Name mangled | `self.__name` | Stronger hint of privacy |

```python
class BankAccount:
    """A bank account with encapsulation."""

    def __init__(self, owner, balance):
        self.owner = owner         # public
        self._branch_code = "001"  # protected — internal use
        self.__balance = balance   # name mangled — "private"

    def deposit(self, amount):
        """Deposit money."""
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        """Get current balance."""
        return self.__balance
```

### Name Mangling Details

When you prefix with `__`, Python renames it: `_ClassName__attr`. This avoids accidental overrides in subclasses but is still accessible if you know the mangled name.

```python
acc = BankAccount("Alice", 1000)
# print(acc.__balance)       # AttributeError!
print(acc._BankAccount__balance)  # 1000 — still accessible but clearly internal
```

### Getter / Setter Patterns

Before Python's `@property` (covered fully in Module 052), you can use explicit getter/setter methods:

```python
class Temperature:
    """Temperature with getter/setter."""

    def __init__(self, celsius=0):
        self._celsius = celsius

    def get_celsius(self):
        """Return temperature in Celsius."""
        return self._celsius

    def set_celsius(self, value):
        """Set temperature, ensuring sensible range."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    def get_fahrenheit(self):
        """Convert to Fahrenheit."""
        return self._celsius * 9/5 + 32
```

```python
t = Temperature(25)
print(t.get_celsius())      # 25
print(t.get_fahrenheit())   # 77.0
t.set_celsius(30)
```

### Why Encapsulation Matters

1. **Validation**: Prevent invalid state (e.g., negative age)
2. **Decoupling**: Change internal implementation without affecting users
3. **Debugging**: Add logging or breakpoints easily at the method level
4. **Contracts**: Methods document what goes in/out; direct attribute access bypasses them

## Common Pitfalls

1. **Thinking `__` makes truly private**: It's still accessible via `_ClassName__attr`.
2. **Over-encapsulating**: Not everything needs a getter — plain attributes are fine when no logic is required.
3. **Confusing `_` and `__`**: Use `_` for "internal use" and `__` to avoid name collisions in inheritance.

## Hands-On Walkthrough

1. Create a `class Person` with a "private" `__age` attribute.
2. Add getter `get_age()` and setter `set_age(age)` with validation (age > 0 and < 150).
3. Attempt to access `__age` directly and via the mangled name.
4. Create a subclass and see how name mangling prevents accidental overrides.

## Key Takeaways

- Encapsulation hides internal state and exposes a controlled interface.  
- `_name` = protected convention; `__name` = name mangling for stronger privacy.  
- Getter/setter methods allow validation and future flexibility.  
- Encapsulation makes code more robust and maintainable.

## Further Reading

- [Python docs: Private variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [PEP 8: Naming conventions](https://peps.python.org/pep-0008/#naming-conventions)

## Next Module

Continue to **Module 046: Inheritance**.
