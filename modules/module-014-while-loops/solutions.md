# Module 014: Loops: `while` — Solutions

## Exercise 1: Countdown

```python
count = 10
while count > 0:
    print(count)
    count = count - 1
print("Blast off!")
```

## Exercise 2: Sum Until Zero

```python
total = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    total = total + num
    num = int(input("Enter a number (0 to stop): "))
print(f"Total: {total}")
```

## Exercise 3: Input Validation

```python
num = None
while num is None:
    user_input = input("Enter a number between 1 and 10: ")
    if user_input.isdigit():
        n = int(user_input)
        if 1 <= n <= 10:
            num = n
        else:
            print("Number must be between 1 and 10.")
    else:
        print("Invalid input. Please enter a number.")
print(f"You entered: {num}")
```

## Exercise 4: Factorial

```python
n = int(input("Enter a positive integer: "))
result = 1
original_n = n
while n > 0:
    result = result * n
    n = n - 1
print(f"{original_n}! = {result}")
```

## Exercise 5: Guess the Number (Hard Mode)

```python
import random
secret = random.randint(1, 100)
guesses = 0
max_guesses = 7
guess = None

while guess != secret and guesses < max_guesses:
    user_input = input(f"Guess ({guesses + 1}/{max_guesses}): ")
    if user_input.isdigit():
        guess = int(user_input)
        guesses = guesses + 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
    else:
        print("Enter a number!")

if guess == secret:
    print(f"Correct! You got it in {guesses} guesses.")
else:
    print(f"Out of guesses! The number was {secret}.")
```

## Exercise 6: Average Calculator

```python
total = 0
count = 0
user_input = input("Enter a number (or 'done'): ")
while user_input != "done":
    if user_input.isdigit():
        total = total + int(user_input)
        count = count + 1
    else:
        print("Invalid input.")
    user_input = input("Enter a number (or 'done'): ")

if count > 0:
    print(f"Average: {total / count:.2f}")
else:
    print("No numbers entered.")
```

## Exercise 7: Multiplication Table Printer

```python
n = int(input("Enter a number: "))
i = 1
while i <= 12:
    print(f"{n} x {i:2} = {n * i:3}")
    i = i + 1
```
