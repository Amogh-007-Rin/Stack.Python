# Module 045: Quiz

## Question 1 (Multiple Choice)
What does encapsulation mean in OOP?
- A) Making all attributes public
- B) Bundling data and methods, restricting direct access to internal state
- C) Writing all code in one file
- D) Using only class variables

## Question 2 (Multiple Choice)
What does a single underscore prefix (`_attr`) indicate?
- A) The attribute is truly private
- B) The attribute is protected (internal use, convention)
- C) The attribute is a class variable
- D) The attribute is a method

## Question 3 (Multiple Choice)
What does a double underscore prefix (`__attr`) do?
- A) Makes the attribute completely private
- B) Triggers name mangling to `_ClassName__attr`
- C) Deletes the attribute
- D) Makes the attribute read-only

## Question 4 (True/False)
Name mangling makes an attribute truly inaccessible from outside the class.
- True
- False

## Question 5 (Multiple Choice)
What is the purpose of a getter method?
- A) To modify an attribute
- B) To provide controlled access to an attribute
- C) To delete an attribute
- D) To create a new class

## Question 6 (Multiple Choice)
What is the purpose of a setter method?
- A) To retrieve an attribute's value
- B) To set an attribute's value with validation
- C) To define a class variable
- D) To create a new instance

## Question 7 (True/False)
Python has strict private/public access control like Java.
- True
- False

## Question 8 (Multiple Choice)
Why is encapsulation important?
- A) It makes code run faster
- B) It prevents invalid state and allows internal changes without breaking users
- C) It reduces the number of files needed
- D) It automatically documents code

## Question 9 (Multiple Choice)
What does this code access?
```python
class X:
    def __init__(self):
        self.__v = 5

x = X()
print(x._X__v)
```
- A) A class variable
- B) The mangled private attribute
- C) A public attribute
- D) It raises an error

## Question 10 (Short Answer)
What is the difference between `_protected` and `__private` in Python?

---

## Answers

1. **B** — Bundling data and methods, restricting direct access to internal state
2. **B** — The attribute is protected (internal use, convention)
3. **B** — Triggers name mangling to `_ClassName__attr`
4. **False** — It's still accessible via the mangled name
5. **B** — To provide controlled access to an attribute
6. **B** — To set an attribute's value with validation
7. **False** — Python uses conventions, not enforced access control
8. **B** — It prevents invalid state and allows internal changes without breaking users
9. **B** — The mangled private attribute
10. `_protected` is a naming convention indicating internal use. `__private` triggers name mangling to `_ClassName__attr`, making it harder (but not impossible) to access accidentally, especially in inheritance.
