# Module 048: Quiz

## Question 1 (Multiple Choice)
What does `__repr__` return?
- A) A readable string for end users
- B) An unambiguous representation for developers
- C) A hash value
- D) The object's memory address

## Question 2 (Multiple Choice)
What does `__str__` return?
- A) A readable string for end users
- B) An unambiguous representation for developers
- C) A hash value
- D) The object's type

## Question 3 (True/False)
`print(obj)` calls `__repr__` on the object.
- True
- False

## Question 4 (Multiple Choice)
If only `__repr__` is defined, what happens when you call `str(obj)`?
- A) It raises TypeError
- B) It falls back to `__repr__`
- C) It returns "" (empty string)
- D) It returns "None"

## Question 5 (Multiple Choice)
When you define `__eq__`, why should you also define `__hash__`?
- A) It's optional but recommended for consistent hashing with equality
- B) It's required by Python syntax
- C) To make the object iterable
- D) To enable string conversion

## Question 6 (True/False)
Implementing `__getitem__` allows your object to support indexing with square brackets.
- True
- False

## Question 7 (Multiple Choice)
What does `__call__` do?
- A) Makes an object callable like a function
- B) Called when the object is created
- C) Called when the object is deleted
- D) Returns a string representation

## Question 8 (Multiple Choice)
Which dunder method defines the behavior of `len(obj)`?
- A) `__length__`
- B) `__len__`
- C) `__size__`
- D) `__count__`

## Question 9 (Multiple Choice)
Which dunder method defines truthiness for `if obj:` checks?
- A) `__bool__`
- B) `__true__`
- C) `__truthy__`
- D) `__if__`

## Question 10 (Short Answer)
What is the difference between `__str__` and `__repr__`, and when is each used?

---

## Answers

1. **B** — An unambiguous representation for developers
2. **A** — A readable string for end users
3. **False** — It calls `__str__`
4. **B** — It falls back to `__repr__`
5. **A** — It's optional but recommended for consistent hashing with equality (objects that are equal should hash the same)
6. **True**
7. **A** — Makes an object callable like a function
8. **B** — `__len__`
9. **A** — `__bool__`
10. `__repr__` returns an unambiguous string meant for developers (ideally reproducing the object). `__str__` returns a readable string for end users. `repr()` uses `__repr__`; `print()` and `str()` use `__str__` (falling back to `__repr__` if not defined).
