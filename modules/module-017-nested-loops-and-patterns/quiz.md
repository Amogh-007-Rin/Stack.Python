# Module 017: Nested Loops and Pattern Printing — Quiz

## Question 1
How many times does the inner loop body execute?
```python
for i in range(3):
    for j in range(4):
        print("x")
```
- A) 7
- B) 12
- C) 3
- D) 4

## Question 2
What does this code print?
```python
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()
```
- A) ```
*
**
***
```
- B) ```
***
**
*
```
- C) ```
*
*
*
```
- D) ```
*
**
***
****
```

## Question 3
What is the time complexity of two nested loops each running `n` times?
- A) O(n)
- B) O(n²)
- C) O(log n)
- D) O(2n)

## Question 4
What does `end=""` do in a `print()` call?
- A) Adds a newline at the end
- B) Keeps the output on the same line
- C) Ends the program
- D) Converts to uppercase

## Question 5
In a diamond pattern with height 5, how many total stars are in the widest row?
- A) 5
- B) 7
- C) 9
- D) 11

## Question 6
How would you create a right-aligned triangle of stars?
- A) Print stars, then spaces
- B) Print spaces, then stars
- C) Print only stars with no spaces
- D) Print numbers instead

## Answers
1. B — 3 × 4 = 12 iterations
2. A — Row 1: 1 star; Row 2: 2 stars; Row 3: 3 stars
3. B — n × n = n² operations, which is O(n²)
4. B — `end=""` replaces the default newline, keeping output on the same line
5. C — The widest row is `2 * 5 - 1 = 9` stars
6. B — Print spaces first (to right-align), then stars
