# Module 005: Quiz

## Question 1 (Multiple Choice)
What does `input()` always return?
- A) An integer
- B) A float
- C) A string
- D) The type depends on what the user types

## Question 2 (Multiple Choice)
If the user types `42`, what is the type of `input()`'s return value?
- A) int
- B) float
- C) str
- D) bool

## Question 3 (What does this output?)
```python
age = input("Age: ")
print(age * 2)
```
(User types `10`)

## Question 4 (Multiple Choice)
How do you get a number from the user and store it as an integer?
- A) `int(input())`
- B) `input(int())`
- C) `input().int()`
- D) `int = input()`

## Question 5 (True/False)
The prompt string passed to `input()` is displayed to the user.
- True
- False

## Question 6 (Multiple Choice)
What does `float(input())` return if the user types `3.5`?
- A) `"3.5"`
- B) `3.5`
- C) `3`
- D) Error

## Question 7 (Short Answer)
Write a single line of code that asks "What is your age? " and stores the result as an integer.

## Question 8 (Multiple Choice)
What is wrong with this code?
```python
x = input("Number: ")
print(x + 10)
```
- A) `input()` cannot take a prompt
- B) `x` is a string, cannot add to integer
- C) `print()` cannot take two arguments
- D) Nothing — it works fine

---

## Answers

1. **C** — A string
2. **C** — str (always a string, regardless of content)
3. **1010** (string repetition, not numeric multiplication)
4. **A** — `int(input())`
5. **True**
6. **B** — 3.5
7. **`age = int(input("What is your age? "))`**
8. **B** — `x` is a string, cannot add `str` + `int`
