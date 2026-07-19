# Module 035: Recursion

> **Phase:** 4. Functions  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- Module 031 (Functions: Basics)
- Module 033 (Scope and Namespaces)

## Learning Objectives
By the end of this module, you will be able to:
- Write recursive functions with a base case and recursive case
- Implement factorial and Fibonacci recursively
- Compare recursion vs iteration
- Understand Python's recursion stack depth limit
- Visualize recursion trees
- Explain the concept of tail recursion

## Why This Matters
Recursion is a powerful technique for problems that have a self-similar structure (trees, graphs, divide-and-conquer algorithms). Understanding recursion deepens your grasp of function calls and the call stack.

## Concept Explanation

### What is Recursion?

A function is **recursive** if it calls itself. Every recursive function needs:

1. **Base case** — stops the recursion.
2. **Recursive case** — calls itself with a smaller or simpler input.

### Factorial Example

```python
def factorial(n: int) -> int:
    """Calculate n! recursively.

    Args:
        n: A non-negative integer

    Returns:
        n! (n factorial)
    """
    if n <= 1:
        return 1          # base case
    return n * factorial(n - 1)  # recursive case
```

### Recursion Tree for factorial(4)

```
factorial(4)
    │
    └── 4 * factorial(3)
              │
              └── 3 * factorial(2)
                        │
                        └── 2 * factorial(1)
                                  │
                                  └── 1  (base case)
```

### Fibonacci Example

```python
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.

    Args:
        n: Position in Fibonacci sequence

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Code style | Elegant, declarative | Explicit loop control |
| Memory | Uses call stack (risk of overflow) | Usually O(1) extra space |
| Performance | Slightly slower (function call overhead) | Faster |
| Best for | Tree/graph traversal, divide-and-conquer | Simple linear tasks |

### Stack Depth Limits

Python limits recursion depth (default ~1000) to prevent stack overflow:

```python
import sys
print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(2000)     # increase (not recommended for production)
```

### Tail Recursion (Concept)

A recursive call is **tail-recursive** if it's the last operation in the function. Python does NOT optimize tail recursion, but the concept is important:

```python
def factorial_tail(n: int, acc: int = 1) -> int:
    """Tail-recursive factorial (conceptual — Python doesn't optimize)."""
    if n <= 1:
        return acc
    return factorial_tail(n - 1, acc * n)
```

## Common Pitfalls

1. **Missing base case** — infinite recursion leads to `RecursionError`.
2. **Base case never reached** — make sure input shrinks toward the base case.
3. **Stack overflow** — Python's recursion limit is ~1000; use iteration for deep recursion.
4. **Inefficient recursion** — Fibonacci without memoization is exponential (O(2^n)).

## Hands-On Walkthrough

1. Write `factorial(n)` recursively and test with n=5.
2. Write `fibonacci(n)` recursively and test with n=10.
3. Write a recursive `countdown(n)` function that prints n, then calls itself with n-1.
4. Use a loop to see at what n you get a RecursionError.

## Key Takeaways

- Recursion = base case + recursive case.
- The call stack grows with each recursive call.
- Python has a recursion limit (~1000).
- Not all problems are best solved recursively — consider iteration for deep recursion.
- Tail recursion is a concept; Python doesn't optimize it.

## Further Reading
- [Python docs: Recursion](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)
- [Real Python: Recursion in Python](https://realpython.com/python-recursion/)

## Next Module
Continue to **Module 036: Higher-Order Functions (map, filter, reduce)**.
