# Module 037: Quiz

## Question 1 (Multiple Choice)
What is a decorator?
- A) A function that modifies another function
- B) A class that inherits from another
- C) A type of variable
- D) A built-in Python module

## Question 2 (Multiple Choice)
What does `@decorator` mean?
- A) `func = decorator(func)`
- B) `func = decorator`
- C) `func = func(decorator)`
- D) `decorator = func`

## Question 3 (True/False)
A decorator must always return a function.
- True
- False

## Question 4 (Multiple Choice)
Why should you use `@wraps` from `functools`?
- A) To make code run faster
- B) To preserve the original function's metadata
- C) To prevent errors
- D) To add type checking

## Question 5 (Multiple Choice)
What is the output?
```python
def shout(func):
    def wrapper():
        return func().upper()
    return wrapper

@shout
def greet():
    return "hello"

print(greet())
```
- A) hello
- B) HELLO
- C) shout
- D) wrapper

## Question 6 (True/False)
When applying `@a @b def f()`, `a` is applied first, then `b`.
- True
- False

## Question 7 (Multiple Choice)
What does `*args` and `**kwargs` in a decorator wrapper provide?
- A) Error handling
- B) Flexibility for any function arguments
- C) Type conversion
- D) Nothing special

## Question 8 (Multiple Choice)
What is a closure?
- A) A function that closes a file
- B) A nested function that captures variables from its enclosing scope
- C) A way to close a program
- D) A type of loop

## Question 9 (Multiple Choice)
What happens if you forget `@wraps` on a decorator?
- A) The program crashes
- B) The function loses its original name and docstring
- C) The decorator doesn't work
- D) Nothing changes

## Question 10 (Short Answer)
What is the order of execution when applying multiple decorators?

---

## Answers

1. **A** — A function that modifies another function
2. **A** — `func = decorator(func)`
3. **True** — It must return a callable (usually a function)
4. **B** — To preserve the original function's metadata
5. **B** — HELLO
6. **False** — `b` is applied first (closest to function), then `a`
7. **B** — Flexibility for any function arguments
8. **B** — A nested function that captures variables from its enclosing scope
9. **B** — The function loses its original name and docstring
10. The decorator closest to the function is applied first, working outward. For `@a @b def f()`, it's `a(b(f))`.
