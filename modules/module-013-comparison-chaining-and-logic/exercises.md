# Module 013: Comparison Chaining & Logical Operators Deep Dive — Exercises

## Exercise 1: Chained Comparison
Write a program that asks for a number and checks if it's between 1 and 100 (inclusive) using a **single chained comparison**.

## Exercise 2: De Morgan's Refactor
Rewrite the following condition using De Morgan's laws to make it simpler:
```python
if not (age >= 18 and has_id):
    print("Access denied")
```

## Exercise 3: `is` vs `==`
Predict the output:
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a is c)
print(c == b)
```

## Exercise 4: Short-Circuit Safety
Write a function `safe_divide(a, b)` that returns `a / b` if `b` is non-zero, otherwise returns `None`. Use short-circuit evaluation in a single line.

## Exercise 5: Vowel or Consonant
Ask the user for a letter. Use the `in` operator to check if it's a vowel (a, e, i, o, u). Print "vowel", "consonant", or "not a letter".

## Exercise 6: Operator Precedence Puzzle
Without running, determine the output:
```python
x = 3
y = 0
z = 5
result = x > 0 and y == 0 or z > 10
print(result)

result2 = not x > 0 and y == 0
print(result2)
```

## Exercise 7: Range Validator
Ask the user for a score (0-100). Use chained comparisons and logical operators to print:
- "Excellent" for 90-100
- "Good" for 70-89
- "Needs improvement" for 50-69
- "Fail" for 0-49
- "Invalid" for anything else
