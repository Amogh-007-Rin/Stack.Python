# Module 013: Comparison Chaining & Logical Operators Deep Dive — Solutions

## Exercise 1: Chained Comparison

```python
num = float(input("Enter a number: "))
if 1 <= num <= 100:
    print(f"{num} is between 1 and 100")
else:
    print(f"{num} is outside the range")
```

## Exercise 2: De Morgan's Refactor

```python
# Original: not (age >= 18 and has_id)
# De Morgan's: (not age >= 18) or (not has_id)
# Simplified: age < 18 or not has_id
if age < 18 or not has_id:
    print("Access denied")
```

## Exercise 3: `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True  (same values)
print(a is b)  # False (different objects)
print(a is c)  # True  (same object)
print(c == b)  # True  (same values)
```

## Exercise 4: Short-Circuit Safety

```python
def safe_divide(a, b):
    return b != 0 and a / b or None

# Tests
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None
```

## Exercise 5: Vowel or Consonant

```python
char = input("Enter a letter: ").lower()
if len(char) != 1 or not char.isalpha():
    print("Not a single letter")
elif char in "aeiou":
    print("vowel")
else:
    print("consonant")
```

## Exercise 6: Operator Precedence Puzzle

```python
x = 3
y = 0
z = 5

# Precedence: comparisons first, then not, then and, then or
# (x > 0) and (y == 0) or (z > 10)
# True and True or False → True or False → True
result = x > 0 and y == 0 or z > 10
print(result)  # True

# not (x > 0) and (y == 0)
# not True and True → False and True → False
result2 = not x > 0 and y == 0
print(result2)  # False
```

## Exercise 7: Range Validator

```python
score = float(input("Enter score (0-100): "))
if 0 <= score <= 100:
    if 90 <= score <= 100:
        print("Excellent")
    elif 70 <= score <= 89:
        print("Good")
    elif 50 <= score <= 69:
        print("Needs improvement")
    else:
        print("Fail")
else:
    print("Invalid")
```
