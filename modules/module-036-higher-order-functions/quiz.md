# Module 036: Quiz

## Question 1 (Multiple Choice)
What does `map()` return?
- A) A list
- B) A map/iterator object
- C) A tuple
- D) None

## Question 2 (Multiple Choice)
What is the output?
```python
result = list(filter(lambda x: x > 2, [1, 2, 3, 4]))
print(result)
```
- A) [1, 2]
- B) [3, 4]
- C) [1, 2, 3, 4]
- D) []

## Question 3 (True/False)
`reduce()` is a built-in function that requires no import.
- True
- False

## Question 4 (Multiple Choice)
What does the following return?
```python
sorted(["cat", "banana", "apple"], key=len)
```
- A) ["apple", "banana", "cat"]
- B) ["cat", "apple", "banana"]
- C) ["banana", "apple", "cat"]
- D) ["cat", "banana", "apple"]

## Question 5 (Multiple Choice)
What is the output?
```python
from functools import reduce
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))
```
- A) 10
- B) 24
- C) 12
- D) 30

## Question 6 (True/False)
Functions in Python are first-class objects.
- True
- False

## Question 7 (Multiple Choice)
What does this code do?
```python
list(map(str.upper, ["a", "b", "c"]))
```
- A) Converts to lowercase
- B) Converts to uppercase
- C) Returns ["a", "b", "c"]
- D) Returns ["A", "B", "C"]

## Question 8 (Multiple Choice)
Which function selects elements based on a condition?
- A) map()
- B) filter()
- C) reduce()
- D) sorted()

## Question 9 (Multiple Choice)
What is the output?
```python
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))
```
- A) 5
- B) 10
- C) 15
- D) 50

## Question 10 (Short Answer)
What is the difference between `map()` and `filter()`?

---

## Answers

1. **B** — A map/iterator object
2. **B** — [3, 4]
3. **False** — It's in `functools`
4. **B** — ["cat", "apple", "banana"] (sorted by length ascending)
5. **B** — 24
6. **True**
7. **D** — ["A", "B", "C"]
8. **B** — filter()
9. **C** — 15
10. `map()` transforms every element; `filter()` keeps only elements where the predicate is True.
