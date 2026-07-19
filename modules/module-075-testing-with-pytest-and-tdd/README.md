# Module 075: Testing with pytest and Test-Driven Development

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2 hours

## Learning Objectives

- Write tests using pytest with plain assert statements
- Implement the TDD cycle: red-green-refactor
- Use pytest fixtures for reusable test setup
- Parametrize tests with @pytest.mark.parametrize
- Mock dependencies with unittest.mock and pytest-mock
- Run pytest with various flags

## Topics Covered

1. pytest syntax and assert statements
2. TDD cycle (red-green-refactor)
3. pytest fixtures and conftest.py
4. Parametrized tests
5. Mocking with unittest.mock / pytest-mock
6. Running pytest (pytest -v, pytest --cov)

## Prerequisites

Modules 000-074.

## Key Concepts

```python
# test_calculator.py
import pytest

def add(a: int, b: int) -> int:
    return a + b

def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6), (0, 5, 0), (-1, 5, -5),
])
def test_multiply(a: int, b: int, expected: int) -> None:
    assert a * b == expected
```

## Resources

- pytest documentation
- "Test-Driven Development with Python" book
- pytest-cov plugin
