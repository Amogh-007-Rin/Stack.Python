# Solutions: Testing Basics: unittest

## Exercise 1 & 2: Calculator Test Class
```python
import unittest

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_divide(self) -> None:
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=3)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

## Exercise 3: setUp
```python
import unittest

class TestWithSetup(unittest.TestCase):
    def setUp(self) -> None:
        self.numbers = [1, 2, 3, 4, 5]

    def test_sum(self) -> None:
        self.assertEqual(sum(self.numbers), 15)

    def test_length(self) -> None:
        self.assertEqual(len(self.numbers), 5)

if __name__ == '__main__':
    unittest.main()
```

## Exercise 4: Multiple Multiply Tests
```python
class TestMultiply(unittest.TestCase):
    def test_multiply(self) -> None:
        test_cases = [(2, 3, 6), (0, 5, 0), (-1, 5, -5), (3, 3, 9)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiply(a, b), expected)
```

## Exercise 5: Test Discovery
```
tests/
  test_calculator.py
  test_strings.py

Run: python -m unittest discover -s tests
```

## Exercise 6: String Processing
```python
def reverse_string(s: str) -> str:
    return s[::-1]

class TestStringReverse(unittest.TestCase):
    def test_empty(self) -> None:
        self.assertEqual(reverse_string(""), "")

    def test_single_char(self) -> None:
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self) -> None:
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_normal(self) -> None:
        self.assertEqual(reverse_string("hello"), "olleh")

if __name__ == '__main__':
    unittest.main()
```
