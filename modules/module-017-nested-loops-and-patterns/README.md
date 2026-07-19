# Module 017: Nested Loops and Pattern Printing

> **Phase:** 2. Control Flow & Data | **Estimated time:** 2 hours | **Milestone Project:** No

## Prerequisites
- [Module 016: Loop Control (break, continue, loop else)](../module-016-loop-control/README.md)

## Learning Objectives
- Write nested `for` and `while` loops
- Print geometric patterns (rectangles, triangles, pyramids, diamonds)
- Generate multiplication tables with nested loops
- Develop intuition for O(n²) time complexity

## Why This Matters
Nested loops are essential for working with 2D data (grids, tables, matrices). Pattern printing is a classic coding exercise that builds your ability to reason about loops, conditions, and spacing. It's also common in technical interviews — and it's genuinely satisfying to create visual output from logic.

## Concept Explanation

### Nested Loops

A nested loop is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop:

```python
for i in range(3):
    for j in range(4):
        print(f"({i},{j})", end=" ")
    print()
# Output:
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
```

The outer loop runs 3 times; each time, the inner loop runs 4 times — that's 3 × 4 = 12 total iterations.

### Printing Rectangles

```python
rows = 3
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
# Output:
# *****
# *****
# *****
```

`end=""` keeps the print on the same line; the empty `print()` after the inner loop moves to the next line.

### Printing Triangles

**Right triangle (increasing stars):**

```python
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
# *****
```

The inner loop runs `i` times on the `i`-th row — row 1 has 1 star, row 2 has 2 stars, etc.

**Inverted right triangle:**

```python
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *****
# ****
# ***
# **
# *
```

### Printing Pyramids

```python
n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Output:
#     *
#    ***
#   *****
#  *******
# *********
```

Spaces decrease as you go down; stars increase as `2*i - 1`.

### Printing a Diamond

```python
n = 5
# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

### Multiplication Tables

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()
```

Use format specifiers (`:2`) to align columns.

### Time Complexity Intuition (O(n²))

If you have two nested loops, each running `n` times, the inner body runs `n × n = n²` times:

```python
n = 1000
operations = 0
for i in range(n):
    for j in range(n):
        operations = operations + 1
print(f"Operations: {operations}")  # Operations: 1000000
```

When `n` doubles, the work quadruples. This is O(n²) — acceptable for small `n`, but slow for large inputs.

## Common Pitfalls

1. **Swapping row and column variables** — Keep `i` for outer (rows) and `j` for inner (columns) by convention.

2. **Wrong inner loop range** — If the inner loop condition doesn't reference the outer variable, you won't get the triangular shape.

3. **Forgetting the newline** — After the inner loop finishes, you need `print()` to move to the next line.

4. **Hardcoding sizes** — Store dimensions in variables (`n = 5`) so you can change them easily.

5. **Not aligning numbers** — Without formatting, numbers of different widths produce jagged output.

## Hands-On Walkthrough

Let's print a number pyramid:

```python
n = 5
for i in range(1, n + 1):
    # Leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
# Output:
#     1
#    121
#   12321
#  1234321
# 123454321
```

Now let's make a checkerboard:

```python
size = 4
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
# Output:
# ■ □ ■ □
# □ ■ □ ■
# ■ □ ■ □
# □ ■ □ ■
```

## Key Takeaways

- The outer loop runs the inner loop multiple times: total iterations = outer × inner
- Nested loops produce 2D output: the outer loop controls rows, the inner loop controls columns
- Triangular patterns use an inner loop range that depends on the outer variable
- Pyramids and diamonds need separate loops for spaces and stars/numbers
- Multiplication tables are a classic nested-loop application
- O(n²) complexity: doubling the input quadruples the work
- Use `end=""` to stay on the same line; call `print()` after the inner loop for a newline

## Further Reading
- [Real Python: Nested Loops in Python](https://realpython.com/python-nested-loops/)
- [Python docs: More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Big O Notation Explained](https://www.bigocheatsheet.com/)

## Next Module
[Module 018: Lists: Basics](../module-018-lists-basics/README.md) — Start working with Python's most versatile data structure: the list.
