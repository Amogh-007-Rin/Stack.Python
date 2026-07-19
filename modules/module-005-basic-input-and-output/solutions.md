# Module 005: Solutions

## Exercise 1
```python
name = input("What is your name? ")
print("Hello,", name)
```

## Exercise 2
```python
age = int(input("How old are you? "))
months = age * 12
print("You are", months, "months old.")
```

## Exercise 3
```python
width = float(input("Enter width: "))
height = float(input("Enter height: "))
area = width * height
print("Area:", area)
```

## Exercise 4
```python
value = input("Type something: ")
print(type(value))  # <class 'str'>
```
`input()` always returns a string.

## Exercise 5
```python
celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(celsius, "C =", fahrenheit, "F")
```

## Exercise 6
`age` is a string, so `age * 2` repeats the string (e.g., "2525"). Fix by converting to int:
```python
age = int(input("Your age: "))
print("Double your age:", age * 2)
```

## Exercise 7
```python
first = input("First name: ")
last = input("Last name: ")
year = input("Birth year: ")
print(first, last, "was born in", year + ".")
```

## Exercise 8
```python
item = input("Item name: ")
qty = int(input("Quantity: "))
price = float(input("Unit price: "))
total = qty * price
print(qty, item, "cost $" + str(total))
```
