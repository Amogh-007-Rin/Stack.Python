# Module 038: Solutions

## Exercise 1
```python
def odds(n):
    """Yield odd numbers up to n.

    Args:
        n: Upper limit

    Yields:
        Odd numbers from 1 to n
    """
    for i in range(1, n + 1, 2):
        yield i

print(list(odds(10)))  # [1, 3, 5, 7, 9]
```

## Exercise 2
```python
result = sum(x ** 2 for x in range(1, 101))
print(result)  # 338350
```

## Exercise 3
```python
letters = (c for c in "Python")
print(next(letters))  # P
print(next(letters))  # y
print(next(letters))  # t
print(next(letters))  # h
print(next(letters))  # o
print(next(letters))  # n
```

## Exercise 4
```python
def flatten(lists):
    """Flatten a list of lists using yield from.

    Args:
        lists: List of lists

    Yields:
        Individual items from each sublist
    """
    for sublist in lists:
        yield from sublist

nested = [[1, 2], [3, 4, 5], [6]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

## Exercise 5
```python
def counter(start=0):
    """Infinite counter starting from start.

    Args:
        start: Starting number

    Yields:
        Consecutive integers
    """
    i = start
    while True:
        yield i
        i += 1

c = counter(5)
print([next(c) for _ in range(5)])  # [5, 6, 7, 8, 9]
```

## Exercise 6
```python
def numbers(n):
    """Yield numbers from 0 to n."""
    for i in range(n):
        yield i

def squares(nums):
    """Yield squares from a number generator."""
    for n in nums:
        yield n ** 2

pipeline = squares(numbers(10))
print(list(pipeline))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Exercise 7
```python
def read_lines(filename):
    """Read a file line by line.

    Args:
        filename: Path to file

    Yields:
        Individual lines
    """
    with open(filename) as f:
        for line in f:
            yield line.rstrip("\n")

# Example (creates a test file first)
with open("/tmp/test.txt", "w") as f:
    f.write("line1\nline2\nline3\n")

for line in read_lines("/tmp/test.txt"):
    print(line)
```

## Exercise 8
```python
def running_average():
    """Generator that maintains a running average via send()."""
    total = 0
    count = 0
    while True:
        value = yield total / count if count > 0 else 0
        if value is not None:
            total += value
            count += 1

avg = running_average()
next(avg)  # prime the generator
print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
```

## Exercise 9
```python
def primes():
    """Generate prime numbers infinitely."""
    yield 2
    n = 3
    while True:
        is_prime = True
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 2

p = primes()
print([next(p) for _ in range(10)])  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Exercise 10
```python
import sys

n = 1_000_000
list_squares = [x ** 2 for x in range(n)]
gen_squares = (x ** 2 for x in range(n))

print(f"List of {n} squares: {sys.getsizeof(list_squares)} bytes")
print(f"Generator of {n} squares: {sys.getsizeof(gen_squares)} bytes")
# The generator is ~200 bytes regardless of n!
```
