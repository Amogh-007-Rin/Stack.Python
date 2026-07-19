# Module 003: Solutions

## Exercise 1
```python
city = "Tokyo"
population = 13929286
area_km2 = 2194.0
print(city, population, area_km2)
```

## Exercise 2
```python
a = 15
b = 4
print(a + b)  # 19
print(a * b)  # 60
print(a / b)  # 3.75
```

## Exercise 3
```python
thing = 10
print(type(thing))  # <class 'int'>
thing = "hello"
print(type(thing))  # <class 'str'>
```

## Exercise 4
```python
x = True
print(type(x))  # <class 'bool'>
y = "42"
print(type(y))  # <class 'str'>
z = 42.0
print(type(z))  # <class 'float'>
```

## Exercise 5
- `2nd_place` — invalid (starts with digit). Fix: `second_place`
- `my_var` — valid
- `class` — invalid (keyword). Fix: `class_` or `my_class`
- `_data` — valid
- `user-name` — invalid (hyphen). Fix: `user_name`
- `total$` — invalid (`$` not allowed). Fix: `total`

## Exercise 6
It prints `Alice`. Variables are case-sensitive; `name` and `Name` are different variables.

## Exercise 7
```python
first = "Jane"
last = "Doe"
birth_year = 1995
height = 1.70
used_python_before = True
print(first, last, birth_year, height, used_python_before)
```

## Exercise 8
```python
result = 10 / 2
print(type(result))  # <class 'float'>
```
Division always returns a float, even when the result is a whole number.
