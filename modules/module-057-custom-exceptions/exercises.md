# Module 057: Custom Exceptions — Exercises

1. **Simple Custom Exception**: Create a `NegativeNumberError` that inherits from `Exception`. Write a function `sqrt_positive(x)` that raises it for negative numbers.

2. **Exception with Attributes**: Create a `GradeOutOfRangeError` with `grade` and `min_value`, `max_value` attributes. Write a function `validate_grade(grade)` that raises it if grade is not between 0 and 100.

3. **Exception Hierarchy**: Create an exception hierarchy for a library management system:
   - `LibraryError` (base)
   - `BookNotFoundError` (book not in catalog)
   - `BookNotAvailableError` (book is checked out)
   - `MemberNotFoundError` (member not found)

4. **Catching Custom Exceptions**: Write a `Bank` class with `transfer(from_acct, to_acct, amount)` that raises `InsufficientFundsError` (custom) if the source has insufficient balance. Catch it in the calling code and print a user-friendly message.

5. **Re-raising**: Write a function `process_order(order_data)` that catches a custom `ValidationError`, logs it, then re-raises after adding context info to the exception.
