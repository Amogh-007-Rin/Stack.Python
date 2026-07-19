# Module 052: Class Methods, Static Methods, Properties — Solutions

```python
import math
from datetime import datetime, timezone
from typing import Optional


# 1. Alternative Constructor
class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    @classmethod
    def from_string(cls, data: str) -> "Book":
        parts = data.split("|")
        return cls(parts[0], parts[1], parts[2])


book = Book.from_string("1984|George Orwell|978-0451524935")
print(book.title)

# 2. Static Method Utility
class MathUtils:
    @staticmethod
    def factorial(n: int) -> int:
        return math.factorial(n)

    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


print(MathUtils.factorial(5))
print(MathUtils.is_prime(17))

# 3. Property with Validation
class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = initial_balance
        self.created_at = datetime.now(timezone.utc)

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @property
    def account_age_days(self) -> float:
        return (datetime.now(timezone.utc) - self.created_at).total_seconds() / 86400


acct = BankAccount("Alice", 100)
print(acct.balance)

# 4. Property Getter/Setter/Deleter
class Password:
    def __init__(self) -> None:
        self._password: Optional[str] = None

    @property
    def password(self) -> str:
        return "****" if self._password else ""

    @password.setter
    def password(self, value: str) -> None:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        self._password = value

    @password.deleter
    def password(self) -> None:
        self._password = None


# 5. Combined
class Temperature:
    def __init__(self, celsius: float = 0.0) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)


t = Temperature.from_fahrenheit(212)
print(f"{t.celsius:.1f}C = {t.fahrenheit:.1f}F")
```
