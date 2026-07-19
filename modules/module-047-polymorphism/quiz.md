# Module 047: Quiz

## Question 1 (Multiple Choice)
What is polymorphism?
- A) Using only one type of object
- B) Same interface, different behavior depending on the object type
- C) A way to make classes private
- D) A method that returns multiple values

## Question 2 (Multiple Choice)
What is duck typing?
- A) A type of variable that can hold any value
- B) If an object has the required methods, it's treated as the right type
- C) A way to convert between types
- D) A method that checks object types

## Question 3 (True/False)
Polymorphism requires inheritance.
- True
- False

## Question 4 (Multiple Choice)
Which built-in function demonstrates polymorphism?
- A) `print()`
- B) `len()`
- C) `type()`
- D) `id()`

## Question 5 (Multiple Choice)
What is a protocol in Python?
- A) A formal interface defined with `abc`
- B) An informal interface defined by implementing specific methods
- C) A network communication standard
- D) A type of variable

## Question 6 (True/False)
Duck typing means checking the type of an object before calling its methods.
- True
- False

## Question 7 (Multiple Choice)
What does this code demonstrate?
```python
class A:
    def go(self):
        return "A"

class B:
    def go(self):
        return "B"

def run(obj):
    print(obj.go())

run(A())
run(B())
```
- A) Inheritance
- B) Encapsulation
- C) Duck typing / polymorphism
- D) Constructor overloading

## Question 8 (Multiple Choice)
What is method overriding?
- A) Defining the same method in a subclass that exists in the parent
- B) Calling a method multiple times
- C) Deleting a method from a class
- D) Copying a method to another class

## Question 9 (Multiple Choice)
Which statement is true about `len()`?
- A) It only works on strings
- B) It works on any object that has `__len__`
- C) It only works on lists
- D) It requires inheritance from a specific class

## Question 10 (Short Answer)
Explain "if it walks like a duck and quacks like a duck, it's a duck" in the context of Python.

---

## Answers

1. **B** — Same interface, different behavior depending on the object type
2. **B** — If an object has the required methods, it's treated as the right type
3. **False** — Duck typing allows polymorphism without inheritance
4. **B** — `len()`
5. **B** — An informal interface defined by implementing specific methods
6. **False** — Duck typing doesn't check types, it checks for method existence at call time
7. **C** — Duck typing / polymorphism
8. **A** — Defining the same method in a subclass that exists in the parent
9. **B** — It works on any object that has `__len__`
10. It means Python doesn't care about the actual type of an object — if it has the methods you're calling, that's enough. You can call `quack()` on anything that has a `quack()` method, regardless of its class hierarchy.
