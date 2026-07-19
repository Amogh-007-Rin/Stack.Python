# Module 018: Lists: Basics — Solutions

## Exercise 1: List Create and Index

```python
foods = ["pizza", "sushi", "tacos", "pasta", "ice cream"]
print(f"First: {foods[0]}")
print(f"Last: {foods[-1]}")
print(f"Middle: {foods[len(foods) // 2]}")
```

## Exercise 2: Slice Practice

```python
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"First 3: {nums[:3]}")
print(f"Last 3: {nums[-3:]}")
print(f"Every other: {nums[::2]}")
print(f"Reversed: {nums[::-1]}")
```

## Exercise 3: Sum and Average

```python
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i + 1}: "))
    numbers.append(n)
total = 0
for n in numbers:
    total = total + n
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {total / len(numbers)}")
```

## Exercise 4: Nested List Tic-Tac-Toe

```python
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
board[0][0] = "X"
board[1][1] = "O"
board[2][2] = "X"
for row in board:
    print("|" + "|".join(row) + "|")
```

## Exercise 5: Palindrome Checker

```python
word = input("Enter a word: ")
chars = list(word)
if chars == chars[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

## Exercise 6: List from String

```python
sentence = input("Enter a sentence: ")
chars = list(sentence)
space_count = 0
for c in chars:
    if c == " ":
        space_count = space_count + 1
print(f"Spaces: {space_count}")
print(f"Total characters: {len(chars)}")
```

## Exercise 7: Max and Min (No Built-in)

```python
values = [45, 12, 89, 3, 67, 24, 55]
maximum = values[0]
minimum = values[0]
for num in values:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print(f"Max: {maximum}, Min: {minimum}")
```

## Exercise 8: List Shifting

```python
items = [1, 2, 3, 4, 5]
left_shift = items[1:] + items[:1]
print(f"Left shift: {left_shift}")
right_shift = items[-1:] + items[:-1]
print(f"Right shift: {right_shift}")
```
