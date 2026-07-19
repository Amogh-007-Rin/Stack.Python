# Module 044: Quiz

## Question 1 (Multiple Choice)
Where are class variables defined?
- A) Inside methods with `self`
- B) Outside any method, directly in the class body
- C) In a separate config module
- D) Inside `__init__` without `self`

## Question 2 (Multiple Choice)
Class variables are:
- A) Unique to each instance
- B) Shared across all instances
- C) Private to the class
- D) Only accessible from the class, not instances

## Question 3 (True/False)
Instance variables are defined using `self.attr` inside methods.
- True
- False

## Question 4 (Multiple Choice)
What happens when you assign `instance.class_var = value`?
- A) The class variable is modified for all instances
- B) A new instance variable is created, shadowing the class variable
- C) An error occurs
- D) The class variable is deleted

## Question 5 (Multiple Choice)
What does `p.__dict__` return for an instance `p`?
- A) The class definition
- B) A dict of the instance's attributes
- C) The source code of the class
- D) The memory address

## Question 6 (True/False)
Modifying a mutable class variable (like a list) through one instance affects all instances.
- True
- False

## Question 7 (Multiple Choice)
What is the output?
```python
class A:
    val = 1

a1 = A()
a2 = A()
A.val = 2
print(a1.val, a2.val)
```
- A) 1 1
- B) 2 2
- C) 1 2
- D) 2 1

## Question 8 (Multiple Choice)
When should you use a class variable?
- A) When each instance needs its own unique data
- B) When data should be shared across all instances
- C) When you want to hide data from users
- D) Never — always use instance variables

## Question 9 (Multiple Choice)
Which is true about class variables?
- A) They can only be integers
- B) They are accessed via `self.var` or `ClassName.var`
- C) They cannot be modified
- D) They are only accessible inside `__init__`

## Question 10 (Short Answer)
What is the difference between a class variable and an instance variable?

---

## Answers

1. **B** — Outside any method, directly in the class body
2. **B** — Shared across all instances
3. **True**
4. **B** — A new instance variable is created, shadowing the class variable
5. **B** — A dict of the instance's attributes
6. **True** — Because they reference the same mutable object
7. **B** — 2 2
8. **B** — When data should be shared across all instances
9. **B** — They are accessed via `self.var` or `ClassName.var`
10. A class variable is defined at the class level and shared by all instances. An instance variable is defined with `self.attr` and is unique to each instance.
