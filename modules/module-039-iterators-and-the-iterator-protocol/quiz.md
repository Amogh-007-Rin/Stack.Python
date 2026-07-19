# Module 039: Quiz

## Question 1 (Multiple Choice)
What method must an iterator implement?
- A) __iter__() only
- B) __next__() only
- C) Both __iter__() and __next__()
- D) __getitem__()

## Question 2 (Multiple Choice)
What does `iter([1, 2, 3])` return?
- A) A list
- B) An iterator object
- C) A tuple
- D) A generator

## Question 3 (True/False)
A list is an iterator.
- True
- False

## Question 4 (Multiple Choice)
What is used to signal that an iterator is exhausted?
- A) Return None
- B) IndexError
- C) StopIteration
- D) GeneratorExit

## Question 5 (Multiple Choice)
What is the output?
```python
it = iter([1, 2, 3])
print(next(it))
print(next(it))
```
- A) 1 2
- B) [1, 2]
- C) 1 3
- D) Error

## Question 6 (True/False)
A generator is a type of iterator.
- True
- False

## Question 7 (Multiple Choice)
What does this code simulate?
```python
_it = iter(iterable)
while True:
    try:
        item = next(_it)
    except StopIteration:
        break
```
- A) A while loop
- B) A for loop
- C) List comprehension
- D) A function call

## Question 8 (Multiple Choice)
Can an iterator be used in multiple for loops?
- A) Yes, always
- B) No, it's exhausted after one pass
- C) Yes, but only with small data
- D) Only if it's a list

## Question 9 (Multiple Choice)
What is the key difference between an iterable and an iterator?
- A) Iterables have __next__; iterators have __iter__
- B) Iterators are mutable; iterables are immutable
- C) Iterators track their state; iterables do not
- D) There is no difference

## Question 10 (Short Answer)
How does a `for` loop work internally in terms of the iterator protocol?

---

## Answers

1. **C** — Both __iter__() and __next__()
2. **B** — An iterator object
3. **False** — A list is an iterable, not an iterator
4. **C** — StopIteration
5. **A** — 1 2
6. **True**
7. **B** — A for loop
8. **B** — No, it's exhausted after one pass
9. **C** — Iterators track their state; iterables do not
10. Python calls `iter()` on the iterable to get an iterator, then calls `next()` on it in a loop, catching `StopIteration` to exit.
