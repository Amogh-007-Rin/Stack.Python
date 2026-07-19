# Module 006: Operators (Arithmetic, Comparison, Logical, Assignment)

> **Phase:** 1. Fundamentals  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 005: Basic Input and Output](../module-005-basic-input-and-output/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Use all arithmetic operators including `//`, `%`, and `**`
- Compare values using `==`, `!=`, `<`, `>`, `<=`, `>=`
- Combine conditions with `and`, `or`, `not`
- Use augmented assignment operators like `+=`, `-=`
- Predict evaluation order using operator precedence

## Why This Matters
Operators are the tools you use to compute, compare, and control. Every program — from a simple calculator to a complex AI model — relies on these fundamental operations. Mastering them gives you the vocabulary to express any computation.

## Concept Explanation

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (float) | `5 / 3` | `1.666...` |
| `//` | Floor division | `5 // 3` | `1` |
| `%` | Modulo (remainder) | `5 % 3` | `2` |
| `**` | Exponentiation | `5 ** 3` | `125` |

#### Floor Division (`//`)
Divides and rounds DOWN to the nearest integer:

```python
print(10 // 3)    # 3
print(-10 // 3)   # -4 (rounds DOWN, not toward zero)
print(10.0 // 3)  # 3.0 (float if any operand is float)
```

#### Modulo (`%`)
Returns the remainder after division. Useful for checking even/odd:

```python
print(10 % 3)     # 1
print(15 % 5)     # 0 (divisible)
print(7 % 2)      # 1 (odd)
print(8 % 2)      # 0 (even)
```

#### Exponentiation (`**`)
Raises a number to a power:

```python
print(2 ** 3)      # 8
print(4 ** 0.5)    # 2.0 (square root)
print(10 ** -1)    # 0.1
```

### Comparison Operators

Comparison operators return `True` or `False` (boolean):

```python
x = 10
y = 5

print(x == y)    # False (equal to)
print(x != y)    # True (not equal to)
print(x < y)     # False
print(x > y)     # True
print(x <= 10)   # True
print(x >= 10)   # True
```

You can chain comparisons:

```python
age = 25
print(18 <= age < 65)  # True (age is between 18 and 64 inclusive)
```

### Logical Operators

`and`, `or`, `not` combine boolean values:

```python
age = 20
has_id = True

print(age >= 18 and has_id)   # True (both conditions True)
print(age >= 18 or has_id)    # True (at least one is True)
print(not has_id)             # False (negates)
```

Truth table for `and`:
```
True  and True   → True
True  and False  → False
False and True   → False
False and False  → False
```

Truth table for `or`:
```
True  or True    → True
True  or False   → True
False or True    → True
False or False   → False
```

### Assignment Operators

Beyond simple `=`, Python provides **augmented assignment** operators:

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

```python
count = 10
count += 5    # count is now 15
count -= 3    # count is now 12
count *= 2    # count is now 24
print(count)
```

### Operator Precedence

Python follows the standard PEMDAS order. From highest to lowest precedence:

1. `**` (exponentiation)
2. `+x`, `-x` (unary plus/minus)
3. `*`, `/`, `//`, `%` (multiplication, division)
4. `+`, `-` (addition, subtraction)
5. `==`, `!=`, `<`, `>`, `<=`, `>=` (comparison)
6. `not` (logical NOT)
7. `and` (logical AND)
8. `or` (logical OR)

```python
result = 5 + 3 * 2 ** 3
# 2 ** 3 → 8
# 3 * 8 → 24
# 5 + 24 → 29
print(result)  # 29
```

Use parentheses to make precedence explicit:

```python
result = (5 + 3) * 2 ** 3  # 8 * 8 → 64
print(result)  # 64
```

## Common Pitfalls

1. **`/` vs `//`**: `10 / 3` is `3.333...`, `10 // 3` is `3`. Know the difference.
2. **`==` vs `=`**: `if x = 5` is an assignment, not a comparison. Use `==` for equality checks.
3. **Chaining `and`/`or` without parentheses**: `age > 18 and has_id or is_vip` may not mean what you think. Use parentheses: `(age > 18 and has_id) or is_vip`.
4. **Forgetting that `%` with negative numbers can surprise you**: `-5 % 3` gives `1`, not `-2`.
5. **Integer division with negatives**: `-10 // 3` gives `-4` (floor division rounds down).

## Hands-On Walkthrough

Let's build a "Number Analyzer" program:

```python
# Get a number from the user
num = int(input("Enter an integer: "))

# Arithmetic
print("Square:", num ** 2)
print("Cube:", num ** 3)
print("Square root (approx):", num ** 0.5)

# Even or odd?
print("Is even?", num % 2 == 0)

# Analysis
print("Positive?", num > 0)
print("Negative?", num < 0)
print("Zero?", num == 0)

# Range check
print("Between 1 and 100?", 1 <= num <= 100)

# Augmented assignment demo
total = 0
total += num
total += 10
print("Total after adding num and 10:", total)
```

Example run with input `7`:
```
Square: 49
Cube: 343
Square root (approx): 2.6457513110645907
Is even? False
Positive? True
Negative? False
Zero? False
Between 1 and 100? True
Total after adding num and 10: 17
```

## Key Takeaways

- Arithmetic: `+`, `-`, `*`, `/`, `//` (floor), `%` (modulo), `**` (power).
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=` — all return `bool`.
- Logical: `and` (both True), `or` (at least one True), `not` (negation).
- Augmented assignment: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
- Operator precedence: `**` > unary > `*`/`/`/`//`/`%` > `+`/`-` > comparison > `not` > `and` > `or`.
- Use parentheses to clarify precedence.
- `//` rounds down (floor), not toward zero.
- `%` gives remainder; `x % 2 == 0` checks for even numbers.

## Further Reading
- [Python Operators (docs.python.org)](https://docs.python.org/3/library/operator.html)
- [Operator Precedence (docs.python.org)](https://docs.python.org/3/reference/expressions.html#operator-precedence)

## Next Module
Dive deeper into text manipulation in [Module 007: Strings Deep Dive](../module-007-strings-deep-dive/README.md).
