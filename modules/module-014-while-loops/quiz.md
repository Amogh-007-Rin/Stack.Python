# Module 014: Loops: `while` — Quiz

## Question 1
How many times does "Hello" print?
```python
count = 3
while count > 0:
    print("Hello")
    count = count - 1
```
- A) 0
- B) 2
- C) 3
- D) 4

## Question 2
What happens if you forget to update the loop variable?
- A) The loop runs once
- B) The loop never runs
- C) Infinite loop
- D) Syntax error

## Question 3
What keystroke interrupts an infinite loop in the terminal?
- A) Ctrl+Z
- B) Ctrl+C
- C) Ctrl+D
- D) Ctrl+X

## Question 4
What does this code print?
```python
x = 5
while x > 0:
    x = x - 2
print(x)
```
- A) 0
- B) -1
- C) 1
- D) 5

## Question 5
Which accumulator value is correct for calculating a product?
- A) 0
- B) 1
- C) None
- D) "" (empty string)

## Question 6
What is a sentinel value?
- A) A value that stops the loop
- B) A value that starts the loop
- C) A syntax error
- D) The loop variable

## Question 7
What does this code print?
```python
i = 0
total = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    total = total + i
print(total)
```
- A) 10
- B) 12
- C) 15
- D) 13

## Answers
1. C — 3 iterations (count = 3, 2, 1)
2. C — The condition never becomes False, causing infinite loop
3. B — Ctrl+C sends SIGINT and stops execution
4. B — x goes: 5, 3, 1, -1 (loop stops when x <= 0)
5. B — Products start at 1; starting at 0 always gives 0
6. A — A sentinel is a special value that signals loop termination
7. B — Added values: 1, 2, (skip 3), 4, 5 = 12
