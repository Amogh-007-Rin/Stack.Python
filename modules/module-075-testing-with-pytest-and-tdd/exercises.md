# Exercises: Testing with pytest and TDD

## Exercise 1: First pytest Test
Write a function `is_palindrome(s: str) -> bool` and test it with pytest using plain assert.

## Exercise 2: Parametrize
Use `@pytest.mark.parametrize` to test `is_palindrome` with: "racecar", "hello", "", "a", "Aba" (case-insensitive).

## Exercise 3: TDD Cycle
Practice red-green-refactor:
1. Write a test for `fib(n: int) -> int` returning the nth Fibonacci number
2. Run it (it should fail - red)
3. Implement the function (green)
4. Refactor to use a more efficient approach

## Exercise 4: Fixtures
Create a fixture that provides a list of numbers `[1, 2, 3, 4, 5]`. Write tests using that fixture.

## Exercise 5: Mocking
Write a function `get_weather(city: str) -> str` that calls an external API. Use `unittest.mock.patch` to mock the API call in tests.

## Exercise 6: conftest.py
Create a `conftest.py` with a shared fixture and use it across multiple test files.

## Challenge: Pytest Coverage
Install pytest-cov and run tests with coverage report. Aim for 100% coverage on a simple module.
