# Module 011: Booleans and Truthiness — Exercises

## Exercise 1: Identify Truthiness
Predict what `bool()` returns for each value. Then verify with `print()`.

1. `bool(-1)`
2. `bool("False")`
3. `bool(" ")` (a single space)
4. `bool(0.0001)`
5. `bool(None)`

## Exercise 2: What's the Output?
Write the output of each expression without running it.

1. `print(True and False)`
2. `print(True or False)`
3. `print(not True)`
4. `print(0 and 42)`
5. `print("" or "default")`
6. `print(3 or 0)`
7. `print(0 and 5 or 10)`

## Exercise 3: Short-Circuit Detective
Given this function:
```python
def log_and_return(value):
    print(f"called with {value}")
    return value
```

Predict what happens for each:
1. `result = log_and_return(0) and log_and_return(5)`
2. `result = log_and_return(5) or log_and_return(10)`
3. `result = log_and_return(0) or log_and_return(3) and log_and_return(7)`

## Exercise 4: Fix the Bug
Why does this code print an unexpected result? Fix it.

```python
value = "False"
if not value:
    print("Value is falsy")
else:
    print("Value is truthy")
```

## Exercise 5: Truthy FizzBuzz
Write a program that:
- Takes a number as input
- If the number is truthy (non-zero), print "Fizz" if it's divisible by 3, "Buzz" if by 5, "FizzBuzz" if by both
- If the number is falsy (zero), print "Zero entered"

## Exercise 6: Validate Input with Truthiness
Write a program that asks the user for their name and age. Use truthiness checks to validate:
- Name is not empty
- Age is a positive number (check with comparison AND a truthiness check)
