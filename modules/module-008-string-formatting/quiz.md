# Module 008: Quiz

## Question 1 (Multiple Choice)
What prefix is used for f-strings?
- A) `s`
- B) `f`
- C) `p`
- D) No prefix needed

## Question 2 (What does this output?)
```python
name = "Alice"
print(f"Hello, {name}")
```

## Question 3 (Multiple Choice)
What does `f"{3.14159:.2f}"` produce?
- A) "3.14"
- B) "3.14159"
- C) "3.1"
- D) "3.142"

## Question 4 (Multiple Choice)
Which alignment character centers text in a format specifier?
- A) `<`
- B) `>`
- C) `^`
- D) `~`

## Question 5 (What does this output?)
```python
value = 7
print(f"|{value:*^10}|")
```

## Question 6 (Multiple Choice)
What is the modern, recommended way to format strings in Python 3.12?
- A) `%`-formatting
- B) `.format()` method
- C) f-strings
- D) Template strings

## Question 7 (Short Answer)
Write an f-string that prints the number `255` in a field of width 5, right-aligned, with `0` as fill character.

## Question 8 (Multiple Choice)
What does this code print?
```python
score = 85
total = 100
print("Score: {} / {}".format(score, total))
```
- A) Score: 85 / 100
- B) Score: {} / {}
- C) Score: score / total
- D) Error

---

## Answers

1. **B** — `f`
2. **Hello, Alice**
3. **A** — "3.14"
4. **C** — `^`
5. **`|****7****|`** (centered, * fill, width 10)
6. **C** — f-strings
7. **`f"{255:0>5}"`** or **`f"{255:0>5d}"`**
8. **A** — Score: 85 / 100
