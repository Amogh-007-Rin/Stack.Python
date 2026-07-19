# Module 050: Quiz

## Question 1 (Multiple Choice)
Which OOP concept is demonstrated by having both `StudentMember` and `TeacherMember` inherit from `Member`?
- A) Encapsulation
- B) Inheritance
- C) Duck typing
- D) Polymorphism

## Question 2 (Multiple Choice)
What does the `@property` decorator do in the Book class?
- A) Makes the method private
- B) Allows a method to be accessed like an attribute
- C) Defines a class variable
- D) Creates a new instance

## Question 3 (True/False)
The `__eq__` method on Book compares books by their title.
- True
- False

## Question 4 (Multiple Choice)
What happens when a StudentMember tries to borrow a 4th book?
- A) The borrow succeeds
- B) A RuntimeError is raised
- C) The oldest borrowed book is returned automatically
- D) The book is added but flagged as overdue

## Question 5 (Multiple Choice)
What data structure is used to store books in the Library class?
- A) A list
- B) A set
- C) A dict keyed by ISBN
- D) A tuple

## Question 6 (True/False)
The `borrow()` method on `Book` raises an exception if no copies are available.
- True
- False

## Question 7 (Multiple Choice)
In the library system, which class is responsible for checking borrowing limits?
- A) `Book`
- B) `Library`
- C) `Member` (and its subclasses)
- D) A separate `BorrowingPolicy` class

## Question 8 (Multiple Choice)
What does `__len__` return on a Library instance?
- A) The number of members
- B) The number of books currently borrowed
- C) The number of books in the collection
- D) The number of available copies

## Question 9 (Multiple Choice)
Which of these is NOT demonstrated in the library system?
- A) Encapsulation
- B) Inheritance
- C) Multiple inheritance
- D) Dunder methods

## Question 10 (Short Answer)
Describe the flow of a `borrow_book()` call in the Library system. What happens step by step?

---

## Answers

1. **B** — Inheritance
2. **B** — Allows a method to be accessed like an attribute
3. **False** — It compares by ISBN
4. **B** — A RuntimeError is raised (borrowing limit exceeded)
5. **C** — A dict keyed by ISBN
6. **False** — It returns False if no copies are available; the Library class raises the error
7. **C** — `Member` (and its subclasses) via `can_borrow()`
8. **C** — The number of books in the collection
9. **C** — Multiple inheritance (only single inheritance is used)
10. The Library's `borrow_book(member_id, isbn)` looks up the member and book, calls `book.borrow()` to decrement available copies (returning False if none), then calls `member.borrow_book(book)` which checks the borrowing limit and appends the book to the member's list. If either step fails, the appropriate error is raised.
