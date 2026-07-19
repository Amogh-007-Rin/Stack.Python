# Module 056: Error Handling — Exercises

1. **Basic try/except**: Write a function `safe_divide(a, b)` that returns the result of `a / b` or `"Error: division by zero"` if `ZeroDivisionError` occurs.

2. **Multiple except**: Write a function `parse_int(value)` that tries to convert `value` to `int`. Catch `ValueError` and `TypeError` separately, with different messages.

3. **try/except/else/finally**: Write a function `read_file_safe(path)` that:
   - Tries to open and read the file
   - Catches `FileNotFoundError`
   - Uses `else` to print success
   - Uses `finally` to print "Operation attempted"

4. **raise**: Write a `withdraw(balance, amount)` function that raises `ValueError` if amount exceeds balance or is negative. Test both cases.

5. **Common exception types**: Write a function `process_data(data)` that handles at least three different exception types: `TypeError`, `ValueError`, and `KeyError`. Demonstrate each case.
