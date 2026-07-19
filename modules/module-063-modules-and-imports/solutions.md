# Module 063: Modules and Imports — Solutions

```python
import sys
import importlib


# 1. Import styles
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.sqrt(16))


# 2. Module guard
# Create greeter.py:
"""
def greet(name: str) -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
"""


# 3. sys.path
print("Original sys.path:", sys.path)
sys.path.insert(0, "/tmp/my_modules")
print("Modified sys.path:", sys.path)


# 4. Custom module
# Create utils.py:
"""
def add(a: float, b: float) -> float:
    return a + b

def multiply(a: float, b: float) -> float:
    return a * b
"""

# In another script:
# import utils
# print(utils.add(3, 4))
# print(utils.multiply(3, 4))


# 5. Circular import avoidance
# Create shared.py with shared code:
"""
def helper() -> str:
    return "shared helper"
"""
# Then a.py and b.py import from shared instead of each other.


# 6. importlib.reload
# Create messages.py:
"""
greeting = "Hello"
"""

import messages  # type: ignore  # noqa: F402
print(messages.greeting)

# Edit messages.py to change greeting to "Hi"
importlib.reload(messages)
print(messages.greeting)
```
