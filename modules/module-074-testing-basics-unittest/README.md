# Module 074: Testing Basics: unittest

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2 hours

## Learning Objectives

- Understand why testing is important
- Write tests using the unittest module
- Use TestCase and assert methods
- Set up test fixtures with setUp/tearDown
- Discover and run tests with python -m unittest
- Organize tests in a project

## Topics Covered

1. Why testing matters
2. unittest module and TestCase class
3. Assert methods (assertEqual, assertTrue, assertRaises, etc.)
4. setUp and tearDown methods
5. Test discovery
6. Organizing test files

## Prerequisites

Modules 000-073.

## Key Concepts

```python
import unittest

def add(a: int, b: int) -> int:
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(2, 2), 5)

if __name__ == '__main__':
    unittest.main()
```

## Resources

- Python docs: unittest module
- Python Testing with unittest (Real Python)
