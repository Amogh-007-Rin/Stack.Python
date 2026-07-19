# Module 052: Class Methods, Static Methods, Properties — Exercises

1. **Alternative Constructor**: Create a `Book` class with `title`, `author`, and `isbn`. Add a class method `from_string(cls, data: str)` that parses `"title|author|isbn"`.

2. **Static Method Utility**: Create a `MathUtils` class with static methods `factorial(n)` and `is_prime(n)`. No instance needed.

3. **Property with Validation**: Create a `BankAccount` class with a `balance` property. The setter should reject negative amounts. Add a read-only `account_age_days` property computed from a `created_at` datetime.

4. **Property Getter/Setter/Deleter**: Create a `Password` class with a `password` property. The getter returns masked text (`****`), the setter validates minimum length (8 chars), and the deleter clears the stored value.

5. **Combined**: Write a `Temperature` class that stores celsius internally but exposes `celsius` and `fahrenheit` as properties. Add a class method `from_fahrenheit(cls, f: float)`.
