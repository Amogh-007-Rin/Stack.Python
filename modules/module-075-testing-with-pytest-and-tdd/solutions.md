# Solutions: Testing with pytest and TDD

## Exercise 1 & 2: Palindrome Tests
```python
# test_palindrome.py
import pytest

def is_palindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

@pytest.mark.parametrize("text,expected", [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("Aba", True),  # case-insensitive
])
def test_is_palindrome(text: str, expected: bool) -> None:
    assert is_palindrome(text) == expected
```

## Exercise 3: TDD Cycle
```python
# test_fib.py
import pytest

def fib(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@pytest.mark.parametrize("n,expected", [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (10, 55),
])
def test_fib(n: int, expected: int) -> None:
    assert fib(n) == expected
```

## Exercise 4: Fixtures
```python
# conftest.py
import pytest

@pytest.fixture
def numbers() -> list:
    return [1, 2, 3, 4, 5]
```

```python
# test_with_fixture.py
def test_sum(numbers: list) -> None:
    assert sum(numbers) == 15

def test_max(numbers: list) -> None:
    assert max(numbers) == 5
```

## Exercise 5: Mocking
```python
# weather.py
import requests

def get_weather(city: str) -> str:
    url = f"https://api.weather.example.com/v1/{city}"
    response = requests.get(url)
    return response.json()["weather"]
```

```python
# test_weather.py
from unittest.mock import patch
import pytest

def test_get_weather() -> None:
    mock_response = {"weather": "sunny"}
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response
        from weather import get_weather
        result = get_weather("London")
        assert result == "sunny"
```

## Exercise 6: conftest.py
```python
# conftest.py
import pytest

@pytest.fixture
def sample_data() -> dict:
    return {"name": "Alice", "age": 30}
```

```python
# test_user.py
def test_user_name(sample_data: dict) -> None:
    assert sample_data["name"] == "Alice"

# test_profile.py
def test_user_age(sample_data: dict) -> None:
    assert sample_data["age"] == 30
```

```bash
# Run with coverage
pytest --cov=my_module tests/
```
