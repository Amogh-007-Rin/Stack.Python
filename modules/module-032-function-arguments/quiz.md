# Module 032: Quiz

## Question 1 (Multiple Choice)
What are positional arguments?
- A) Arguments passed by position
- B) Arguments with default values
- C) Arguments passed by name
- D) Variable-length arguments

## Question 2 (Multiple Choice)
What is the output?
```python
def f(a, b=2, c=3):
    return a + b + c
print(f(1))
```
- A) 1
- B) 6
- C) 7
- D) Error

## Question 3 (True/False)
Default parameter values are evaluated each time the function is called.
- True
- False

## Question 4 (Multiple Choice)
What does `*args` capture?
- A) Keyword arguments as a dict
- B) Positional arguments as a tuple
- C) Only the first argument
- D) Nothing — it causes an error

## Question 5 (Multiple Choice)
What does `**kwargs` capture?
- A) Positional arguments as a tuple
- B) Keyword arguments as a dict
- C) Default parameter values
- D) The return value

## Question 6 (Multiple Choice)
What is the correct argument order?
- A) `*args, default, positional, **kwargs`
- B) `positional, default, *args, **kwargs`
- C) `**kwargs, *args, default, positional`
- D) `default, **kwargs, positional, *args`

## Question 7 (Multiple Choice)
What does `*[1, 2, 3]` do when calling a function?
- A) Passes the list as one argument
- B) Unpacks the list into three arguments
- C) Creates a tuple from the list
- D) Causes a syntax error

## Question 8 (True/False)
You can use both `*args` and `**kwargs` in the same function.
- True
- False

## Question 9 (Multiple Choice)
What is the output?
```python
def show(*args, **kwargs):
    print(len(args), len(kwargs))
show(1, 2, x=3, y=4)
```
- A) 2 2
- B) 4 0
- C) 0 4
- D) Error

## Question 10 (Short Answer)
Why is `def add(item, items=[])` considered dangerous?

---

## Answers

1. **A** — Arguments passed by position
2. **B** — 6 (1 + 2 + 3)
3. **False** — They are evaluated once at definition time.
4. **B** — Positional arguments as a tuple
5. **B** — Keyword arguments as a dict
6. **B** — positional, default, *args, **kwargs
7. **B** — Unpacks the list into three arguments
8. **True**
9. **A** — 2 2
10. The default list is created once at definition time, so it accumulates state across calls. Use `None` and create a new list inside instead.
