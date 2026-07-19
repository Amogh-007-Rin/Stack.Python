# Module 041: Quiz

## Question 1 (Multiple Choice)
What is a class in Python?
- A) A function that returns data
- B) A blueprint for creating objects
- C) A type of variable
- D) A module containing functions

## Question 2 (Multiple Choice)
What keyword is used to define a class?
- A) `struct`
- B) `object`
- C) `class`
- D) `def`

## Question 3 (True/False)
An object is an instance of a class.
- True
- False

## Question 4 (Multiple Choice)
What is the purpose of `__init__` in a class?
- A) To delete an object
- B) To initialize a new object's attributes
- C) To print the object
- D) To define a static method

## Question 5 (Multiple Choice)
What does `self` refer to inside a class method?
- A) The class itself
- B) The current instance
- C) The parent class
- D) A global variable

## Question 6 (True/False)
You must always define `__init__` in every Python class.
- True
- False

## Question 7 (Multiple Choice)
What is the output?
```python
class Greeter:
    def greet(self):
        print("Hello!")

g = Greeter()
g.greet()
```
- A) `Hello!`
- B) `<function Greeter.greet at ...>`
- C) Error
- D) None

## Question 8 (Multiple Choice)
How do you create an instance of a class named `Car`?
- A) `Car.new()`
- B) `Car.create()`
- C) `Car()`
- D) `new Car()`

## Question 9 (Multiple Choice)
What is the main benefit of OOP over procedural programming?
- A) It runs faster
- B) It uses less memory
- C) It bundles data and behavior together
- D) It doesn't require functions

## Question 10 (Short Answer)
Explain the difference between a class and an object in your own words.

---

## Answers

1. **B** — A blueprint for creating objects
2. **C** — `class`
3. **True**
4. **B** — To initialize a new object's attributes
5. **B** — The current instance
6. **False** — Python uses a default `__init__` from `object`
7. **A** — `Hello!`
8. **C** — `Car()`
9. **C** — It bundles data and behavior together
10. A class is a blueprint or template that defines the structure and behavior of objects. An object is a concrete instance created from that class, with its own specific data values.
