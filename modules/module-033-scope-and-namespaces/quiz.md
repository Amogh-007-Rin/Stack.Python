# Module 033: Quiz

## Question 1 (Multiple Choice)
What does LEGB stand for?
- A) Local, External, Global, Built-in
- B) Local, Enclosing, Global, Built-in
- C) List, Enumerate, Generate, Break
- D) Loop, Exit, Guard, Branch

## Question 2 (Multiple Choice)
What does the `global` keyword do?
- A) Creates a new global variable
- B) Allows modifying a global variable inside a function
- C) Deletes a global variable
- D) Makes a function globally available

## Question 3 (True/False)
A function can always read a global variable without any special keyword.
- True
- False

## Question 4 (Multiple Choice)
What does `nonlocal` do?
- A) Accesses a global variable
- B) Modifies a variable in an enclosing function scope
- C) Creates a new local variable
- D) Deletes an enclosing variable

## Question 5 (Multiple Choice)
What is the output?
```python
x = 1
def outer():
    x = 2
    def inner():
        print(x)
    inner()
outer()
```
- A) 1
- B) 2
- C) Error
- D) None

## Question 6 (True/False)
Shadowing means a local variable has the same name as a variable in an outer scope.
- True
- False

## Question 7 (Multiple Choice)
What is the output?
```python
x = 5
def func():
    x = 10
    return x
print(func())
print(x)
```
- A) 10 5
- B) 5 10
- C) 10 10
- D) 5 5

## Question 8 (Multiple Choice)
Which scope is checked FIRST by Python?
- A) Global
- B) Built-in
- C) Local
- D) Enclosing

## Question 9 (True/False)
You can use `nonlocal` at the module level.
- True
- False

## Question 10 (Short Answer)
What is the difference between `global` and `nonlocal`?

---

## Answers

1. **B** — Local, Enclosing, Global, Built-in
2. **B** — Allows modifying a global variable inside a function
3. **True** — Reading is fine; modifying requires `global`
4. **B** — Modifies a variable in an enclosing function scope
5. **B** — 2 (enclosing scope of `outer`)
6. **True**
7. **A** — 10 5
8. **C** — Local
9. **False** — `nonlocal` is only valid inside a nested function
10. `global` refers to the module-level scope; `nonlocal` refers to the nearest enclosing function scope (not global).
