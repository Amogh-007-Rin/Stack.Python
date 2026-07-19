# Module 010: Solutions

# Exercise 1: Floor division
num1 = 15.0
op = "//"
num2 = 4.0
if op == "//":
    result = num1 // num2
print(result)  # 3.0 (floor division of floats)


# Exercise 2: Division with zero check
num2 = float(input("Enter second number: "))
if num2 == 0:
    print("Cannot divide by zero")
else:
    print(10.0 / num2)


# Exercise 3: float() vs int() for input
# float() accepts both integer input ("5") and decimal input ("5.5"),
# making the calculator more flexible. int() would reject decimal input.


# Exercise 4: Valid operator check
valid_ops = ["+", "-", "*", "/", "//", "%", "**"]
op = input("Enter operator: ")
if op not in valid_ops:
    print("Invalid operator")


# Exercise 5: Floating point imprecision
# 7.0 / 3.0 = 2.3333333333333335


# Exercise 6: Calculator edge cases
# - Division by zero (e.g., 5 / 0)
# - Very large numbers (e.g., 10 ** 1000)
# - Negative numbers (e.g., -5 % 3)
# - Very small decimals (e.g., 0.0000001 * 0.0000001)
# - Zero as first number (e.g., 0 + 5)


# Exercise 7: Formatting division results
# For division operations, use formatting:
# result = num1 / num2
# print(f"{num1} / {num2} = {result:.2f}")


# Exercise 8: Full calculator loop
"""
1. Print welcome message and show available operators.
2. Enter a loop that:
   a. Prompts for first number (check if "done" to exit).
   b. Prompts for operator.
   c. Prompts for second number.
   d. Performs the calculation with error checking.
   e. Displays the result.
3. When user types "done", print goodbye message and exit.
"""
