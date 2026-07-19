# Module 016: Loop Control (break, continue, loop else) — Quiz

## Question 1
What does `break` do inside a loop?
- A) Skips the current iteration
- B) Exits the loop immediately
- C) Restarts the loop
- D) Does nothing

## Question 2
What does `continue` do inside a loop?
- A) Exits the loop immediately
- B) Skips the rest of the current iteration and goes to the next
- C) Restarts the loop from the beginning
- D) Does nothing

## Question 3
What does this code print?
```python
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
```
- A) 0 1 2
- B) 0 1 2 3
- C) 0 1 2 3 4
- D) 0 1 2 4

## Question 4
When does the `else` clause of a loop execute?
- A) Only when `break` was used
- B) Only when the loop ends normally (no `break`)
- C) Always, at the end of every loop
- D) Only if the loop body executes at least once

## Question 5
What does this code print?
```python
for n in range(2, 6):
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        print(n, end=" ")
```
- A) 2 3 4 5
- B) 2 3 5
- C) 3 5
- D) 2 3 4

## Question 6
What is `pass` used for?
- A) To exit a loop
- B) As a placeholder where Python requires a statement
- C) To skip an iteration
- D) To raise an error

## Answers
1. B — `break` exits the innermost loop immediately
2. B — `continue` skips the rest of the current body and jumps to the next iteration
3. A — Prints 0, 1, 2; when i=3, break exits the loop
4. B — The `else` runs only when the loop completes without hitting `break`
5. B — 2, 3, 5 are prime (inner loop finds no divisor for 2, 3, 5; 4 is skipped)
6. B — `pass` is a no-op used as a placeholder for syntactically required blocks
