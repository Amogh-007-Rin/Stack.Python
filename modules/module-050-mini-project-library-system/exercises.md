# Module 050: Exercises

These exercises build toward the complete library system. Complete them in order.

## Exercise 1: Book Class
Create a `Book` class with `title`, `author`, `isbn`, `_copies`, and `_available`. Add `borrow()` and `return_copy()` methods.

## Exercise 2: Book Dunder Methods
Add `__str__`, `__repr__`, `__eq__`, and `__hash__` to the Book class.

## Exercise 3: Base Member Class
Create a `Member` class with `name`, `member_id`, `borrowed_books`. Add `can_borrow()`, `borrow_book()`, and `return_book()`.

## Exercise 4: Member Inheritance
Create `StudentMember(Member)` with limit 3 and `TeacherMember(Member)` with limit 10.

## Exercise 5: Library Class - Adding
Create a `Library` class with `add_book()` and `add_member()` methods. Store books in a dict keyed by ISBN, members keyed by member_id.

## Exercise 6: Library Class - Borrowing
Add `borrow_book(member_id, isbn)` to the Library. Check availability, update book copies, and add to member's list.

## Exercise 7: Library Class - Returning
Add `return_book(member_id, isbn)` to the Library. Return the copy and remove from member's list.

## Exercise 8: Library Listing Methods
Add `list_books()` and `list_members()` that print formatted information about each.

## Exercise 9: Library Dunder Methods
Add `__str__` and `__len__` to the Library class.

## Exercise 10: Full Integration
Write a demo script that:
1. Creates a library
2. Adds 3+ books with multiple copies
3. Registers 2 students and 1 teacher
4. Performs several borrow/return operations
5. Lists books and members after each operation
6. Demonstrates error handling (no copies, borrowing limit reached)
