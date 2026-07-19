# Complete Reference Implementation for Command-Line Calculator
# Uses only concepts from Modules 000-009 (no try/except, no functions beyond basic)

print("=== Python Command-Line Calculator ===")
print()

while True:
    first_input = input("Enter first number (or 'done' to exit): ")

    if first_input == "done":
        break

    num1 = float(first_input)

    op = input("Enter operator (+, -, *, /, //, %, **): ")

    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    elif op == "//":
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 // num2
    elif op == "%":
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 % num2
    elif op == "**":
        result = num1 ** num2
    else:
        result = "Error: Unknown operator."

    print(f"{num1} {op} {num2} = {result}")
    print()

print("Goodbye!")
