# Module 042: Quiz

## Question 1 (Multiple Choice)
How do you define an instance attribute inside a class?
- A) `attr = value`
- B) `self.attr = value`
- C) `this.attr = value`
- D) `instance.attr = value`

## Question 2 (Multiple Choice)
What is the first parameter of every instance method?
- A) `cls`
- B) `this`
- C) `self`
- D) `instance`

## Question 3 (True/False)
A method is a function defined inside a class.
- True
- False

## Question 4 (Multiple Choice)
What happens if you call `obj.method` without parentheses?
- A) The method executes
- B) It returns the method object
- C) It raises an error
- D) It returns None

## Question 5 (Multiple Choice)
Can you add a new attribute to an instance after it's created?
- A) No, attributes are fixed at creation
- B) Yes, Python allows dynamic attribute addition
- C) Only if defined in `__slots__`
- D) Only for built-in types

## Question 6 (True/False)
A standalone function and a method are identical in every way.
- True
- False

## Question 7 (Multiple Choice)
What does this code print?
```python
class A:
    def __init__(self):
        self.x = 1

a = A()
a.x = 2
print(a.x)
```
- A) 1
- B) 2
- C) Error
- D) None

## Question 8 (Multiple Choice)
What is the best place to define all expected instance attributes?
- A) In a separate config file
- B) In `__init__`
- C) Just before using them
- D) In a global variable

## Question 9 (Multiple Choice)
Which method is called when you create a new instance?
- A) `__new__`
- B) `__init__`
- C) `__call__`
- D) `__del__`

## Question 10 (Short Answer)
What is the difference between a method and a function?

---

## Answers

1. **B** — `self.attr = value`
2. **C** — `self`
3. **True**
4. **B** — It returns the method object (a bound method)
5. **B** — Yes, Python allows dynamic attribute addition
6. **False** — A method receives `self` and is bound to an instance
7. **B** — 2
8. **B** — In `__init__`
9. **B** — `__init__`
10. A function is defined standalone and called directly. A method is defined inside a class, receives `self` (the instance), and is called on an instance.
