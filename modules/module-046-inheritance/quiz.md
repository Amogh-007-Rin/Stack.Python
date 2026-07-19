# Module 046: Quiz

## Question 1 (Multiple Choice)
What is inheritance?
- A) Copying all methods from one class to another
- B) A child class acquiring attributes and methods from a parent class
- C) Deleting a class
- D) Creating multiple instances of the same class

## Question 2 (Multiple Choice)
How do you define a class `Dog` that inherits from `Animal`?
- A) `class Dog extends Animal:`
- B) `class Dog(Animal):`
- C) `class Dog inherits Animal:`
- D) `class Dog : Animal`

## Question 3 (True/False)
A child class automatically has all the methods of its parent class.
- True
- False

## Question 4 (Multiple Choice)
What does `super()` do?
- A) Returns the parent class object
- B) Creates a new instance of the parent
- C) Deletes the current instance
- D) Returns the method resolution order

## Question 5 (Multiple Choice)
What is method overriding?
- A) Defining a method with the same name in both parent and child
- B) Deleting a method from the parent
- C) Copying a method to another class
- D) Calling a method multiple times

## Question 6 (True/False)
`isinstance(obj, Class)` checks if `obj` is an instance of `Class` or any of its subclasses.
- True
- False

## Question 7 (Multiple Choice)
What does MRO stand for?
- A) Method Resolution Order
- B) Main Runtime Object
- C) Multiple Return Operation
- D) Method Reference Object

## Question 8 (Multiple Choice)
What determines the order Python uses to look up methods in inheritance?
- A) Alphabetical order
- B) MRO (C3 linearization)
- C) Order of definition in the file
- D) Random order

## Question 9 (Multiple Choice)
If `class D(B, C)` and both `B` and `C` define the same method, which one is used?
- A) `C`'s version (rightmost)
- B) `B`'s version (leftmost)
- C) An error is raised
- D) A random one

## Question 10 (Short Answer)
Why would you use `super().__init__()` in a child class?

---

## Answers

1. **B** — A child class acquiring attributes and methods from a parent class
2. **B** — `class Dog(Animal):`
3. **True**
4. **A** — Returns a proxy object that delegates calls to the parent class
5. **A** — Defining a method with the same name in both parent and child
6. **True**
7. **A** — Method Resolution Order
8. **B** — MRO (C3 linearization)
9. **B** — `B`'s version (leftmost, higher priority in MRO)
10. To call the parent class's `__init__` so that parent attributes are properly initialized, avoiding code duplication.
