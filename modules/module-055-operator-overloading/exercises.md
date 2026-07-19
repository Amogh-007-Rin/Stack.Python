# Module 055: Operator Overloading — Exercises

1. **Basic Vector**: Create a `Vector2D` class with `x` and `y`. Overload `__add__`, `__sub__`, `__mul__` (scalar), `__eq__`, and `__repr__`.

2. **Comparison Operators**: Create a `Distance` class (stores meters). Overload all six comparison operators (`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`). Use `functools.total_ordering` to minimize boilerplate.

3. **Unary Operators**: Extend your `Vector2D` with `__neg__`, `__pos__`, and `__abs__` (magnitude).

4. **Custom __str__ and __repr__**: Create a `Money` class with `amount: float` and `currency: str`. Override `__str__` (e.g., "$12.50") and `__repr__` (e.g., "Money(12.5, 'USD')").

5. **__truediv__ with type check**: Create a `Fraction` class with `numerator: int` and `denominator: int`. Overload `__truediv__` to divide by another `Fraction` or an `int`. Return `NotImplemented` for unsupported types.
