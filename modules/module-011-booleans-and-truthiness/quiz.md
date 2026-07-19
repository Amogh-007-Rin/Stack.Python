# Module 011: Booleans and Truthiness — Quiz

## Question 1
Which of the following values is **falsy** in Python? (Select all that apply)
- A) `0`
- B) `-1`
- C) `""`
- D) `"False"`
- E) `None`

## Question 2
What is the output of `print(3 and 0 and 5)`?
- A) `True`
- B) `False`
- C) `0`
- D) `5`

## Question 3
What is the output of `print("" or "hello" or "world")`?
- A) `True`
- B) `""`
- C) `"hello"`
- D) `"world"`

## Question 4
What does `bool(" ")` (a single space) return?
- A) `False`
- B) `True`
- C) `None`
- D) `""`

## Question 5
Which of these expressions evaluates to `True`?
- A) `not True`
- B) `False and True`
- C) `True or False`
- D) `not (True or False)`

## Question 6
If `x = 0`, what is the value of `x and 10 / x`?
- A) `0`
- B) `10`
- C) `ZeroDivisionError`
- D) `True`

## Question 7
What does `bool([])` return?
- A) `True`
- B) `False`
- C) `None`
- D) `[]`

## Question 8
Fill in the blank: The expression `not (A and B)` is equivalent to `__________`.
- A) `(not A) and (not B)`
- B) `(not A) or (not B)`
- C) `not A and B`
- D) `A or not B`

## Answers
1. A, C, E (0, empty string, None are falsy)
2. C — `3 and 0` → `0` (falsy short-circuits); `0 and 5` → `0`
3. C — `""` is falsy, so `"" or "hello"` → `"hello"` (truthy, short-circuits)
4. B — A space is a non-empty string, so `True`
5. C — `True or False` → `True`
6. A — `0` is falsy, `and` short-circuits before division
7. B — Empty list is falsy
8. B — De Morgan's law: `not (A and B)` = `(not A) or (not B)`
