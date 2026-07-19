# Module 039: Iterators and the Iterator Protocol

> **Phase:** 4. Functions  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- Module 038 (Generators and yield)

## Learning Objectives
By the end of this module, you will be able to:
- Explain the iterator protocol (`__iter__`, `__next__`, `StopIteration`)
- Use `iter()` and `next()` built-in functions
- Describe how `for` loops work under the hood
- Create custom iterator classes
- Distinguish between iterables and iterators

## Why This Matters
The iterator protocol is the foundation of all iteration in Python — `for` loops, list comprehensions, `map()`, `filter()`, and more. Understanding it gives you deep insight into Python's design and lets you create your own iterable objects.

## Concept Explanation

### The Iterator Protocol

An **iterable** is any object that can return an iterator (has `__iter__()`).  
An **iterator** is an object that produces values one at a time (has `__next__()` and `__iter__()`).

```
Protocol:
1. Call iter() on an iterable → get an iterator
2. Call next() on the iterator → get values
3. When exhausted → raises StopIteration
```

### `iter()` and `next()` Built-ins

```python
my_list = [1, 2, 3]
it = iter(my_list)       # get iterator from list
print(next(it))          # 1
print(next(it))          # 2
print(next(it))          # 3
print(next(it))          # StopIteration!
```

### For Loop Mechanics Under the Hood

A `for` loop is syntactic sugar for the iterator protocol:

```python
for item in iterable:
    print(item)

# Internally:
_it = iter(iterable)
while True:
    try:
        item = next(_it)
    except StopIteration:
        break
    print(item)
```

### Creating Custom Iterators

Implement `__iter__()` and `__next__()` in a class:

```python
class CountDown:
    """Iterate from n down to 1."""

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

for i in CountDown(5):
    print(i)  # 5 4 3 2 1
```

### Iterable vs Iterator

| Aspect | Iterable | Iterator |
|--------|----------|----------|
| Has `__iter__()` | Yes | Yes |
| Has `__next__()` | No | Yes |
| Can be used in `for` | Yes (returns iterator) | Yes |
| Can be used multiple times | Yes (new iterator each time) | No (single use) |
| Example | `list`, `str`, `tuple` | `file object`, `generator` |

```python
nums = [1, 2, 3]       # iterable
it1 = iter(nums)       # iterator
it2 = iter(nums)       # new iterator — can iterate again
```

## Common Pitfalls

1. **Confusing iterable and iterator**: Lists are iterable, not iterators — they don't have `__next__()`.
2. **Forgetting `__iter__` in custom iterators**: Must return `self`.
3. **Not raising `StopIteration`**: The for loop would run forever.
4. **Exhausting a generator**: Generators are single-use iterators.

## Hands-On Walkthrough

1. Create a list, get an iterator with `iter()`, and manually call `next()` until StopIteration.
2. Write a custom `class Range` that works like `range()` using the iterator protocol.
3. Prove that `for` loops use the iterator protocol by manually simulating one.
4. Check if different types are iterable using `hasattr(obj, '__iter__')`.

## Key Takeaways

- Iterable has `__iter__()`; iterator has `__iter__()` and `__next__()`.
- `for` loop = `iter()` + `next()` + `StopIteration`.
- Custom iterators are classes implementing the protocol.
- Iterables can be iterated many times; iterators are single-use.
- Generators are a concise way to create iterators.

## Further Reading
- [Python docs: Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)
- [Python docs: Iterator Protocol](https://docs.python.org/3/library/stdtypes.html#typeiter)
- [Real Python: Iterators and Iterables](https://realpython.com/python-iterators-iterables/)

## Next Module
Continue to **Module 040: Milestone Project: Text-Based Adventure Game Engine**.
