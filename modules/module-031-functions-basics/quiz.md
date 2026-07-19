# Module 031: Quiz

## Question 1 (Multiple Choice)
What does the `def` keyword do?
- A) Deletes a variable
- B) Defines a function
- C) Returns a value
- D) Prints output

## Question 2 (Multiple Choice)
What does a function return if it has no `return` statement?
- A) 0
- B) True
- C) None
- D) An empty string

## Question 3 (True/False)
A parameter is the value passed when calling a function.
- True
- False

## Question 4 (Multiple Choice)
What is the output?
```python
def add(a, b):
    return a + b
print(add(2, 3))
```
- A) 5
- B) (2, 3)
- C) None
- D) Error

## Question 5 (Multiple Choice)
What naming convention should functions follow in Python?
- A) camelCase
- B) PascalCase
- C) snake_case
- D) kebab-case

## Question 6 (True/False)
Variables created inside a function can be accessed outside the function.
- True
- False

## Question 7 (Multiple Choice)
What does the following code print?
```python
x = 5
def f():
    x = 10
f()
print(x)
```
- A) 5
- B) 10
- C) None
- D) Error

## Question 8 (Multiple Choice)
Which is the correct way to call a function named `greet`?
- A) greet
- B) greet()
- C) call greet
- D) run greet

## Question 9 (Multiple Choice)
What is wrong with this code?
```python
def say_hello
    print("Hi")
```
- A) Missing parentheses in the call
- B) Missing colon after `def say_hello`
- C) print is misspelled
- D) Nothing is wrong

## Question 10 (Short Answer)
What is the difference between a parameter and an argument?

---

## Answers

1. **B** — Defines a function
2. **C** — None
3. **False** — A parameter is the placeholder in the definition; the value passed is an argument.
4. **A** — 5
5. **C** — snake_case
6. **False** — They are local to the function.
7. **A** — 5 (the `x = 10` is local to `f`)
8. **B** — greet()
9. **B** — Missing colon after `def say_hello`
10. A **parameter** is the variable listed in the function definition. An **argument** is the value passed when calling the function.
