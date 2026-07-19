# Module 006: Solutions

## Exercise 1
```python
print(15 // 4)   # 3
print(15 % 4)    # 3
print(2 ** 5)    # 32
print(-15 // 4)  # -4 (floor division rounds down)
```

## Exercise 2
```python
num = 37
print("Even?", num % 2 == 0)   # False
print("Odd?", num % 2 == 1)    # True
```

## Exercise 3
```python
x = 25
print(10 <= x <= 50)  # True
```

## Exercise 4
```python
print(True and False)     # False
print(True or False)      # True
print(not (10 > 5))       # False
```

## Exercise 5
```python
total = 10
total += 5    # 15
total *= 2    # 30
total -= 8    # 22
total //= 4   # 5
```
`total` is `5`.

## Exercise 6
```python
result = 8 + 2 * 5 // 3
# 2 * 5 = 10
# 10 // 3 = 3
# 8 + 3 = 11
print(result)  # 11
```

## Exercise 7
```python
year = int(input("Enter a year: "))
print("Is leap year?", year % 4 == 0)
print("In 21st century?", 2001 <= year <= 2100)
```

## Exercise 8
```python
n = 15
print("Divisible by 3 and 5?", n % 3 == 0 and n % 5 == 0)  # True
```
