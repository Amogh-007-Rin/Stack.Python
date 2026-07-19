# Milestone Project: Command-Line Calculator

> **Module 010** | Phase 1: Fundamentals

## Objective
Build a command-line calculator that accepts two numbers and an operator, performs the calculation, and displays the result.

## Functional Requirements

1. The program runs in an **infinite loop** until the user types `done` as the first number.
2. For each calculation:
   - Prompt for the **first number** (or `done` to exit)
   - Prompt for an **operator** from the list: `+`, `-`, `*`, `/`, `//`, `%`, `**`
   - Prompt for the **second number**
3. Perform the operation and display the result in the format:
   ```
   <num1> <operator> <num2> = <result>
   ```
4. **Division by zero** must be handled gracefully — print an error message instead of crashing.
5. Invalid operators should print an error message.
6. Every number input should accept decimal values (use `float()`).
7. Format output cleanly (f-strings recommended).

## Example Run

```
=== Python Command-Line Calculator ===

Enter first number (or 'done' to exit): 10
Enter operator (+, -, *, /, //, %, **): /
Enter second number: 3
10.0 / 3.0 = 3.3333333333333335

Enter first number (or 'done' to exit): 10
Enter operator (+, -, *, /, //, %, **): /
Enter second number: 0
Error: Division by zero is not allowed.

Enter first number (or 'done' to exit): done
Goodbye!
```

## Constraints
- Use only concepts from Modules 000–009.
- Do **not** use exception handling (`try`/`except`) — we haven't covered it yet.
- The solution should be contained in a single file.

## Files
- `starter_code.py` — skeleton with TODO comments to fill in
- `solution/calculator.py` — complete reference implementation

## Hints
- Use a `while` loop to keep the program running.
- Use `if`/`elif`/`else` to check the operator.
- Check `num2 == 0` for `/`, `//`, and `%`.
- Convert all number inputs with `float()`.
- Use `==` to compare the operator string.
- Use `break` to exit the loop when the user types `done`.
