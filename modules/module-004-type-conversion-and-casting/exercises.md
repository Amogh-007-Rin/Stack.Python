# Module 004: Exercises

## Exercise 1: Basic Casting
Convert the following values to the target type and print the result:
- `"100"` → int
- `"3.14"` → float
- `42` → str
- `0` → bool

## Exercise 2: Truncation vs Rounding
What does `int(7.99)` return? What about `int(-7.99)`?

## Exercise 3: String Concatenation
Fix this code so it runs without error:
```python
score = 95
print("Your score is " + score)
```

## Exercise 4: Truthiness
Predict the output:
```python
print(bool("False"))
print(bool("0"))
print(bool(0.0))
print(bool(" "))
```

## Exercise 5: Safe Conversion
Write code that converts the string `"3.99"` to an integer (the result should be `3`).

## Exercise 6: Implicit Conversion
Will this code run? If so, what is the output?
```python
print(5 + True)
print(5 + False)
```

## Exercise 7: Error Identification
Why does this code fail? How would you fix it?
```python
value = "10.5"
number = int(value)
```

## Exercise 8: Mixed Types
Create a program that:
1. Assigns `"42"` to a variable
2. Converts it to an integer
3. Adds `8`
4. Converts the result back to a string
5. Prints "The answer is " + result
