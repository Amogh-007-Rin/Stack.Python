# Module 038: Quiz

## Question 1 (Multiple Choice)
What keyword is used in a generator function instead of `return`?
- A) break
- B) yield
- C) continue
- D) emit

## Question 2 (Multiple Choice)
What happens when a generator function reaches the end without yielding?
- A) Returns None
- B) Raises StopIteration
- C) Raises GeneratorExit
- D) Loops back to the beginning

## Question 3 (True/False)
A generator can be iterated over multiple times.
- True
- False

## Question 4 (Multiple Choice)
Which uses less memory for large sequences?
- A) List comprehension
- B) Generator expression
- C) Both are the same
- D) Neither

## Question 5 (Multiple Choice)
What does `yield from` do?
- A) Yields from a specific index
- B) Delegates to another generator
- C) Yields the same value multiple times
- D) Stops the generator

## Question 6 (True/False)
A generator function can have multiple `yield` statements.
- True
- False

## Question 7 (Multiple Choice)
What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(list(g))
print(list(g))
```
- A) [1, 2, 3] [1, 2, 3]
- B) [1, 2, 3] []
- C) [1, 2, 3] [1]
- D) [] []

## Question 8 (Multiple Choice)
What is the main advantage of a generator over a list?
- A) Faster execution
- B) Memory efficiency
- C) Reusability
- D) Easier to write

## Question 9 (Multiple Choice)
What type of object does a generator function return?
- A) Function
- B) List
- C) Generator object
- D) Tuple

## Question 10 (Short Answer)
Explain what "lazy evaluation" means in the context of generators.

---

## Answers

1. **B** — yield
2. **B** — Raises StopIteration
3. **False** — A generator is exhausted after one iteration
4. **B** — Generator expression
5. **B** — Delegates to another generator
6. **True**
7. **B** — [1, 2, 3] [] (generator is exhausted)
8. **B** — Memory efficiency
9. **C** — Generator object
10. Lazy evaluation means values are computed on demand, only when requested by `next()` or iteration, rather than all at once.
