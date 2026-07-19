# Module 004: Solutions

## Exercise 1
```python
print(int("100"))     # 100
print(float("3.14"))  # 3.14
print(str(42))        # "42"
print(bool(0))        # False
```

## Exercise 2
`int(7.99)` returns `7` (truncation, not rounding).
`int(-7.99)` returns `-7` (truncates toward zero).

## Exercise 3
```python
score = 95
print("Your score is " + str(score))
```

## Exercise 4
```python
print(bool("False"))  # True (non-empty string)
print(bool("0"))      # True (non-empty string)
print(bool(0.0))      # False
print(bool(" "))      # True (non-empty string — it has a space)
```

## Exercise 5
```python
value = "3.99"
result = int(float(value))
print(result)  # 3
```

## Exercise 6
```python
print(5 + True)   # 6  (True is 1)
print(5 + False)  # 5  (False is 0)
```

## Exercise 7
`int("10.5")` raises `ValueError` because `"10.5"` is not a valid integer literal.
Fix by converting to float first:
```python
value = "10.5"
number = int(float(value))
print(number)  # 10
```

## Exercise 8
```python
val = "42"
val_int = int(val)
val_int += 8
result = "The answer is " + str(val_int)
print(result)  # The answer is 50
```
