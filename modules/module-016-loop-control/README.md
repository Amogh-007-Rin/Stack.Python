# Module 016: Loop Control (`break`, `continue`, loop `else`)

> **Phase:** 2. Control Flow & Data | **Estimated time:** 1.5 hours | **Milestone Project:** No

## Prerequisites
- [Module 015: Loops: `for`](../module-015-for-loops/README.md)

## Learning Objectives
- Use `break` to exit a loop early
- Use `continue` to skip the rest of the current iteration
- Write loop `else` clauses that execute only on normal completion
- Control flow in nested loops with `break` and `continue`
- Use `pass` as a placeholder for empty blocks

## Why This Matters
Sometimes you don't need to finish a loop — you've found what you were looking for (`break`), or the current item doesn't need processing (`continue`). These control statements give you finer command over loop execution and let you write more efficient, readable code. The `else` clause is a Python exclusive that elegantly handles "not found" scenarios without flag variables.

## Concept Explanation

### `break` — Exit the Loop

`break` immediately terminates the innermost loop:

```python
for num in range(1, 101):
    if num == 5:
        break
    print(num, end=" ")
# Output: 1 2 3 4
```

When Python hits `break`, it jumps out of the loop entirely and continues with the next statement after the loop.

**Search pattern with `break`:**

```python
numbers = [3, 7, 15, 22, 8, 10]
target = 22
found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print(f"Found {target}!")
else:
    print(f"{target} not found.")
# Output: Found 22!
```

### `continue` — Skip to the Next Iteration

`continue` skips the rest of the current iteration and moves to the next one:

```python
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num, end=" ")
# Output: 1 3 5 7 9
```

When Python hits `continue`, it jumps back to the loop condition (for `while`) or the next item (for `for`), skipping any code below `continue` in the loop body.

**Filtering with `continue`:**

```python
text = "Hello, 123 World! 456"
digits = ""
for char in text:
    if not char.isdigit():
        continue
    digits = digits + char
print(digits)
# Output: 123456
```

### Loop `else`

The `else` clause runs only if the loop completed **without** hitting `break`:

```python
# Case 1: break happens → else does NOT run
for n in range(2, 10):
    if n % 2 == 0:
        print(f"{n} is even — breaking")
        break
else:
    print("No even numbers found (shouldn't happen here)")
# Output: 2 is even — breaking

# Case 2: no break → else runs
for n in range(2, 10):
    if n % 7 == 0:
        print(f"{n} is divisible by 7 — breaking")
        break
else:
    print("No numbers divisible by 7 in this range")
# Output: 7 is divisible by 7 — breaking
```

**Prime number check with `for-else`:**

```python
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime ({i} × {num // i})")
        break
else:
    print(f"{num} is prime!")
# Output: 17 is prime!
```

Without `for-else`, you'd need a separate flag variable:

```python
num = 17
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is prime!")
```

### Nested Loop Control

`break` and `continue` only affect the **innermost** loop they're in:

```python
for i in range(1, 4):
    print(f"Outer loop: i={i}")
    for j in range(1, 4):
        if j == 2:
            break  # only breaks the inner j-loop
        print(f"  Inner loop: j={j}")
# Output:
# Outer loop: i=1
#   Inner loop: j=1
# Outer loop: i=2
#   Inner loop: j=1
# Outer loop: i=3
#   Inner loop: j=1
```

To break out of nested loops, use a flag or restructure your code:

```python
found = False
for i in range(5):
    for j in range(5):
        if i * j == 12:
            print(f"Found: {i} × {j} = 12")
            found = True
            break
    if found:
        break
# Output: Found: 3 × 4 = 12
```

### `pass` — Do Nothing

`pass` is a no-operation statement. It's a placeholder where Python requires a statement but you don't want to do anything:

```python
x = 10
if x > 5:
    pass  # TODO: handle this case later
else:
    print("x is 5 or less")

for i in range(5):
    pass  # TODO: implement this loop
```

Without `pass`, an empty block causes an `IndentationError`.

## Common Pitfalls

1. **Breaking the outer loop when you meant inner** — `break` only exits the innermost loop. To break out of nested loops, use a flag.

2. **Putting `else` code on the wrong indentation level** — The `else` belongs to the loop (`for` or `while`), not to an `if` inside the loop.

3. **Using `continue` unnecessarily** — Sometimes a simple `if` guard is cleaner:

```python
# Less clear:
for x in data:
    if not condition(x):
        continue
    process(x)

# Clearer:
for x in data:
    if condition(x):
        process(x)
```

4. **Forgetting that `else` runs only if no `break`** — If the loop never executes (empty sequence), the `else` still runs. This is intentional — no element caused a break.

## Hands-On Walkthrough

Let's build a menu system with `break` to quit:

```python
while True:
    print("\n--- Menu ---")
    print("1. Say hello")
    print("2. Print numbers")
    print("3. Quit")
    choice = input("Choose (1-3): ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        for i in range(1, 6):
            print(i, end=" ")
        print()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
```

Now let's find all primes up to 50 using nested loops and `for-else`:

```python
for num in range(2, 51):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            break
    else:
        print(num, end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

## Key Takeaways

- `break` terminates the innermost loop immediately
- `continue` skips the current iteration and moves to the next
- Loop `else` runs only if the loop completed without `break` — elegant for search/validation
- `break`/`continue` only affect the innermost loop they're in
- Use flag variables to exit nested loops
- `pass` is a no-op placeholder for empty blocks
- Prefer `if` guards over `continue` when the condition is simple and positive

## Further Reading
- [Python docs: More Control Flow Tools — break and continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [Python docs: pass statement](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement)
- [Real Python: Python break, continue, and pass](https://realpython.com/python-break-continue-pass/)

## Next Module
[Module 017: Nested Loops and Pattern Printing](../module-017-nested-loops-and-patterns/README.md) — Combine loops within loops to print patterns and understand O(n²) complexity.
