# Module 034: Quiz

## Question 1 (Multiple Choice)
What keyword creates a lambda function?
- A) def
- B) lambda
- C) fn
- D) function

## Question 2 (Multiple Choice)
What is the output?
```python
f = lambda x: x * 2
print(f(3))
```
- A) 3
- B) 6
- C) 9
- D) Error

## Question 3 (True/False)
A lambda function can contain multiple statements.
- True
- False

## Question 4 (Multiple Choice)
What does `sorted([3, 1, 2], key=lambda x: -x)` return?
- A) [1, 2, 3]
- B) [3, 2, 1]
- C) [3, 1, 2]
- D) Error

## Question 5 (Multiple Choice)
What is the output?
```python
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```
- A) [1, 3]
- B) [2, 4]
- C) [1, 2, 3, 4]
- D) []

## Question 6 (True/False)
A lambda can have a docstring.
- True
- False

## Question 7 (Multiple Choice)
What is the output?
```python
f = lambda a, b: a if a > b else b
print(f(5, 8))
```
- A) 5
- B) 8
- C) (5, 8)
- D) Error

## Question 8 (Multiple Choice)
What does `map(lambda x: x ** 2, [1, 2, 3])` return?
- A) [1, 4, 9]
- B) A map object
- C) (1, 4, 9)
- D) Error

## Question 9 (Multiple Choice)
Which function can ONLY have one expression?
- A) A regular function defined with `def`
- B) A lambda function
- C) Both
- D) Neither

## Question 10 (Short Answer)
When should you use `def` instead of `lambda`?

---

## Answers

1. **B** — lambda
2. **B** — 6
3. **False** — Only a single expression
4. **B** — [3, 2, 1] (reverse sort)
5. **B** — [2, 4]
6. **False** — Lambdas cannot have docstrings
7. **B** — 8
8. **B** — Returns a map object; use `list()` to get the result
9. **B** — A lambda function
10. When the function is complex (multiple expressions/statements), needs a docstring, or will be reused.
