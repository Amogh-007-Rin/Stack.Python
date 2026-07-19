# Module 018: Lists: Basics

> **Phase:** 2. Control Flow & Data | **Estimated time:** 2 hours | **Milestone Project:** No

## Prerequisites
- [Module 017: Nested Loops and Pattern Printing](../module-017-nested-loops-and-patterns/README.md)

## Learning Objectives
- Create lists with square brackets and `list()`
- Store heterogeneous elements in a list
- Access elements with positive and negative indexing
- Slice lists to extract sublists
- Use `len()` to get the list length
- Concatenate (`+`) and repeat (`*`) lists
- Check membership with `in`
- Iterate over lists with `for` loops
- Create and access nested lists

## Why This Matters
Lists are the most fundamental data structure in Python. Unlike strings (which are sequences of characters), lists can hold any type of data — numbers, strings, other lists, or a mix. They're mutable (changeable), flexible, and used everywhere: from storing user input to representing data sets and building complex data structures.

## Concept Explanation

### Creating Lists

Lists are created with square brackets `[]`:

```python
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
```

You can also use the `list()` constructor:

```python
chars = list("hello")
print(chars)  # ['h', 'e', 'l', 'l', 'o']
```

### Heterogeneous Elements

Lists can hold different types in the same list:

```python
info = ["Alice", 28, 5.6, True]
print(info)  # ['Alice', 28, 5.6, True]
```

### Indexing (Positive and Negative)

Access elements by their position (0-indexed):

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[-1])  # date   (last element)
print(fruits[-2])  # cherry (second-to-last)
```

Positive index: 0 is first, length-1 is last.
Negative index: -1 is last, -length is first.

### Slicing

Extract a portion of a list with `list[start:stop:step]`:

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:6])     # [2, 3, 4, 5]
print(nums[:4])      # [0, 1, 2, 3]     (start defaults to 0)
print(nums[6:])      # [6, 7, 8, 9]     (stop defaults to end)
print(nums[::2])     # [0, 2, 4, 6, 8]  (every 2nd)
print(nums[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  (reversed)
```

Slicing returns a **new list** — it doesn't modify the original.

### `len()` — List Length

```python
colors = ["red", "green", "blue"]
print(len(colors))  # 3
```

### Concatenation (`+`) and Repetition (`*`)

```python
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)       # [1, 2, 3, 4, 5, 6]
print(a * 3)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print([0] * 5)     # [0, 0, 0, 0, 0]
```

### Membership with `in`

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("grape" not in fruits)  # True
```

### Iterating with `for`

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())
# Output:
# APPLE
# BANANA
# CHERRY
```

### Index iteration pattern:

```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

### Nested Lists

Lists can contain other lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])      # [1, 2, 3]     (first row)
print(matrix[1][2])   # 6             (row 1, column 2)
```

Iterating over nested lists:

```python
for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## Common Pitfalls

1. **Index out of range** — Accessing an index equal to or greater than `len(list)` raises `IndexError`. Always check `len()` first.

2. **Confusing negative indexing** — `-0` is the same as `0` (first element). There's no negative zero index.

3. **Shallow copies with slicing confusion** — `new_list = old_list[:]` creates a shallow copy. For simple lists of numbers/strings, this is fine but be aware of it for nested lists.

4. **Modifying a list while iterating** — Adding or removing elements during a `for` loop causes skipped items or `IndexError`. We'll cover safe patterns later.

5. **Using `+` to build large lists incrementally** — Each `+` creates a new list. For large data, use `.append()` (covered in Module 019).

## Hands-On Walkthrough

Let's build a simple grade tracker with lists:

```python
grades = []
num_students = int(input("How many students? "))  # Assume 3

for i in range(num_students):
    grade = float(input(f"Enter grade for student {i + 1}: "))
    grades.append(grade)

print(f"Grades: {grades}")
print(f"Average: {sum(grades) / len(grades):.1f}")
print(f"Highest: {max(grades)}")
print(f"Lowest: {min(grades)}")
```

Now let's work with a tic-tac-toe board using nested lists:

```python
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

board[0][0] = "X"
board[1][1] = "O"
board[2][2] = "X"

for row in board:
    print("|" + "|".join(row) + "|")
# Output:
# |X| | |
# | |O| |
# | | |X|
```

## Key Takeaways

- Lists are created with `[]` and can hold any mix of data types
- Indexing starts at 0; negative indices count from the end (-1 is last)
- Slicing (`list[start:stop:step]`) creates a new sublist
- `len()` returns the number of elements
- `+` concatenates two lists; `*` repeats a list
- `in` checks membership; `for x in list:` iterates
- Lists are **mutable** — you can change elements with assignment: `list[0] = new_value`
- Nested lists model 2D data like matrices and grids

## Further Reading
- [Python docs: Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python docs: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Real Python: Python Lists](https://realpython.com/python-lists-tuples/)

## Next Module
[Module 019: Lists: Methods & Comprehensions](../module-019-lists-methods-and-comprehensions/README.md) — Learn powerful list methods and the elegant list comprehension syntax.
