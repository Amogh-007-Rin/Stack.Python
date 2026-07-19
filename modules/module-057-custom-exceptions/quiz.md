# Module 057: Custom Exceptions — Quiz

1. **What should custom exception classes inherit from?**
   - a) `object`
   - b) `BaseException`
   - c) `Exception` (or a subclass of it)
   - d) `Error`

2. **Why create custom exceptions instead of using built-in ones?**
   - a) They're faster
   - b) They allow callers to catch specific error types from your code
   - c) They're required by Python
   - d) Built-in exceptions cannot be raised

3. **Can custom exceptions have attributes?**
   - a) No, exceptions can only have messages
   - b) Yes, through `__init__`
   - c) Only through `__new__`
   - d) Only in Python 3.11+

4. **What is the benefit of an exception hierarchy?**
   - a) Less code
   - b) Callers can catch the base class to handle all related errors
   - c) Faster exception handling
   - d) Automatic error recovery

5. **When should you catch `Exception` instead of a custom exception?**
   - a) Never
   - b) When you want to catch all application-level errors broadly
   - c) When you expect `KeyboardInterrupt`
   - d) When performance is critical

<details>
<summary>Answers</summary>
1-c, 2-b, 3-b, 4-b, 5-b
</details>
