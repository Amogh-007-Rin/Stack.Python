# Module 008: String Formatting (f-strings, format, %)

> **Phase:** 1. Fundamentals  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 007: Strings Deep Dive](../module-007-strings-deep-dive/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Embed expressions directly in strings using f-strings
- Use the `.format()` method for advanced formatting
- Recognize and use old-style `%` formatting
- Apply format specifiers for numbers (`:.2f`, `:d`, `:.0f`)
- Control alignment and padding in formatted output

## Why This Matters
Clean, readable string formatting is essential for user-facing output, reports, log messages, and debugging. f-strings — the modern Python approach — make your code shorter, clearer, and less error-prone.

## Concept Explanation

### f-strings (Python 3.6+)

f-strings let you embed expressions directly inside string literals. Prefix the string with `f` or `F`, and use `{expression}` placeholders:

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.
```

You can put any expression inside the braces:

```python
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
# Output: 5 + 3 = 8

print(f"Temperature: {25 * 9/5 + 32}°F")
# Output: Temperature: 77.0°F
```

#### Format Specifiers in f-strings

Use `{variable:specifier}` after a colon:

```python
price = 49.9567
print(f"Price: ${price:.2f}")    # Price: $49.96 (2 decimal places)
print(f"Price: ${price:.0f}")    # Price: $50 (rounded to integer)

count = 42
print(f"Count: {count:d}")       # Count: 42 (integer)

percent = 0.8567
print(f"Score: {percent:.1%}")   # Score: 85.7% (percentage)
```

#### Alignment and Padding

```python
value = 42
print(f"|{value:<10}|")   # Left-align in 10 chars: |42        |
print(f"|{value:>10}|")   # Right-align in 10 chars: |        42|
print(f"|{value:^10}|")   # Center in 10 chars: |    42    |
print(f"|{value:*^10}|")  # Center with * fill: |****42****|
```

### The `.format()` Method

Before f-strings, `.format()` was the primary modern approach. It still appears in older code:

```python
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 30 years old.
```

Positional and keyword arguments:

```python
print("{0} is {1} years old. {0} likes Python.".format(name, age))
# Alice is 30 years old. Alice likes Python.

print("{name} is {age} years old.".format(name="Bob", age=25))
# Bob is 25 years old.
```

Format specifiers work the same way:

```python
pi = 3.14159
print("Pi is approximately {:.2f}".format(pi))
# Pi is approximately 3.14
```

### Old-Style `%` Formatting

Inspired by C's `printf`. You still see this in legacy code:

```python
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# My name is Alice and I am 30 years old.
```

Common placeholders: `%s` (string), `%d` (integer), `%f` (float):

```python
price = 49.9567
print("Price: $%.2f" % price)    # Price: $49.96
print("Percent: %.1f%%" % 85.67) # Percent: 85.7%
```

### Comparison of Approaches

| Feature | f-string | `.format()` | `%`-formatting |
|---------|----------|-------------|----------------|
| Introduced | 3.6 | 2.6 | 0.x (original) |
| Readability | Best | Good | Moderate |
| Performance | Fastest | Fast | Fast |
| Expression embedding | Yes | Limited | No |
| Recommended for new code | **Yes** | Legacy | Legacy |

### Format Specifier Reference

```
:[fill]align][sign][width][.precision][type]
```

align: `<` left, `>` right, `^` center
sign: `+` always show, `-` only negative, ` ` space for positive
width: minimum field width
.precision: decimal places for float
type: `d` integer, `f` float, `%` percentage, `e` scientific

```python
n = -1234.5678
print(f"{n:+.2f}")      # -1234.57
print(f"{n:*>+15.2f}")  # ******-1234.57
```

## Common Pitfalls

1. **Forgetting the `f` prefix**: `"{name}"` prints the literal text `{name}`, not the value. Always prefix with `f`.
2. **Mixing f-string curly braces with JSON/dicts**: `f"{'key': value}"` confuses the parser. Use variables or nested quotes.
3. **Using `%` for multiple values without a tuple**: `"%.2f %s" % (price, name)` — the right side must be a tuple with multiple values.
4. **Not escaping `%` in `%`-formatting**: To print a literal `%`, use `%%`.
5. **Over-specifying**: `f"{x:.2f}"` on an integer works but outputs `3.00`. Use `{x:d}` for integers.

## Hands-On Walkthrough

Let's build an invoice formatter:

```python
# Store data
item = "Widget A"
quantity = 5
unit_price = 12.345
tax_rate = 0.08

# Calculate totals
subtotal = quantity * unit_price
tax = subtotal * tax_rate
total = subtotal + tax

# Print invoice using f-strings (recommended)
print("=== INVOICE ===")
print(f"{'Item':<15} {'Qty':>5} {'Price':>8} {'Total':>8}")
print("-" * 36)
print(f"{item:<15} {quantity:>5} ${unit_price:>6.2f} ${subtotal:>6.2f}")
print()
print(f"{'Subtotal:':>20} ${subtotal:>7.2f}")
print(f"{'Tax (8%):':>20} ${tax:>7.2f}")
print(f"{'Total:':>20} ${total:>7.2f}")

# Same output with .format()
print()
print("=== Same with .format() ===")
print("{:<15} {:>5} {:>8} {:>8}".format("Item", "Qty", "Price", "Total"))
print("-" * 36)
print("{:<15} {:>5} ${:>6.2f} ${:>6.2f}".format(item, quantity, unit_price, subtotal))
```

Example output:
```
=== INVOICE ===
Item              Qty    Price     Total
------------------------------------
Widget A            5 $ 12.35 $  61.73

           Subtotal: $   61.73
           Tax (8%): $    4.94
              Total: $   66.67
```

## Key Takeaways

- f-strings: prefix with `f`, embed with `{}`.
- Format specifiers: `{value:width.precision type}`.
- `.format()` method: `"{} {}".format(a, b)` — still common in older code.
- `%`-formatting: `"%s %d" % (string, int)` — legacy style.
- Alignment: `<` left, `>` right, `^` center.
- Number formatting: `:.2f` for 2 decimals, `:d` for integer, `:.1%` for percent.
- Use padding characters: `{value:*>10}` fills with `*`.
- f-strings are the modern, recommended approach for new Python code.

## Further Reading
- [PEP 498 — Literal String Interpolation (f-strings)](https://peps.python.org/pep-0498/)
- [Format String Syntax (docs.python.org)](https://docs.python.org/3/library/string.html#format-string-syntax)
- [PyFormat.info — Practical examples](https://pyformat.info/)

## Next Module
Dive deeper into numbers in [Module 009: Numbers Deep Dive](../module-009-numbers-deep-dive/README.md).
