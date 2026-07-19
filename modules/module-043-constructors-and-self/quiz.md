# Module 043: Quiz

## Question 1 (Multiple Choice)
When is `__init__` called?
- A) When an object is deleted
- B) When a class is defined
- C) Right after an object is created
- D) When a method is called

## Question 2 (Multiple Choice)
Can `__init__` return a value?
- A) Yes, any value
- B) Yes, but only integers
- C) No, it must return None
- D) Only if it's a subclass

## Question 3 (True/False)
If you don't define `__init__`, the class cannot be instantiated.
- True
- False

## Question 4 (Multiple Choice)
What is wrong with this constructor?
```python
class Bad:
    def __init__(self, items=[]):
        self.items = items
```
- A) Nothing
- B) `items` is a mutable default argument shared across instances
- C) `self` is missing
- D) `[]` is invalid syntax

## Question 5 (Multiple Choice)
What is the correct way to fix the mutable default trap?
- A) `def __init__(self, items=None): self.items = items or []`
- B) `def __init__(self, items=list()): self.items = items`
- C) `def __init__(self, items=[]): self.items = items.copy()`
- D) It cannot be fixed

## Question 6 (True/False)
`self` is a Python keyword.
- True
- False

## Question 7 (Multiple Choice)
What does `self` represent?
- A) The class being defined
- B) The current instance of the class
- C) The parent class
- D) The module containing the class

## Question 8 (Multiple Choice)
What happens when you call `obj.method(arg)`?
- A) Python calls `method(obj, arg)`
- B) Python calls `method(arg, obj)`
- C) Python calls `method(arg)` and ignores obj
- D) Python raises an error

## Question 9 (Multiple Choice)
Which method actually creates (allocates memory for) the object?
- A) `__init__`
- B) `__new__`
- C) `__call__`
- D) `__alloc__`

## Question 10 (Short Answer)
Why should you avoid using mutable objects as default arguments in `__init__`?

---

## Answers

1. **C** — Right after an object is created
2. **C** — No, it must return None (raises TypeError otherwise)
3. **False** — Python inherits `object.__init__`
4. **B** — `items` is a mutable default argument shared across instances
5. **A** — `def __init__(self, items=None): self.items = items or []`
6. **False** — It's a naming convention, not a keyword
7. **B** — The current instance of the class
8. **A** — Python calls `method(obj, arg)` (self is passed implicitly)
9. **B** — `__new__`
10. The mutable object is created once at function definition time and shared across all calls. Mutating it in one instance affects all others.
