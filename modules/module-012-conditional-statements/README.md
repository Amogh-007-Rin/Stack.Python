# Module 012: Conditional Statements (if / elif / else)

> **Phase:** 2. Control Flow & Data | **Estimated time:** 2 hours | **Milestone Project:** No

## Prerequisites
- [Module 011: Booleans and Truthiness](../module-011-booleans-and-truthiness/README.md)

## Learning Objectives
- Write `if` statements to execute code conditionally
- Use `elif` and `else` to handle multiple branches
- Properly indent code blocks
- Nest conditionals inside each other
- Use truthiness directly in conditions
- Check for `None`, empty strings, and other common patterns

## Why This Matters
Conditional statements are how programs make decisions. Without them, code runs the same way every time. With `if`/`elif`/`else`, your program can react to user input, validate data, and handle different scenarios — the essence of intelligent behavior.

## Concept Explanation

### The `if` Statement

An `if` statement runs a block of code only when its condition is truthy:

```python
age = 18
if age >= 18:
    print("You are an adult.")
    print("You can vote.")
# Output: You are an adult.
# Output: You can vote.
```

The condition is any expression that Python evaluates for truthiness. The **indented block** (4 spaces by convention) runs only if the condition is `True`.

```python
age = 16
if age >= 18:
    print("You are an adult.")  # This does NOT run
print("This runs either way.")
# Output: This runs either way.
```

### The `else` Clause

Add `else` to run code when the condition is falsy:

```python
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Output: You are a minor.
```

### The `elif` Clause

Use `elif` (short for "else if") for multiple conditions:

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")
# Output: Grade: B
```

Only the **first** matching branch runs. Once a condition is `True`, Python skips the remaining `elif` and `else` blocks.

### Indentation

Python uses indentation (4 spaces recommended) to define code blocks. Consistent indentation is mandatory:

```python
x = 10
if x > 5:
    print("x is greater than 5")    # 4 spaces
    if x > 8:
        print("x is also > 8")      # 8 spaces (nested)
print("Outside the if block")       # 0 spaces
```

### Truthiness in Conditions

You don't need `if x == True:`. Just use `if x:`:

```python
name = input("Enter your name: ")  # User types "" (empty)
if name:
    print(f"Hello, {name}!")
else:
    print("No name entered.")
# Output: No name entered.
```

### Checking for `None`

The idiomatic way to check for `None`:

```python
result = None
if result is None:
    print("No result yet.")
else:
    print(f"Result: {result}")
# Output: No result yet.
```

Use `is None` rather than `== None`. The `is` operator checks identity, which is the correct way to compare to `None`.

### Checking for Empty Strings

```python
text = ""
if not text:
    print("String is empty.")
# Output: String is empty.
```

### Nested Conditionals

You can put `if` statements inside other `if` statements:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("Get a license first.")
else:
    print("Too young to drive.")
# Output: You can drive.
```

## Common Pitfalls

1. **Forgetting the colon** — Every `if`, `elif`, and `else` line must end with a colon (`:`).

2. **Inconsistent indentation** — Mixing tabs and spaces, or using the wrong number of spaces, causes `IndentationError`.

3. **Using assignment `=` instead of comparison `==`** — Python 3.12 allows `=` in conditions, but it's almost certainly a bug if you meant `==`.

4. **Putting too many conditions in `elif`** — Remember that once a condition matches, later `elif` branches are skipped, even if they would also match.

5. **Empty `if` block** — Python won't let you leave a block empty. Use `pass` as a placeholder:

```python
if condition:
    pass  # I'll fill this in later
```

## Hands-On Walkthrough

Let's build a simple number guessing game using conditionals:

```python
import random

secret = random.randint(1, 10)
guess = int(input("Guess a number 1-10: "))  # Assume user types 7

if guess == secret:
    print("Perfect! You guessed it!")
elif guess > secret:
    print("Too high! Try again.")
else:
    print("Too low! Try again.")

print(f"The secret number was {secret}.")
```

Now a temperature checker with nested conditions:

```python
temp = float(input("Enter temperature in °C: "))  # Assume 30

if temp > 30:
    print("It's hot outside!")
elif temp > 20:
    print("It's warm and pleasant.")
elif temp > 10:
    print("It's a bit cool.")
elif temp > 0:
    print("It's cold!")
else:
    print("It's freezing! Stay inside.")
```

## Key Takeaways

- `if` runs a block when its condition is truthy; `else` provides the fallback
- `elif` adds additional conditions — only the first matching branch executes
- Indentation (4 spaces) defines blocks; all lines in a block must be indented consistently
- Use `if x:` for truthiness checks instead of `if x == True:`
- Use `if x is None:` to check for `None` (identity, not equality)
- Use `if not x:` to check for empty strings, empty collections, or zero values
- Nested conditionals let you check multiple layers of conditions
- Every `if`, `elif`, `else` line must end with a colon

## Further Reading
- [Python docs: More Control Flow Tools — if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [PEP 8 — Indentation guidelines](https://peps.python.org/pep-0008/#indentation)
- [Real Python: Conditional Statements in Python](https://realpython.com/python-conditional-statements/)

## Next Module
[Module 013: Comparison Chaining & Logical Operators Deep Dive](../module-013-comparison-chaining-and-logic/README.md) — Master chained comparisons like `1 < x < 10`, understand `is` vs `==`, and learn De Morgan's laws.
