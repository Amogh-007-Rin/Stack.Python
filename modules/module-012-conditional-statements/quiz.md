# Module 012: Conditional Statements (if / elif / else) — Quiz

## Question 1
What does the following code print?
```python
x = 5
if x > 10:
    print("A")
elif x > 3:
    print("B")
elif x > 1:
    print("C")
else:
    print("D")
```
- A) A
- B) B
- C) C
- D) B then C

## Question 2
Which of the following checks if `name` is **not empty**?
- A) `if name:`
- B) `if name == "":`
- C) `if not name:`
- D) `if name is None:`

## Question 3
What is the correct way to check if a variable `result` is `None`?
- A) `if result == None:`
- B) `if result is None:`
- C) `if not result:`
- D) `if result = None:`

## Question 4
What's wrong with this code?
```python
if score >= 90
    print("A")
```
- A) Missing colon after the condition
- B) `score` is not defined
- C) `print` should be capitalized
- D) Nothing is wrong

## Question 5
Which of the following is NOT valid indentation for an `if` block?
- A) 4 spaces
- B) 1 tab
- C) 2 spaces
- D) 0 spaces

## Question 6
What does this code print?
```python
x = 0
if x:
    print("Truthy")
else:
    print("Falsy")
```
- A) Truthy
- B) Falsy
- C) Nothing
- D) Error

## Question 7
How many branches can a single `if` statement have with `elif`?
- A) Exactly 2
- B) Exactly 3
- C) As many as you need
- D) At most 5

## Answers
1. B — `x > 3` is True, so prints "B" and skips remaining elif/else
2. A — `if name:` checks truthiness; non-empty string is truthy
3. B — Use `is None` for identity comparison with None
4. A — All `if`, `elif`, `else` lines must end with a colon
5. D — 0 spaces would mean the block is not indented
6. B — `0` is falsy, so `else` branch runs
7. C — You can have as many `elif` branches as needed
