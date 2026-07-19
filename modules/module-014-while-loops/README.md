# Module 014: Loops: `while`

> **Phase:** 2. Control Flow & Data | **Estimated time:** 2 hours | **Milestone Project:** No

## Prerequisites
- [Module 013: Comparison Chaining & Logical Operators Deep Dive](../module-013-comparison-chaining-and-logic/README.md)

## Learning Objectives
- Write `while` loops with proper conditions
- Avoid and escape infinite loops
- Use `while` loops for input validation
- Implement sentinel-controlled loops
- Apply the accumulator pattern (summing, counting)

## Why This Matters
Loops let you repeat work without writing the same code over and over. The `while` loop is the most flexible loop — it keeps going as long as a condition holds true. You'll use it for input validation (keep asking until you get valid input), game loops, and any situation where you don't know in advance how many iterations you need.

## Concept Explanation

### The `while` Loop

A `while` loop repeats a block of code as long as its condition is truthy:

```python
count = 0
while count < 3:
    print(f"Count is {count}")
    count = count + 1
# Output:
# Count is 0
# Count is 1
# Count is 2
```

**Flow:**
1. Check the condition (`count < 3`)
2. If truthy, run the indented block
3. Go back to step 1
4. If falsy, skip the block and continue

### The Loop Variable

The variable in the condition must change inside the loop, or the loop will run forever:

```python
# This loop will terminate because `i` changes each time
i = 1
while i <= 5:
    print(i)
    i = i + 1
# Output: 1 2 3 4 5
```

### Infinite Loops

An infinite loop occurs when the condition never becomes falsy:

```python
# DANGER: Infinite loop!
# i = 1
# while i > 0:
#     print(i)
#     i = i + 1  # i keeps growing, always > 0
```

If you run an infinite loop in a terminal, press **Ctrl+C** to stop it.

Ways to avoid infinite loops:
- Ensure the condition variable changes toward the exit condition
- Add a maximum iteration counter as a safety net
- Use `break` (covered in Module 016)

### Input Validation with `while`

A common pattern: keep asking for input until you get something valid:

```python
age = None
while age is None:
    user_input = input("Enter your age: ")
    if user_input.isdigit():
        age = int(user_input)
    else:
        print("Invalid input. Please enter a number.")

print(f"You are {age} years old.")
```

### Sentinel Values

A sentinel is a special value that signals "stop":

```python
total = 0
print("Enter numbers to sum. Enter -1 to stop.")

num = int(input("Enter a number: "))
while num != -1:
    total = total + num
    num = int(input("Enter a number: "))

print(f"Total: {total}")
```

### The Accumulator Pattern

Build up a result inside a loop:

**Summing:**

```python
total = 0      # accumulator starts at 0 for sums
i = 1
while i <= 100:
    total = total + i
    i = i + 1
print(f"Sum of 1 to 100: {total}")  # Sum of 1 to 100: 5050
```

**Counting:**

```python
count = 0      # accumulator starts at 0 for counts
i = 1
while i <= 100:
    if i % 2 == 0:
        count = count + 1
    i = i + 1
print(f"Count of even numbers 1-100: {count}")  # Count of even numbers 1-100: 50
```

**Product (multiplication):**

```python
product = 1    # accumulator starts at 1 for products
i = 1
while i <= 5:
    product = product * i
    i = i + 1
print(f"5! = {product}")  # 5! = 120
```

## Common Pitfalls

1. **Forgetting to update the loop variable** — This causes an infinite loop. Always ensure the condition will eventually become falsy.

2. **Off-by-one errors** — If you need exactly N iterations, double-check your condition. `while i < N` runs N times (i = 0, 1, ..., N-1). `while i <= N` runs N+1 times.

3. **Using `=` instead of `==` in the condition** — `while x = 5` is an assignment (which Python 3.12 disallows in this context), not a comparison.

4. **Not handling invalid input** — If `int()` receives non-numeric input, the program crashes with a `ValueError`. Always validate before converting.

5. **Starting accumulator with wrong value** — Sums start at 0, products start at 1. Starting a product at 0 gives 0 every time.

## Hands-On Walkthrough

Let's build a guessing game with input validation:

```python
import random

secret = random.randint(1, 100)
guess = None
attempts = 0

while guess != secret:
    user_input = input("Guess the number (1-100): ")
    if user_input.isdigit():
        guess = int(user_input)
        attempts = attempts + 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
    else:
        print("Please enter a valid number.")

print(f"Correct! You got it in {attempts} attempts.")
```

Now a calculator loop using sentinel:

```python
print("Simple Calculator")
print("Enter 'q' to quit.")

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input == 'q':
        break
    if user_input.isdigit():
        num = int(user_input)
        total = total + num if 'total' in dir() else num
        print(f"Running total: {total}")
    else:
        print("Invalid input.")
```

## Key Takeaways

- `while condition:` repeats the indented block as long as the condition is truthy
- Update the loop variable inside the body to avoid infinite loops
- Press Ctrl+C to interrupt a runaway loop
- Use sentinel values to signal loop termination
- The accumulator pattern: initialize before the loop, update inside the loop
- Sum accumulators start at 0; product accumulators start at 1
- Always validate user input before converting with `int()` or `float()`
- `while` is ideal when you don't know the number of iterations in advance

## Further Reading
- [Python docs: while statements](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [Real Python: Python while Loops](https://realpython.com/python-while-loop/)
- [Python docs: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

## Next Module
[Module 015: Loops: `for`](../module-015-for-loops/README.md) — Learn the `for` loop for iterating over sequences, and master the `range()` function.
