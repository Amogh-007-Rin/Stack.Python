# Module 054: Enums — Solutions

```python
from enum import Enum, auto, IntEnum
from typing import Iterable


# 1. Basic Enum
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def is_weekend(day: Weekday) -> bool:
    return day in (Weekday.SATURDAY, Weekday.SUNDAY)


print(is_weekend(Weekday.SATURDAY))
print(is_weekend(Weekday.MONDAY))

# 2. auto() Values
class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


for level in LogLevel:
    print(f"{level.name} = {level.value}")

# 3. IntEnum
class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


print(HttpStatus.OK == 200)
print(HttpStatus.NOT_FOUND.value)

# 4. Enum Iteration
class Suit(Enum):
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"
    SPADES = "S"


for suit in Suit:
    print(suit)
print(f"Number of suits: {len(Suit)}")

# 5. Enums vs Constants
class OrderStatus(Enum):
    PENDING = auto()
    CONFIRMED = auto()
    SHIPPED = auto()
    DELIVERED = auto()


def update_order(order_id: int, status: OrderStatus) -> str:
    return f"Order {order_id} updated to {status.name}"


print(update_order(1001, OrderStatus.SHIPPED))
# update_order(1001, "shipped")  # type checker would flag this
```
