# Module 009: Numbers Deep Dive (Precision, the `math` module)

> **Phase:** 1. Fundamentals  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 008: String Formatting](../module-008-string-formatting/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Explain the difference between integer and float precision
- Recognize and work around floating-point imprecision
- Import and use functions from the `math` module
- Use `math.sqrt()`, `math.ceil()`, `math.floor()`, `math.pow()`, `math.pi`
- Use `round()` to control decimal places
- Describe complex numbers at a high level

## Why This Matters
Numbers are the foundation of computation. Understanding how Python stores integers vs floats — and where floats can surprise you — prevents subtle bugs. The `math` module gives you access to mathematical functions that go far beyond basic arithmetic.

## Concept Explanation

### Integer Precision

Python integers have **arbitrary precision** — they can be as large as your memory allows:

```python
small = 42
huge = 10 ** 100
print(huge)
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

You can perform arithmetic on arbitrarily large integers without overflow:

```python
factorial = 1
for i in range(1, 101):
    factorial *= i
print(factorial)  # A 158-digit number — no problem for Python!
```

### Float Precision

Floats (floating-point numbers) have **limited precision** — they are stored in 64 bits following the IEEE 754 standard. This means:

- About 15-17 significant decimal digits of precision
- Some decimal numbers cannot be represented exactly

```python
print(0.1 + 0.2)        # 0.30000000000000004 (not 0.3!)
print(0.1 + 0.2 == 0.3) # False!
```

This is not a Python bug — it's a fundamental property of binary floating-point arithmetic used by almost every programming language.

#### Working Around Float Imprecision

```python
# Use round() for display
print(round(0.1 + 0.2, 2))  # 0.3

# Use a tolerance for comparisons
tolerance = 1e-10
print(abs((0.1 + 0.2) - 0.3) < tolerance)  # True

# Use the decimal module for exact decimal arithmetic (advanced)
```

### The `round()` Function

```python
print(round(3.14159, 2))   # 3.14
print(round(3.14159, 0))   # 3.0
print(round(3.14159))      # 3 (no decimal places → int)
print(round(2.5))          # 2 (bankers' rounding!)
```

Note: Python uses "bankers' rounding" (round half to even). `round(2.5)` gives `2`, `round(3.5)` gives `4`.

### The `math` Module

The `math` module provides mathematical functions and constants. You must import it first:

```python
import math
```

#### Common Functions

```python
# Power and roots
print(math.sqrt(16))     # 4.0 (square root)
print(math.pow(2, 10))   # 1024.0 (2^10)
print(math.sqrt(2))      # 1.4142135623730951

# Rounding
print(math.ceil(3.2))    # 4 (round up)
print(math.floor(3.8))   # 3 (round down)
print(math.trunc(3.8))   # 3 (truncate toward zero)

# Constants
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045

# Logarithms and exponentials
print(math.log(100, 10)) # 2.0 (log base 10)
print(math.log(2.71828)) # ~1.0 (natural log)
print(math.exp(1))       # 2.718281828459045 (e^1)

# Trigonometry
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))            # 1.0
print(math.degrees(math.pi))  # 180.0
print(math.radians(180))      # 3.141592653589793
```

#### Comparison: `math.pow()` vs `**`

```python
print(2 ** 10)        # 1024 (int if base is int)
print(math.pow(2, 10)) # 1024.0 (always float)
```

### Complex Numbers

Python has built-in support for complex numbers. A complex number has a real and an imaginary part:

```python
z = 3 + 4j
print(z.real)    # 3.0
print(z.imag)    # 4.0
print(z * z)     # (-7+24j)
print(abs(z))    # 5.0 (magnitude: sqrt(3^2 + 4^2))
```

Complex numbers are used in engineering, physics, and scientific computing. You won't need them often in general programming, but it's good to know they exist.

### Factorial and Other Helpers

```python
print(math.factorial(5))  # 120
print(math.gcd(12, 8))    # 4
print(math.fsum([0.1, 0.2, 0.3]))  # 0.6 (accurate float sum)
```

## Common Pitfalls

1. **Comparing floats with `==`**: `0.1 + 0.2 == 0.3` is `False`. Use a tolerance with `abs()`.
2. **Forgetting to import `math`**: `math.sqrt(9)` without importing raises `NameError`.
3. **`math.pow()` returns a float**: Use `**` if you need integer results.
4. **`round(2.5)` surprises**: Python uses bankers' rounding (round half to even).
5. **Dividing integers gives a float**: `4 / 2` returns `2.0`, not `2`.
6. **Confusing `math.ceil()` and `math.floor()`**: `ceil(3.1)` is `4` (up), `floor(3.9)` is `3` (down).

## Hands-On Walkthrough

Let's build a geometry calculator:

```python
import math

print("=== Geometry Calculator ===")

# Circle
radius = 5.0
circumference = 2 * math.pi * radius
area_circle = math.pi * radius ** 2
print(f"Circle (r={radius}):")
print(f"  Circumference: {circumference:.2f}")
print(f"  Area: {area_circle:.2f}")

# Right triangle
a = 3.0
b = 4.0
c = math.sqrt(a ** 2 + b ** 2)
angle_a = math.degrees(math.atan(a / b))
angle_b = 90 - angle_a
print(f"Triangle (a={a}, b={b}):")
print(f"  Hypotenuse: {c}")
print(f"  Angles: {angle_a:.1f}°, {angle_b:.1f}°, 90°")

# Sphere
radius = 2.5
volume = 4 / 3 * math.pi * radius ** 3
surface = 4 * math.pi * radius ** 2
print(f"Sphere (r={radius}):")
print(f"  Volume: {volume:.2f}")
print(f"  Surface area: {surface:.2f}")

# Float precision demo
print()
print("=== Float Precision Demo ===")
print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3 is {0.1 + 0.2 == 0.3}")
print(f"round(0.1 + 0.2, 2) = {round(0.1 + 0.2, 2)}")
```

Expected output:
```
=== Geometry Calculator ===
Circle (r=5.0):
  Circumference: 31.42
  Area: 78.54
Triangle (a=3.0, b=4.0):
  Hypotenuse: 5.0
  Angles: 36.9°, 53.1°, 90°
Sphere (r=2.5):
  Volume: 65.45
  Surface area: 78.54

=== Float Precision Demo ===
0.1 + 0.2 = 0.30000000000000004
0.1 + 0.2 == 0.3 is False
round(0.1 + 0.2, 2) = 0.3
```

## Key Takeaways

- Integers have arbitrary precision (no overflow).
- Floats have ~15-17 significant digits; some decimals are inexact.
- Never compare floats with `==`; use `abs(a - b) < tolerance`.
- `round()` uses bankers' rounding (round half to even).
- `import math` gives access to `sqrt()`, `ceil()`, `floor()`, `pow()`, `pi`, `e`, and more.
- `math.ceil()` rounds up, `math.floor()` rounds down.
- `math.pow()` returns float; `**` returns int when both operands are ints.
- Complex numbers (`3 + 4j`) have `.real` and `.imag` parts.
- Python standard library includes `math.factorial()`, `math.gcd()`, `math.fsum()`.

## Further Reading
- [Floating Point Arithmetic: Issues and Limitations (docs.python.org)](https://docs.python.org/3/tutorial/floatingpoint.html)
- [math — Mathematical Functions (docs.python.org)](https://docs.python.org/3/library/math.html)

## Next Module
Build your first complete project in [Module 010: Milestone Project — Command-Line Calculator](../module-010-mini-project-calculator/README.md).
