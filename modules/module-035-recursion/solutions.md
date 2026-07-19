# Module 035: Solutions

## Exercise 1
```python
def sum_n(n: int) -> int:
    """Sum numbers from 1 to n recursively.

    Args:
        n: Upper limit (inclusive)

    Returns:
        Sum of 1 + 2 + ... + n
    """
    if n <= 1:
        return n
    return n + sum_n(n - 1)

print(sum_n(5))   # 15
print(sum_n(100))  # 5050
```

## Exercise 2
```python
def power(base: int, exp: int) -> int:
    """Calculate base^exp recursively.

    Args:
        base: The base number
        exp: The exponent

    Returns:
        base raised to the power of exp
    """
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))  # 32
```

## Exercise 3
```python
def count_items(lst: list) -> int:
    """Count items in a list recursively.

    Args:
        lst: The list to count

    Returns:
        Number of items in the list
    """
    if not lst:
        return 0
    return 1 + count_items(lst[1:])

print(count_items([1, 2, 3, 4, 5]))  # 5
```

## Exercise 4
```python
def reverse_string(s: str) -> str:
    """Reverse a string recursively.

    Args:
        s: The string to reverse

    Returns:
        The reversed string
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # olleh
```

## Exercise 5
```python
def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome recursively.

    Args:
        s: The string to check

    Returns:
        True if palindrome, False otherwise
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

## Exercise 6
```python
def fib_memo(n: int, memo: dict = None) -> int:
    """Calculate Fibonacci with memoization.

    Args:
        n: Position in Fibonacci sequence
        memo: Dictionary storing computed values

    Returns:
        The nth Fibonacci number
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(35))  # 9227465 (fast!)
```

## Exercise 7
```python
def flatten(nested_list: list) -> list:
    """Flatten a nested list one level.

    Args:
        nested_list: List that may contain sublists

    Returns:
        Flattened list
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, [5, 6]]]))  # [1, 2, 3, 4, 5, 6]
```

## Exercise 8
```python
def ackermann(m: int, n: int) -> int:
    """Compute the Ackermann function.

    Args:
        m: First parameter
        n: Second parameter

    Returns:
        Ackermann value
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3, 4))  # 125
```

## Exercise 9
The default recursion limit is 1000. `factorial(1000)` will work, but `factorial(1001)` will raise RecursionError. The exact point depends on your system's stack size.

## Exercise 10
```python
def fib_iterative(n: int) -> int:
    """Calculate Fibonacci iteratively.

    Args:
        n: Position in Fibonacci sequence

    Returns:
        The nth Fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

import time
start = time.time()
print(fib_iterative(35))
print(f"Iterative: {time.time() - start:.4f}s")

start = time.time()
print(fib_memo(35))
print(f"Recursive+memo: {time.time() - start:.4f}s")
```
