# Module 015: Loops: `for` — Solutions

## Exercise 1: Sum of Even Numbers

```python
total = 0
for i in range(2, 101, 2):
    total = total + i
print(f"Sum of evens 2-100: {total}")
```

## Exercise 2: Character Counter

```python
text = input("Enter a string: ")
char = input("Enter a character to count: ")
count = 0
for c in text:
    if c == char:
        count = count + 1
print(f"'{char}' appears {count} time(s)")
```

## Exercise 3: Multiplication Table

```python
n = int(input("Enter a number: "))
for i in range(1, 13):
    print(f"{n} x {i:2} = {n * i:3}")
```

## Exercise 4: Factorial with `for`

```python
n = int(input("Enter a positive integer: "))
result = 1
for i in range(1, n + 1):
    result = result * i
print(f"{n}! = {result}")
```

## Exercise 5: Reverse a String

```python
text = input("Enter a string: ")
for i in range(len(text) - 1, -1, -1):
    print(text[i])
```

## Exercise 6: FizzBuzz

```python
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

## Exercise 7: `for-else` Prime Finder

```python
n = int(input("Enter a number: "))
if n <= 1:
    print(f"{n} is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime ({i} × {n // i})")
            break
    else:
        print(f"{n} is prime!")
```

## Exercise 8: Sum of Digits

```python
num = input("Enter a positive integer: ")
total = 0
for char in num:
    if char.isdigit():
        total = total + int(char)
print(f"Sum of digits: {total}")
```
