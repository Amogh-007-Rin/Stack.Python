# Module 057: Custom Exceptions — Solutions

```python
import math


# 1. Simple Custom Exception
class NegativeNumberError(Exception):
    pass


def sqrt_positive(x: float) -> float:
    if x < 0:
        raise NegativeNumberError(f"Cannot compute sqrt of {x}")
    return math.sqrt(x)


try:
    sqrt_positive(-4)
except NegativeNumberError as e:
    print(f"Error: {e}")

# 2. Exception with Attributes
class GradeOutOfRangeError(Exception):
    def __init__(self, grade: float, min_value: float, max_value: float) -> None:
        self.grade = grade
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(f"Grade {grade} is outside [{min_value}, {max_value}]")


def validate_grade(grade: float) -> None:
    if not 0 <= grade <= 100:
        raise GradeOutOfRangeError(grade, 0, 100)


try:
    validate_grade(105)
except GradeOutOfRangeError as e:
    print(f"Invalid grade {e.grade}")

# 3. Exception Hierarchy
class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
    def __init__(self, isbn: str) -> None:
        self.isbn = isbn
        super().__init__(f"Book with ISBN {isbn} not found")


class BookNotAvailableError(LibraryError):
    def __init__(self, isbn: str) -> None:
        self.isbn = isbn
        super().__init__(f"Book {isbn} is currently checked out")


class MemberNotFoundError(LibraryError):
    def __init__(self, member_id: str) -> None:
        self.member_id = member_id
        super().__init__(f"Member {member_id} not found")


def checkout_book(isbn: str) -> None:
    raise BookNotAvailableError(isbn)


try:
    checkout_book("978-0451524935")
except LibraryError as e:
    print(f"Library: {e}")

# 4. Bank transfer with custom exception
class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float) -> None:
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance={balance}, needed={amount}")


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def transfer_to(self, other: "BankAccount", amount: float) -> str:
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        other.balance += amount
        return f"Transferred ${amount:.2f} to {other.owner}"


alice = BankAccount("Alice", 500)
bob = BankAccount("Bob", 100)

try:
    alice.transfer_to(bob, 600)
except InsufficientFundsError as e:
    print(f"Transfer failed: {e}")

# 5. Re-raising with context
class ValidationError(Exception):
    def __init__(self, field: str, message: str) -> None:
        self.field = field
        super().__init__(f"{field}: {message}")


def process_order(order_data: dict) -> str:
    try:
        if "email" not in order_data:
            raise ValidationError("email", "Email is required")
        if "@" not in order_data["email"]:
            raise ValidationError("email", "Invalid email format")
        return "Order processed"
    except ValidationError:
        print(f"Validation failed for order: {order_data}")
        raise


try:
    process_order({"item": "book"})
except ValidationError as e:
    print(f"Caught after re-raise: {e}")
```
