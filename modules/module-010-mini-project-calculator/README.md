# Module 010: Milestone Project — Command-Line Calculator

> **Phase:** 1. Fundamentals  |  **Estimated time:** 3 hours  |  **Milestone Project:** Yes

## Prerequisites
- [Module 009: Numbers Deep Dive](../module-009-numbers-deep-dive/README.md)
- All prior modules (000–009) are assumed

## Learning Objectives
By the end of this module, you will be able to:
- Build a complete, interactive CLI program from scratch
- Take user input for two numbers and an operator
- Perform arithmetic based on the operator using conditional logic
- Handle division by zero gracefully
- Apply concepts from all prior modules (variables, types, conversion, operators, strings, formatting, math)

## Why This Matters
A calculator is the classic "first real program" for a reason: it combines input, output, math, control flow, and error handling into one cohesive project. Completing this milestone proves you can build something useful from scratch — and gives you a template for many future projects.

## Project Brief

Build a command-line calculator that:
1. Prompts the user for two numbers.
2. Prompts for an operator (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
3. Computes and displays the result.
4. Handles division by zero gracefully (prints an error message instead of crashing).
5. Formats output cleanly using f-strings.

### Example Run

```
=== Python Command-Line Calculator ===

Enter first number: 10
Enter operator (+, -, *, /, //, %, **): /
Enter second number: 3
10.0 / 3.0 = 3.3333333333333335

Enter first number: 10
Enter operator (+, -, *, /, //, %, **): /
Enter second number: 0
Error: Division by zero is not allowed.

Enter first number: 2
Enter operator (+, -, *, /, //, %, **): **
Enter second number: 10
2.0 ** 10.0 = 1024.0

Enter first number: done
Goodbye!
```

## Concept Application

This project brings together everything from Modules 002–009:

| Concept | Where Used |
|---------|------------|
| `print()` | Output and formatting |
| `input()` | Getting user input |
| Variables | Storing numbers and operator |
| Type conversion | `float()` on input strings |
| Arithmetic operators | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparison operators | Checking for zero divisor, valid operator |
| Logical operators | Combining conditions |
| f-strings | Formatting output |
| `==` and `!=` | Comparing operator string |
| Comments | Documenting code |

## Common Pitfalls

1. **Not converting input to numbers**: `input()` returns strings. Use `float()` or `int()`.
2. **Division by zero**: Check if the second number is 0 before dividing.
3. **Invalid operator**: Decide what happens when the user enters something other than the 7 valid operators.
4. **Infinite loop**: Make sure there's a way for the user to exit (e.g., typing "done" or pressing Ctrl+C).
5. **Floating-point display**: Some results like `0.1 + 0.2` may show many decimal places. `round()` or format specifiers can help.

## Key Takeaways

- A complete interactive program requires input → processing → output.
- Always validate input before performing operations.
- Division by zero must be checked explicitly.
- A loop lets the user perform multiple calculations without restarting.
- Break the problem into small steps: get input, validate, compute, display.
- All the pieces from earlier modules come together here.
- This project structure (input-loop-compute-display) applies to many CLI tools.

## Further Reading
- [Input and Output (docs.python.org)](https://docs.python.org/3/tutorial/inputoutput.html)
- [Errors and Exceptions (docs.python.org)](https://docs.python.org/3/tutorial/errors.html)

## Next Module
Congratulations on completing your first milestone! Continue to **Module 011** (Control Flow: if/elif/else) to learn how to make decisions in your programs.
