# Module 055: Operator Overloading — Solutions

```python
import math
from functools import total_ordering
from typing import Union


# 1. Basic Vector
class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.x, -self.y)

    def __pos__(self) -> "Vector2D":
        return Vector2D(+self.x, +self.y)

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


print(Vector2D(1, 2) + Vector2D(3, 4))
print(abs(Vector2D(3, 4)))

# 2. Comparison Operators with total_ordering
@total_ordering
class Distance:
    def __init__(self, meters: float) -> None:
        self.meters = meters

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return NotImplemented
        return self.meters == other.meters

    def __lt__(self, other: "Distance") -> bool:
        return self.meters < other.meters

    def __repr__(self) -> str:
        return f"Distance({self.meters}m)"


print(Distance(100) > Distance(50))
print(Distance(100) >= Distance(100))

# 3. Money class
class Money:
    def __init__(self, amount: float, currency: str = "USD") -> None:
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        symbols = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3"}
        sym = symbols.get(self.currency, self.currency + " ")
        return f"{sym}{self.amount:.2f}"

    def __repr__(self) -> str:
        return f"Money({self.amount!r}, {self.currency!r})"


m = Money(12.50)
print(str(m))
print(repr(m))

# 4. Fraction with __truediv__
class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __truediv__(self, other: Union["Fraction", int]) -> "Fraction":
        if isinstance(other, int):
            return Fraction(self.numerator, self.denominator * other)
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator * other.denominator,
                self.denominator * other.numerator,
            )
        return NotImplemented

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 / f2)
print(f1 / 2)
```
