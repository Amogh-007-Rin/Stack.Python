# Module 038: Generators and yield

> **Phase:** 4. Functions  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)
- Module 036 (Higher-Order Functions)

## Learning Objectives
By the end of this module, you will be able to:
- Define generator functions using `yield`
- Write generator expressions
- Understand lazy evaluation and memory efficiency
- Use `next()` and handle `StopIteration`
- Use `yield from` to delegate to sub-generators
- Build infinite sequences
- Compare generators vs lists

## Why This Matters
Generators allow you to work with large or infinite data streams without loading everything into memory. They are essential for efficient iteration in data processing, pipeline building, and memory-constrained environments.

## Concept Explanation

### Generator Functions with `yield`

A generator function uses `yield` instead of `return`. When called, it returns a generator object that yields values one at a time:

```python
def count_up_to(n):
    """Yield numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)  # 1 2 3 4 5
```

### How `yield` Works

Each `yield` pauses the function, saving its state. The next call to `next()` resumes from where it left off:

```python
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # StopIteration
```

### Generator Expressions

Similar to list comprehensions but use `()` instead of `[]`:

```python
squares = (x ** 2 for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1
```

### Memory Efficiency

```python
# List — all values in memory
big_list = [x for x in range(100_000_000)]  # MemoryError!

# Generator — one value at a time
big_gen = (x for x in range(100_000_000))   # Works fine
```

### `yield from`

Delegate to another generator:

```python
def chain(*iterables):
    for it in iterables:
        yield from it

def a():
    yield from "abc"

def b():
    yield from [1, 2, 3]

combined = chain(a(), b())
print(list(combined))  # ['a', 'b', 'c', 1, 2, 3]
```

### Infinite Sequences

Generators can represent infinite sequences:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Generators vs Lists

| Aspect | List | Generator |
|--------|------|-----------|
| Memory | All elements in memory | One at a time |
| Speed | Faster for small data | Slightly slower per item |
| Reusability | Can iterate multiple times | Exhausted after one pass |
| Use case | Small/known datasets | Large/infinite streams |

## Common Pitfalls

1. **Generator exhaustion**: You can only iterate once through a generator.
2. **Converting to list unnecessarily**: Defeats the memory advantage.
3. **Using `return` with a value**: In a generator, `return value` is equivalent to `raise StopIteration(value)`.
4. **Modifying the generator from outside**: It's an iterator, not a data store.

## Hands-On Walkthrough

1. Write a generator `even_numbers(n)` that yields even numbers up to n.
2. Write a generator expression that yields squares of odd numbers.
3. Use `yield from` to flatten a list of lists.
4. Create an infinite generator for the Fibonacci sequence and print the first 20 values.

## Key Takeaways

- `yield` produces a value and pauses the function; the function resumes on the next `next()` call.
- Generator expressions are memory-efficient alternatives to list comprehensions.
- `yield from` delegates to a sub-generator.
- Generators are single-use; they are exhausted after iteration.
- Ideal for large or infinite data streams.

## Further Reading
- [Python docs: Generators](https://docs.python.org/3/tutorial/classes.html#generators)
- [PEP 255 — Simple Generators](https://peps.python.org/pep-0255/)
- [Real Python: Generators](https://realpython.com/python-generators/)

## Next Module
Continue to **Module 039: Iterators and the Iterator Protocol**.
