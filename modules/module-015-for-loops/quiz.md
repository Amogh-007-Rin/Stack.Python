# Module 015: Loops: `for` — Quiz

## Question 1
How many iterations does `for i in range(5):` execute?
- A) 4
- B) 5
- C) 6
- D) Depends on the loop body

## Question 2
What does `range(3, 10, 2)` generate?
- A) 3, 4, 5, 6, 7, 8, 9, 10
- B) 3, 5, 7, 9
- C) 3, 5, 7, 9, 11
- D) 3, 4, 5, 6, 7, 8, 9

## Question 3
What does this code print?
```python
total = 0
for i in range(1, 4):
    total = total + i
print(total)
```
- A) 3
- B) 4
- C) 5
- D) 6

## Question 4
When does the `else` clause of a `for` loop execute?
- A) When the loop variable is even
- B) When the loop ends without `break`
- C) When the loop has at least one iteration
- D) Always

## Question 5
Which loop is better for input validation?
- A) `for`
- B) `while`
- C) Both are equally good
- D) Neither

## Question 6
What is the output of `range(10, 0, -3)` as a list?
- A) [10, 7, 4, 1]
- B) [10, 7, 4, 1, -2]
- C) [10, 7, 4]
- D) [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

## Question 7
True or False: A `for` loop can iterate over a string.
- A) True
- B) False

## Answers
1. B — `range(5)` is 0, 1, 2, 3, 4 — 5 values
2. B — Start at 3, stop before 10, step by 2: 3, 5, 7, 9
3. D — Adds 1 + 2 + 3 = 6
4. B — The `else` runs only when the loop completes without hitting `break`
5. B — `while` is better when you don't know the number of iterations
6. A — 10, 7, 4, 1 (stops before 0)
7. A — Strings are iterable in Python
