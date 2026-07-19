# Module 009: Solutions

## Exercise 1
```python
result = 2 ** 200
print(result)
print("Digits:", len(str(result)))  # 61 digits
```

## Exercise 2
```python
print(0.3 == 0.1 + 0.2)  # False
```
Because `0.1` and `0.2` cannot be represented exactly in binary floating-point. The result of `0.1 + 0.2` is `0.30000000000000004`, which is not equal to `0.3`.

## Exercise 3
```python
result = abs((0.1 + 0.2) - 0.3) < 1e-10
print(result)  # True
```

## Exercise 4
```python
import math
print(math.sqrt(144))       # 12.0
print(math.ceil(3.14159))   # 4
print(math.floor(3.14159))  # 3
print(math.pi * math.e)     # 8.539734222673566
```

## Exercise 5
```python
print(round(4.5))  # 4 (half rounds to even: 4 is even)
print(round(5.5))  # 6 (half rounds to even: 6 is even)
```
Python uses bankers' rounding (round half to even).

## Exercise 6
```python
import math
radius = 3
height = 7
volume = math.pi * radius ** 2 * height
print(f"Volume: {volume:.2f}")
```

## Exercise 7
```python
a = 2 + 3j
b = 1 - 1j
print("a + b:", a + b)    # (3+2j)
print("a * b:", a * b)    # (5+1j)
print("abs(a):", abs(a))  # 3.605551275463989
```

## Exercise 8
```python
import math
x1, y1 = 1, 2
x2, y2 = 4, 6
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance:", distance)  # 5.0
```
