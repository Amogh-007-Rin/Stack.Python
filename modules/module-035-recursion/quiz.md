# Module 035: Quiz

## Question 1 (Multiple Choice)
What are the two essential parts of a recursive function?
- A) Loop and break
- B) Base case and recursive case
- C) Input and output
- D) Try and except

## Question 2 (Multiple Choice)
What is the output?
```python
def f(n):
    if n <= 1:
        return 1
    return n + f(n - 1)
print(f(3))
```
- A) 3
- B) 4
- C) 6
- D) 7

## Question 3 (True/False)
Python optimizes tail recursion to avoid stack overflow.
- True
- False

## Question 4 (Multiple Choice)
What error occurs when recursion depth exceeds the limit?
- A) SyntaxError
- B) RecursionError
- C) IndexError
- D) ValueError

## Question 5 (Multiple Choice)
What is the base case in `factorial(n)`?
- A) n < 0
- B) n <= 1
- C) n == 10
- D) n is None

## Question 6 (Multiple Choice)
What is the default recursion limit in Python?
- A) 100
- B) 500
- C) 1000
- D) 5000

## Question 7 (True/False)
A recursive function must always call itself.
- True
- False

## Question 8 (Multiple Choice)
What is the 6th Fibonacci number (fib(6))?
- A) 5
- B) 8
- C) 13
- D) 21

## Question 9 (Multiple Choice)
Which approach is generally more memory-efficient for deep recursion?
- A) Recursion
- B) Iteration
- C) Both are equal
- D) Neither

## Question 10 (Short Answer)
What happens if a recursive function has no base case?

---

## Answers

1. **B** — Base case and recursive case
2. **C** — 6 (3 + 2 + 1)
3. **False** — Python does not optimize tail recursion
4. **B** — RecursionError
5. **B** — n <= 1
6. **C** — 1000
7. **False** — It must call itself, but if the base case is always reached, it might not call itself on the final call
8. **B** — 8 (0, 1, 1, 2, 3, 5, 8)
9. **B** — Iteration (constant stack usage)
10. It will call itself infinitely until a RecursionError (stack overflow) occurs.
