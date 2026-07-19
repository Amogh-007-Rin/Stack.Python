# Module 012: Conditional Statements (if / elif / else) — Solutions

## Exercise 1: Grade Classifier

```python
grade = int(input("Enter grade (0-100): "))
if grade < 0 or grade > 100:
    print("Invalid grade. Must be 0-100.")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```

## Exercise 2: Leap Year Checker

```python
year = int(input("Enter a year: "))
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

## Exercise 3: Login Simulator

```python
saved_user = "admin"
saved_pass = "secret123"

username = input("Username: ")
if not username:
    print("Username required")
else:
    password = input("Password: ")
    if not password:
        print("Password required")
    elif username == saved_user and password == saved_pass:
        print(f"Welcome, {username}!")
    elif username == saved_user:
        print("Wrong password")
    else:
        print("User not found")
```

## Exercise 4: Nested Conditions

```python
age = int(input("Age: "))
license_input = input("Have a license? (y/n): ")
has_license = license_input == "y"

if age < 16:
    print("Too young to drive")
else:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
```

## Exercise 5: Number Analyzer

```python
num = float(input("Enter a number: "))
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

if num != 0 and num % 2 == 0:
    parity = "Even"
elif num != 0:
    parity = "Odd"
else:
    parity = ""

if num == 0:
    print("Zero")
else:
    print(f"{sign} and {parity}")
```

## Exercise 6: Simple Calculator

```python
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+, -, *, /): ")

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Invalid operator.")
```
