# Module 049: Quiz

## Question 1 (Multiple Choice)
What module provides ABC support in Python?
- A) `abstract`
- B) `abc`
- C) `interface`
- D) `polymorph`

## Question 2 (Multiple Choice)
What decorator is used to mark a method as abstract?
- A) `@abstract`
- B) `@abstractmethod`
- C) `@interface`
- D) `@must_implement`

## Question 3 (True/False)
You can instantiate an ABC directly.
- True
- False

## Question 4 (Multiple Choice)
What happens if a subclass doesn't implement all abstract methods?
- A) It raises a warning
- B) It cannot be instantiated (TypeError)
- C) It uses a default implementation
- D) The missing methods are ignored

## Question 5 (Multiple Choice)
What is the purpose of an ABC?
- A) To improve performance
- B) To define an interface contract that subclasses must follow
- C) To automatically generate documentation
- D) To reduce memory usage

## Question 6 (True/False)
An ABC can have concrete (non-abstract) methods.
- True
- False

## Question 7 (Multiple Choice)
What does `register()` do on an ABC?
- A) Creates a new instance
- B) Marks an existing class as a virtual subclass
- C) Deletes the class
- D) Prints the class name

## Question 8 (Multiple Choice)
Where can you find ready-made ABCs in the standard library?
- A) `collections.abc`
- B) `itertools`
- C) `functools`
- D) `typing`

## Question 9 (Multiple Choice)
Can you define an abstract property in an ABC?
- A) No, only methods can be abstract
- B) Yes, using `@property` and `@abstractmethod` together
- C) Only in Python 3.10+
- D) Only for class methods

## Question 10 (Short Answer)
Why would you use an ABC instead of relying on duck typing?

---

## Answers

1. **B** — `abc`
2. **B** — `@abstractmethod`
3. **False** — Raises `TypeError`
4. **B** — It cannot be instantiated (TypeError)
5. **B** — To define an interface contract that subclasses must follow
6. **True** — ABCs can have concrete methods that subclasses inherit
7. **B** — Marks an existing class as a virtual subclass
8. **A** — `collections.abc`
9. **B** — Yes, using `@property` and `@abstractmethod` together
10. ABCs provide compile-time/instantiation-time enforcement of interfaces. They document the contract explicitly, catch missing methods early (before runtime method calls), and support `isinstance()` checks for interface conformance. Duck typing is more flexible but provides no guarantees.
