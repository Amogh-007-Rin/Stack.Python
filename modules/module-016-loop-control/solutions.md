# Module 016: Loop Control (break, continue, loop else) — Solutions

## Exercise 1: Find First Even

```python
numbers = [3, 7, 9, 12, 15, 18]
for n in numbers:
    if n % 2 == 0:
        print(f"First even number: {n}")
        break
```

## Exercise 2: Skip Vowels

```python
word = input("Enter a word: ")
vowels = "aeiou"
for char in word:
    if char in vowels:
        continue
    print(char, end="")
print()
```

## Exercise 3: Prime Checker with `for-else`

```python
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime!")
```

## Exercise 4: Menu with Break

```python
while True:
    print("\n1. Numbers 1-10")
    print("2. Say Hello 5x")
    print("3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        for i in range(1, 11):
            print(i, end=" ")
        print()
    elif choice == "2":
        for _ in range(5):
            print("Hello")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid.")
```

## Exercise 5: Nested Loop — Find a Pair

```python
found = False
for i in range(1, 11):
    for j in range(1, 11):
        if i * j == 24:
            print(f"Found: {i} × {j} = 24")
            found = True
            break
    if found:
        break
```

## Exercise 6: Filter with Continue

```python
text = "a1b2c3d4e5"
digits = ""
for char in text:
    if not char.isdigit():
        continue
    digits = digits + char
print(digits)
```

## Exercise 7: Pass Placeholder

```python
def my_function():
    pass  # TODO: implement later

my_function()  # does nothing

# Now fill it in
def my_function():
    print("Function works!")

my_function()
```
