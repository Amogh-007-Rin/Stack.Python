# Quiz: Comprehensions Deep Dive

## Question 1
What is the output of `[x**2 for x in range(4)]`?
- A) [0, 1, 4, 9]
- B) [1, 4, 9, 16]
- C) [0, 1, 2, 3]
- D) [0, 1, 4, 9, 16]

## Question 2
Which comprehension uses parentheses `()`?
- A) List comprehension
- B) Dict comprehension
- C) Set comprehension
- D) Generator expression

## Question 3
What does `{x: x**2 for x in range(3)}` produce?
- A) {0: 0, 1: 1, 2: 4}
- B) {0, 1, 4}
- C) [0, 1, 4]
- D) (0, 1, 4)

## Question 4
Which of the following flattens `[[1,2],[3,4]]`?
- A) `[x for x in row for row in matrix]`
- B) `[item for row in matrix for item in row]`
- C) `[row for item in matrix for row in item]`
- D) `[matrix[row][col] for row in range(2) for col in range(2)]`

## Question 5
Generator expressions are preferred over list comprehensions when:
- A) You need to reuse the data multiple times
- B) Memory efficiency is important for large sequences
- C) You need random access to elements
- D) You need to modify elements in place

## Answer Key
1-A, 2-D, 3-A, 4-B, 5-B
