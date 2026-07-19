# Module 015: Loops: `for`

> **Phase:** 2. Control Flow & Data | **Estimated time:** 2 hours | **Milestone Project:** No

## Prerequisites
- [Module 014: Loops: `while`](../module-014-while-loops/README.md)

## Learning Objectives
- Write `for` loops to iterate over sequences
- Use `range()` with start, stop, and step parameters
- Iterate over strings character by character
- Understand the `for-else` clause
- Choose between `for` and `while` loops appropriately
- Use indexing patterns with `range(len())`

## Why This Matters
The `for` loop is the most commonly used loop in Python. It's cleaner and safer than `while` for iterating over sequences because you don't have to manage a loop variable manually. Whether you're processing each character in a string, generating a sequence of numbers with `range()`, or working with collections (coming in Module 018), `for` is your go-to tool.

## Concept Explanation

### The `for` Loop

A `for` loop iterates over each item in a sequence:

```python
for item in sequence:
    # do something with item
```

The loop variable (`item`) takes each value from the sequence, one at a time:

```python
for name in ["Alice", "Bob", "Charlie"]:
    print(f"Hello, {name}!")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Iterating Over Strings

Strings are sequences of characters:

```python
word = "Python"
for letter in word:
    print(letter, end=" ")
# Output: P y t h o n
```

### The `range()` Function

`range()` generates a sequence of integers. It's commonly used with `for` loops.

**`range(stop)`** — Numbers from 0 up to (but not including) `stop`:

```python
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

**`range(start, stop)`** — Numbers from `start` to `stop - 1`:

```python
for i in range(2, 7):
    print(i, end=" ")
# Output: 2 3 4 5 6
```

**`range(start, stop, step)`** — Numbers from `start`, incrementing by `step`:

```python
for i in range(0, 10, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8

for i in range(10, 0, -2):
    print(i, end=" ")
# Output: 10 8 6 4 2
```

**Key facts about `range()`:**
- `range` is lazy — it doesn't create a list of all numbers in memory
- The stop value is **exclusive** (not included)
- Default start is 0
- Step can be negative to count downward

### `for-else`

The `else` clause after a `for` loop runs **only if the loop completed without hitting `break`**:

```python
numbers = [1, 3, 5, 7, 9]
for n in numbers:
    if n % 2 == 0:
        print(f"Found an even number: {n}")
        break
else:
    print("No even numbers found.")
# Output: No even numbers found.
```

(Detailed use of `break` comes in Module 016.)

### `for` vs `while`

| Use `for` when...                         | Use `while` when...                         |
|-------------------------------------------|---------------------------------------------|
| You know the sequence to iterate over     | The number of iterations is unknown         |
| You need to process items one by one      | You're waiting for a condition to change    |
| You want to avoid manual index management | You need a sentinel-controlled loop         |
| You're using `range()`                    | You're doing input validation               |

```python
# for loop: clean iteration over a range
for i in range(10):
    print(i)

# while loop: equivalent but more verbose
i = 0
while i < 10:
    print(i)
    i = i + 1
```

### Iterating with Index Patterns

Sometimes you need both the index and the value:

```python
word = "hello"
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")
# Output:
# Index 0: h
# Index 1: e
# Index 2: l
# Index 3: l
# Index 4: o
```

## Common Pitfalls

1. **Modifying the sequence while iterating** — Don't add or remove items from a list while looping over it (leads to skipped items). We'll cover safe patterns later.

2. **Forgetting that `range(stop)` excludes `stop`** — `range(10)` gives 0-9, not 0-10. If you need to include 10, use `range(11)`.

3. **Using `for` when input validation needs `while`** — If you're waiting for a user to enter valid input, you don't know how many tries it will take. Use `while`.

4. **Loop variable leaking after the loop** — In Python 3, the loop variable keeps its last value after the loop ends. Be aware of this.

5. **Unnecessary index tracking** — If you don't need the index, just iterate directly: `for item in sequence:` not `for i in range(len(sequence)):`.

## Hands-On Walkthrough

Let's count vowels in a string using a `for` loop:

```python
text = input("Enter some text: ")  # Assume "Hello World"
vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count = count + 1

print(f"Number of vowels: {count}")  # Number of vowels: 3
```

Now let's use `range()` to print a multiplication table:

```python
n = int(input("Which multiplication table? "))  # Assume 7

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
# Output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70
```

## Key Takeaways

- `for item in sequence:` iterates over each element in a sequence
- `range(start, stop, step)` generates integer sequences without creating a list
- `range(stop)` goes from 0 to stop-1; `range(start, stop)` goes from start to stop-1
- Strings are iterable — `for char in "hello":` works
- `for-else` runs the `else` block only if no `break` occurred
- Use `for` when iterating over sequences; use `while` when waiting for a condition
- `for i in range(len(seq)):` gives you indexes; prefer direct iteration when you don't need them

## Further Reading
- [Python docs: for statements](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)
- [Python docs: range() function](https://docs.python.org/3/library/stdtypes.html#range)
- [Real Python: Python for Loops](https://realpython.com/python-for-loop/)

## Next Module
[Module 016: Loop Control (break, continue, loop else)](../module-016-loop-control/README.md) — Take control of your loops with `break`, `continue`, and the loop `else` clause.
