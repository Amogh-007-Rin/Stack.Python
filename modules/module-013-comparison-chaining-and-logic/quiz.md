# Module 013: Comparison Chaining & Logical Operators Deep Dive — Quiz

## Question 1
What does `print(1 < 5 < 10)` output?
- A) True
- B) False
- C) Error
- D) `1 5 10`

## Question 2
What is the value of `3 > 5 and 10 < 20`?
- A) True
- B) False
- C) 10
- D) 3

## Question 3
Which of the following is the De Morgan's equivalent of `not (x > 0 and y < 10)`?
- A) `(x <= 0) or (y >= 10)`
- B) `(x <= 0) and (y >= 10)`
- C) `(x > 0) or (y < 10)`
- D) `not x > 0 and not y < 10`

## Question 4
What is the difference between `is` and `==`?
- A) `is` checks value, `==` checks identity
- B) `is` checks identity, `==` checks value
- C) They are exactly the same
- D) `is` can only be used with numbers

## Question 5
What does `print("e" in "hello")` output?
- A) True
- B) False
- C) Error
- D) 1

## Question 6
Which operator has the **highest** precedence: `and`, `or`, or `not`?
- A) `and`
- B) `or`
- C) `not`
- D) They all have the same precedence

## Question 7
What does `print(0 and 5 or 10 and 20)` output?
- A) 0
- B) 5
- C) 10
- D) 20

## Question 8
What is the correct way to check if a variable `x` is **not** `None`?
- A) `if x != None:`
- B) `if not x is None:`
- C) `if x is not None:`
- D) `if x:`

## Answers
1. A — Chained comparison: `1 < 5` is True and `5 < 10` is True
2. B — `3 > 5` is False, `and` short-circuits to False
3. A — `not (A and B)` = `(not A) or (not B)` = `(x <= 0) or (y >= 10)`
4. B — `is` checks identity (same object), `==` checks equality (same value)
5. A — `"e"` is in `"hello"` at index 1
6. C — Precedence: `not` > `and` > `or`
7. D — `0 and 5` → `0`; `0 or 10` → `10`; `10 and 20` → `20`
8. C — `x is not None` is the idiomatic way
