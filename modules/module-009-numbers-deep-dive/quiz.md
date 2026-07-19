# Module 009: Quiz

## Question 1 (True/False)
Python integers can overflow like in many other languages.
- True
- False

## Question 2 (Multiple Choice)
What does `0.1 + 0.2 == 0.3` evaluate to?
- A) True
- B) False
- C) Error
- D) Depends on the system

## Question 3 (Multiple Choice)
Which function from the `math` module rounds a number UP to the nearest integer?
- A) `math.floor()`
- B) `math.round()`
- C) `math.ceil()`
- D) `math.trunc()`

## Question 4 (What does this output?)
```python
import math
print(math.floor(3.9))
```

## Question 5 (Multiple Choice)
What does `round(2.5)` return?
- A) 3
- B) 2
- C) 3.0
- D) 2.0

## Question 6 (Multiple Choice)
What does `math.sqrt(25)` return?
- A) 5
- B) 5.0
- C) 25
- D) 12.5

## Question 7 (Short Answer)
Name two functions from the `math` module that relate to rounding.

## Question 8 (Multiple Choice)
What is the value of `abs(3 + 4j)`?
- A) 5
- B) 7
- C) 3
- D) 4

---

## Answers

1. **False** — Python integers have arbitrary precision
2. **B** — False (due to floating-point imprecision)
3. **C** — `math.ceil()`
4. **3** (floor rounds down)
5. **B** — 2 (bankers' rounding: rounds half to even)
6. **B** — 5.0 (math.sqrt always returns a float)
7. **`math.ceil()` and `math.floor()`** (or `round()` built-in and `math.trunc()`)
8. **A** — 5 (`sqrt(3^2 + 4^2) = sqrt(25) = 5`)
