# Module 064: Packages and \_\_init\_\_.py — Solutions

```python
import os


# 1. Basic package
# Create structure:
# mypackage/
#   __init__.py  (empty)
#   math_ops.py
#
# math_ops.py:
"""
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b
"""

# In script:
# import mypackage.math_ops
# print(mypackage.math_ops.add(5, 3))


# 2. Package initialization
# Edit mypackage/__init__.py:
"""
from .math_ops import add, subtract
"""

# Now: from mypackage import add, subtract


# 3. Subpackages
# Create mypackage/advanced/__init__.py (empty)
# Create mypackage/advanced/calc.py:
"""
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
"""

# Absolute import:
# from mypackage.advanced.calc import factorial
# print(factorial(5))


# 4. __all__
# Edit mypackage/__init__.py:
"""
from .math_ops import add, subtract

__all__ = ["add"]
"""

# from mypackage import *  # only imports add


# 5. Relative imports
# Edit mypackage/advanced/calc.py:
"""
from ..math_ops import add

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
"""


# 6. Namespace package
# Create without __init__.py:
# namespace_pkg/sub_a/mod_a.py
# namespace_pkg/sub_b/mod_b.py

# import namespace_pkg.sub_a.mod_a
# import namespace_pkg.sub_b.mod_b
print("Namespace packages work without __init__.py")
```
