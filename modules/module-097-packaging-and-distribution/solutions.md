# Solutions: Packaging and Distributing Python Projects (PyPI)

## Exercise 1: Minimal Package Structure
```python
# calculator/__init__.py
from calculator.ops import add, subtract, multiply, divide

__all__ = ['add', 'subtract', 'multiply', 'divide']
```

```python
# calculator/ops.py
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "calculator"
version = "0.1.0"
description = "A simple calculator package"
readme = "README.md"
license = {text = "MIT"}
```

## Exercise 2: Metadata
```toml
[project]
name = "calculator"
version = "0.1.0"
description = "A simple calculator package"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "you@example.com"},
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
```

## Exercise 3: __version__ Convention
```python
# calculator/__init__.py
__version__: str = "0.1.0"

from calculator.ops import add, subtract, multiply, divide
```

```python
# show_version.py
import calculator

print(f"Calculator version: {calculator.__version__}")
```

## Exercise 4: CLI Script
```toml
[project.scripts]
calculator = "calculator.cli:main"
```

```python
# calculator/cli.py
import sys
from typing import List
from calculator.ops import add, subtract, multiply, divide

def main() -> None:
    args: List[str] = sys.argv[1:]
    if len(args) != 3:
        print("Usage: calculator <a> <op> <b>")
        print("Operations: add, sub, mul, div")
        sys.exit(1)

    a: float = float(args[0])
    op: str = args[1]
    b: float = float(args[2])

    ops = {
        'add': add, 'sub': subtract,
        'mul': multiply, 'div': divide,
    }

    if op not in ops:
        print(f"Unknown operation: {op}")
        sys.exit(1)

    result = ops[op](a, b)
    print(f"Result: {result}")
```

## Exercise 5: Build and Test
```bash
# Build
python -m build

# Check
twine check dist/*

# Output should show:
# Checking dist/calculator-0.1.0.tar.gz: PASSED
# Checking dist/calculator-0.1.0-py3-none-any.whl: PASSED
```

## Exercise 6: Semantic Versioning
```python
"""
Given version 1.3.0:

- A bug fix:        1.3.1  (patch bump)
- New backward-compatible feature: 1.4.0  (minor bump)
- Breaking API change:            2.0.0  (major bump)
"""
```

## Challenge: Upload to Test PyPI
```bash
# Install and configure
pip install twine

# Build
python -m build

# Upload
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ calculator

# Test it
python -c "import calculator; print(calculator.add(2, 3))"
```
