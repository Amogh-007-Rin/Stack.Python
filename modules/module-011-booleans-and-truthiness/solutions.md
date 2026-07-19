# Module 011: Booleans and Truthiness — Solutions

## Exercise 1: Identify Truthiness

```python
print(bool(-1))       # True  (non-zero)
print(bool("False"))  # True  (non-empty string)
print(bool(" "))      # True  (non-empty string — it's a space)
print(bool(0.0001))   # True  (non-zero)
print(bool(None))     # False
```

## Exercise 2: What's the Output?

```python
print(True and False)     # False
print(True or False)      # True
print(not True)           # False
print(0 and 42)           # 0     (0 is falsy, and returns it)
print("" or "default")    # default  ("" is falsy, or returns "default")
print(3 or 0)             # 3     (3 is truthy, short-circuits)
print(0 and 5 or 10)      # 10    (0 and 5 → 0, then 0 or 10 → 10)
```

## Exercise 3: Short-Circuit Detective

```python
def log_and_return(value):
    print(f"called with {value}")
    return value

# 1: log_and_return(0) returns 0 (falsy), and short-circuits
result = log_and_return(0) and log_and_return(5)
# Output: called with 0
# result = 0

# 2: log_and_return(5) returns 5 (truthy), or short-circuits
result = log_and_return(5) or log_and_return(10)
# Output: called with 5
# result = 5

# 3: and has higher precedence than or
# Equivalent to: log_and_return(0) or (log_and_return(3) and log_and_return(7))
result = log_and_return(0) or log_and_return(3) and log_and_return(7)
# Output: called with 0, called with 3, called with 7
# result = 7 (3 and 7 → 7; 0 or 7 → 7)
```

## Exercise 4: Fix the Bug

The string `"False"` is non-empty, so `bool("False")` is `True`. The code thinks the value is falsy.

```python
value = "False"
if not value:          # bool("False") is True, so not True is False
    print("Value is falsy")
else:
    print("Value is truthy")  # This runs

# Fix: check the actual intended condition
if value == "False":
    print("String says False")
elif not value:
    print("Value is truly empty/falsy")
else:
    print(f"Value is: {value}")
```

## Exercise 5: Truthy FizzBuzz

```python
num = int(input("Enter a number: "))
if not num:
    print("Zero entered")
else:
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    print(output if output else f"{num} is not divisible by 3 or 5")
```

## Exercise 6: Validate Input with Truthiness

```python
name = input("Enter your name: ")
if not name:
    print("Name cannot be empty!")
else:
    age_input = input("Enter your age: ")
    if age_input and age_input.isdigit():
        age = int(age_input)
        if age > 0:
            print(f"Hello {name}, you are {age} years old.")
        else:
            print("Age must be positive.")
    else:
        print("Invalid age input.")
```
