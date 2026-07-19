# Module 005: Basic Input and Output

> **Phase:** 1. Fundamentals  |  **Estimated time:** 1.5 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 004: Type Conversion and Casting](../module-004-type-conversion-and-casting/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Get text input from the user using `input()`
- Print dynamic output that includes user-provided values
- Convert string input to numeric types for calculation
- Build a simple interactive program

## Why This Matters
Programs that only display fixed output are boring. The `input()` function is your gateway to building interactive applications — from simple Q&A scripts to games, calculators, and data-entry tools.

## Concept Explanation

### The `input()` Function

`input()` pauses the program and waits for the user to type something and press Enter. Whatever the user types is returned as a **string**:

```python
name = input()
print("Hello,", name)
```

You can pass a **prompt string** to `input()` that is displayed to the user:

```python
name = input("What is your name? ")
print("Nice to meet you,", name)
```

### What `input()` Returns

**`input()` always returns a string.** Even if the user types a number:

```python
age = input("How old are you? ")
print(age, type(age))  # e.g., 25 <class 'str'>
```

If you need a number, you must convert it yourself using `int()` or `float()`:

```python
age = int(input("How old are you? "))
print("Next year you'll be", age + 1)
```

### Combining Input with Print

You can build sentences using f-string style (we'll cover f-strings properly in Module 008) or by passing multiple arguments to `print()`:

```python
name = input("Enter your name: ")
color = input("Enter your favorite color: ")
print(name, "likes", color)
```

### Simple Interactive Programs

A simple calculator using input:

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
```

### The End of Input

When running in a terminal, `input()` waits forever until the user types something. In a Jupyter notebook, you may need to run code cells that simulate input differently (see the notebook).

## Common Pitfalls

1. **Forgetting that `input()` returns a string**: `input() + 5` causes `TypeError`. Convert to `int` or `float` first.
2. **Not stripping whitespace**: `input()` preserves leading/trailing spaces. Use `.strip()` to clean input.
3. **Using `input()` in an online/notebook environment**: Some environments don't support interactive input. Use a simulated approach or pass the prompt carefully.
4. **Assuming the prompt needs a newline**: `input()` does not add a newline after the prompt. Add a space at the end of your prompt string for readability.
5. **Chaining conversions unsafely**: `int(input())` raises `ValueError` if the user types non-numeric text. We'll learn error handling for this in a later module.

## Hands-On Walkthrough

Let's build a simple "Personal Greeting" program:

```python
# Ask for user's details
name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Which city do you live in? ")

# Generate a personalized message
print()
print("Hello,", name + "!")
print("You are", age, "years old and live in", city + ".")
print("In 5 years, you will be", age + 5, "years old.")
```

Example run:
```
What is your name? Alice
How old are you? 30
Which city do you live in? London

Hello, Alice!
You are 30 years old and live in London.
In 5 years, you will be 35 years old.
```

Now let's build an interest calculator:

```python
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as %, e.g. 5 for 5%): "))
years = int(input("Number of years: "))

interest = principal * (rate / 100) * years
total = principal + interest

print("Interest earned:", interest)
print("Total after", years, "years:", total)
```

## Key Takeaways

- `input()` reads a line of text from the user as a string.
- Always convert numeric input with `int()` or `float()` before doing math.
- `input()` accepts an optional prompt string.
- Combine `input()` and `print()` for interactive programs.
- Use `.strip()` to clean whitespace from input.
- `input()` returns a string regardless of what the user types.
- Prompt strings should end with a space for readability.
- Simple interactive programs follow: input → process → output.

## Further Reading
- [Built-in Functions: input() (docs.python.org)](https://docs.python.org/3/library/functions.html#input)
- [Printing and Input (docs.python.org)](https://docs.python.org/3/tutorial/introduction.html#an-informal-introduction-to-python)

## Next Module
Learn the building blocks of computation in [Module 006: Operators](../module-006-operators/README.md).
