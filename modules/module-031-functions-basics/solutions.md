# Module 031: Solutions

## Exercise 1
```python
def hello():
    """Print a greeting."""
    print("Hello, Python!")

hello()
```

## Exercise 2
```python
def double(n):
    """Double a number and return it.

    Args:
        n: The number to double

    Returns:
        n multiplied by 2
    """
    return n * 2

print(double(7))  # 14
```

## Exercise 3
```python
def subtract(a, b):
    """Return a minus b.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference a - b
    """
    return a - b

print(subtract(10, 3))  # 7
```

## Exercise 4
```python
def subtract(a, b):
    """Subtract b from a and return the result.

    Args:
        a: The number to subtract from
        b: The number to subtract

    Returns:
        a minus b
    """
    return a - b
```

## Exercise 5
```
Inside: 20
Outside: 10
```
The `x = 20` inside the function creates a new local variable; it does not modify the global `x`.

## Exercise 6
```python
def sum_to(n):
    """Sum numbers from 1 to n.

    Args:
        n: Upper limit (inclusive)

    Returns:
        Sum of 1 + 2 + ... + n
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to(5))   # 15
print(sum_to(100)) # 5050
```

## Exercise 7
```python
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit.

    Args:
        c: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit
    """
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
```

## Exercise 8
```python
def min_max(numbers):
    """Return the minimum and maximum from a list.

    Args:
        numbers: A list of numbers

    Returns:
        Tuple of (minimum, maximum)
    """
    return min(numbers), max(numbers)

print(min_max([3, 1, 9, 2, 7]))  # (1, 9)
```

## Exercise 9
```python
def repeat(text, times):
    """Repeat text a given number of times with spaces.

    Args:
        text: The string to repeat
        times: How many times to repeat

    Returns:
        Repeated string with spaces
    """
    return (text + " ") * times

print(repeat("Hi", 3))  # "Hi Hi Hi "
```

## Exercise 10
```python
def is_even(n):
    """Check if a number is even.

    Args:
        n: The number to check

    Returns:
        True if n is even, False otherwise
    """
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
```
