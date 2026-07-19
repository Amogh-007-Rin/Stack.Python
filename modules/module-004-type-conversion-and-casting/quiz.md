# Module 004: Quiz

## Question 1 (Multiple Choice)
What does `int(3.99)` return?
- A) 4
- B) 3.99
- C) 3
- D) 4.0

## Question 2 (Multiple Choice)
What does `float("42")` return?
- A) "42"
- B) 42
- C) 42.0
- D) Error

## Question 3 (True/False)
`bool("False")` returns `False`.
- True
- False

## Question 4 (What does this output?)
```python
value = "10"
print(int(value) + 5)
```

## Question 5 (Multiple Choice)
Why does `int("3.14")` cause an error?
- A) Strings cannot be converted to int
- B) "3.14" contains a decimal point, which is invalid for int()
- C) int() only works on floats
- D) Python does not have int conversion

## Question 6 (Short Answer)
What is the output of `print(10 + True)`?

## Question 7 (Multiple Choice)
What is the correct way to convert `"3.14"` to an integer 3?
- A) `int("3.14")`
- B) `float("3.14")`
- C) `int(float("3.14"))`
- D) `str("3.14")`

## Question 8 (Multiple Choice)
Which of these evaluates to `False`?
- A) `bool(1)`
- B) `bool(-1)`
- C) `bool(0)`
- D) `bool("0")`

---

## Answers

1. **C** — 3 (truncation)
2. **C** — 42.0
3. **False** — Any non-empty string is `True`
4. **15**
5. **B** — "3.14" contains a decimal point, which is invalid for int()
6. **11** (True is treated as 1)
7. **C** — `int(float("3.14"))`
8. **C** — `bool(0)` is False; `bool("0")` is True (non-empty string)
