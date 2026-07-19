# Module 008: Exercises

## Exercise 1: f-string Basics
Create variables `product = "Book"` and `price = 19.99`. Use an f-string to print: "The Book costs $19.99."

## Exercise 2: Arithmetic in f-strings
Use an f-string to print the result of `15 * 37` with a label.

## Exercise 3: Format Specifiers
Given `pi = 3.1415926535`, print it with:
- 2 decimal places
- 4 decimal places
- As a percentage (multiply by 100 — actually just use `:.2f` and append `%`)

## Exercise 4: Alignment
Print the word "Python" left-aligned in 15 spaces, right-aligned in 15 spaces, and centered in 15 spaces.

## Exercise 5: .format() Method
Using the `.format()` method, print: "Your score is 85 out of 100." using variables `score = 85` and `total = 100`.

## Exercise 6: %-formatting
Convert this f-string to old-style `%` formatting:
```python
name = "Bob"
age = 25
print(f"{name} is {age} years old.")
```

## Exercise 7: Tabular Output
Create a small table using f-strings with alignment:
```
Name    Age  City
Alice   30   London
Bob     25   Paris
```

## Exercise 8: Currency Formatter
Given `amount = 1234.5678`, print it as:
- `$1,234.57` (hint: use `:,.2f`)
- Right-aligned in 15 characters with `$` prefix
