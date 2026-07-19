# Module 013: Comparison Chaining & Logical Operators Deep Dive

> **Phase:** 2. Control Flow & Data | **Estimated time:** 1.5 hours | **Milestone Project:** No

## Prerequisites
- [Module 012: Conditional Statements (if / elif / else)](../module-012-conditional-statements/README.md)

## Learning Objectives
- Write chained comparisons like `0 < x <= 10`
- Combine comparisons with `and`, `or`, `not` effectively
- Understand short-circuit evaluation in detail
- Apply De Morgan's laws to simplify negated conditions
- Know operator precedence for logical operators
- Distinguish `is` (identity) from `==` (equality)
- Use the `in` operator for membership testing

## Why This Matters
Clear, concise conditions make your code more readable and less error-prone. Chaining comparisons mirrors mathematical notation, and understanding short-circuit evaluation helps you write efficient, safe conditions. Knowing `is` vs `==` prevents subtle bugs with `None`, sentinels, and certain Python internals.

## Concept Explanation

### Chained Comparisons

Python lets you chain multiple comparisons in a single expression:

```python
x = 5
print(1 < x < 10)     # True   (1 < 5 and 5 < 10)
print(0 <= x <= 5)    # True   (0 <= 5 and 5 <= 5)
print(1 < x < 4)      # False  (1 < 5 is True, but 5 < 4 is False)
```

This is equivalent to `1 < x and x < 10`, but more readable and closer to mathematical notation.

You can chain any comparison operators:

```python
age = 25
print(18 <= age <= 65)   # True   (adult working age)
name = "Anna"
print("A" <= name <= "Z")  # Depends on lexicographic order
```

### Combining Comparisons with `and`, `or`, `not`

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome to the show.")
# Output: Welcome to the show.

if age < 12 or age >= 65:
    print("Discount applies.")
# Output: (nothing, since 22 is between 12 and 64)

if not has_ticket:
    print("Please buy a ticket.")
# Output: (nothing)
```

You can group with parentheses for clarity:

```python
age = 70
is_member = False

# Without parentheses: operator precedence handles it
if age >= 65 and is_member or age >= 75:
    print("Special discount.")
# Output: Special discount.

# Better: parentheses make intent clear
if (age >= 65 and is_member) or age >= 75:
    print("Special discount.")
# Output: Special discount.
```

### Short-Circuit Evaluation (Deep Dive)

Python evaluates `and` and `or` **left to right** and stops as soon as the result is known.

**`and`:** Stops on the first falsy value.

```python
def check_positive(n):
    print(f"  check_positive({n}) called")
    return n > 0

# All three conditions are True, so all functions are called
result = check_positive(5) and check_positive(3) and check_positive(1)
print(f"Result: {result}")
# Output:
#   check_positive(5) called
#   check_positive(3) called
#   check_positive(1) called
# Result: True

# check_positive(0) returns False, so Python never calls check_positive(3)
result = check_positive(5) and check_positive(0) and check_positive(3)
print(f"Result: {result}")
# Output:
#   check_positive(5) called
#   check_positive(0) called
# Result: False
```

**`or`:** Stops on the first truthy value.

```python
def get_name(i):
    print(f"  get_name({i}) called")
    return ["", "", "Alice", "Bob"][i]

# get_name(0) returns "" (falsy), so Python continues
# get_name(1) returns "" (falsy), so Python continues
# get_name(2) returns "Alice" (truthy), Python stops
name = get_name(0) or get_name(1) or get_name(2) or get_name(3)
print(f"Name: {name}")
# Output:
#   get_name(0) called
#   get_name(1) called
#   get_name(2) called
# Name: Alice
```

### De Morgan's Laws

These rules let you simplify negated compound conditions:

- `not (A and B)` is equivalent to `(not A) or (not B)`
- `not (A or B)` is equivalent to `(not A) and (not B)`

```python
age = 20
has_id = False

# Both conditions are equivalent:
if not (age >= 18 and has_id):
    print("Cannot enter without valid ID.")

if (age < 18) or (not has_id):
    print("Cannot enter without valid ID.")
# Output (both): Cannot enter without valid ID.
```

Use De Morgan's to make your conditions more natural to read. Choose the form that sounds most like plain English.

### Operator Precedence

From highest to lowest precedence for logical operators:

1. `not`   (highest)
2. `and`
3. `or`    (lowest)

Comparison operators (`>`, `<`, `==`, `!=`, `>=`, `<=`, `is`, `in`) have higher precedence than `not`/`and`/`or`, so comparisons are evaluated first.

```python
x = 5
# Precedence: (x > 3) and (x < 10)
result = x > 3 and x < 10  # True

# Precedence: not (x > 10)
result = not x > 10         # True
```

When in doubt, add parentheses. They make your intent clear and cost nothing at runtime.

### `is` vs `==` (Identity vs Equality)

- `==` checks whether two objects have the **same value** (equality)
- `is` checks whether two objects are the **same object in memory** (identity)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True   (same contents)
print(a is b)  # False  (different list objects)
print(a is c)  # True   (c points to the same object as a)
```

**Important:** Use `is` to compare to `None`:

```python
value = None
if value is None:
    print("No value.")
if value is not None:
    print("Has a value.")
```

Never use `is` for comparing integers, strings, or other values — it works unpredictably across implementations.

### The `in` Operator

`in` checks whether a value appears in a collection or sequence:

```python
print("a" in "hello")       # False
print("e" in "hello")       # True
print(3 in [1, 2, 3, 4])    # True
print(10 in [1, 2, 3, 4])   # False
```

`not in` checks the opposite:

```python
print("x" not in "hello")   # True
```

## Common Pitfalls

1. **Using `is` instead of `==` for strings/numbers** — `is` compares identity, not value. It may accidentally work for small integers (due to interning) but is unreliable.

2. **Forgetting that `not` has higher precedence than `and`/`or`** — `not x > 0 and y > 0` means `(not (x > 0)) and (y > 0)`, not `not ((x > 0) and (y > 0))`.

3. **Over-chaining** — `a < b < c` is fine, but `a < b < c < d < e < f` is hard to read.

4. **Negating complex conditions without De Morgan's** — `not (age >= 18 and has_id)` is harder to read than `age < 18 or not has_id`.

5. **Using `== True` or `== False` unnecessarily** — Just use `if x:` or `if not x:`.

## Hands-On Walkthrough

Let's build an admission system with chained comparisons and logical operators:

```python
age = int(input("Enter age: "))  # Assume 22
height = float(input("Enter height in cm: "))  # Assume 175

# Chained comparison
if 12 <= age <= 80:
    if height >= 120:
        if 50 <= height <= 200:
            print("You meet all ride requirements!")
        else:
            print("Height out of valid range.")
    else:
        print("Too short for this ride.")
else:
    print("Age out of allowed range.")
```

Now using `in` with conditionals:

```python
vowels = "aeiou"
char = input("Enter a letter: ").lower()  # Assume 'a'

if char in vowels:
    print(f"{char} is a vowel.")
elif char not in vowels and char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("That's not a letter.")
# Output: a is a vowel.
```

## Key Takeaways

- Chained comparisons (`a < x < b`) are evaluated as `a < x and x < b`
- `and` returns the first falsy operand; `or` returns the first truthy operand
- Short-circuit evaluation stops as soon as the result is determined
- De Morgan's laws: `not (A and B)` = `(not A) or (not B)`; `not (A or B)` = `(not A) and (not B)`
- Precedence: `not` > `and` > `or` (comparisons happen before all of these)
- `is` checks identity (same object); `==` checks equality (same value)
- Always use `is None` / `is not None` to check for `None`
- `in` checks membership in a string, list, or other collection

## Further Reading
- [Python docs: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
- [Python docs: Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Python docs: Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations)
- [Real Python: Python `is` vs `==`](https://realpython.com/courses/python-is-identity-vs-equality/)

## Next Module
[Module 014: Loops: `while`](../module-014-while-loops/README.md) — Learn how to repeat code with `while` loops, avoid infinite loops, and use the accumulator pattern.
