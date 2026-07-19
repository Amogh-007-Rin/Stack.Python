# Module 050: Milestone Project — Library/Inventory Management System

> **Phase:** 5. OOP  |  **Estimated time:** 3 hours  |  **Milestone Project:** Yes

## Prerequisites
- All modules 041-049 (Phase 5: OOP)

## Learning Objectives
By the end of this module, you will be able to:
- Design and implement a multi-class OOP system
- Use inheritance to model specialized behavior
- Demonstrate encapsulation with private/protected attributes
- Use dunder methods (`__str__`, `__repr__`, `__len__`) for integration
- Apply polymorphism and duck typing
- Optionally use ABCs for interface contracts

## Why This Matters
This milestone project ties together everything from Phase 5: classes, attributes, methods, constructors, class/instance variables, encapsulation, inheritance, polymorphism, dunder methods, and abstract base classes. You'll build a complete library management system demonstrating professional OOP design.

## Project Overview

Build a Library Management System with three core classes: `Book`, `Member`, and `Library`. The system should handle adding/borrowing/returning books, tracking members, and enforcing borrowing limits.

### Core Classes

```python
class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies
        self._available = copies

    # Properties, dunder methods, and methods
```

```python
class Member:
    """Represents a library member."""

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book from the library."""

    def return_book(self, book):
        """Return a borrowed book."""
```

```python
class Library:
    """Manages the collection of books and members."""

    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        """Add a book to the library."""

    def add_member(self, member):
        """Register a member."""

    def borrow_book(self, member_id, isbn):
        """Allow a member to borrow a book."""

    def return_book(self, member_id, isbn):
        """Process a book return."""

    def list_books(self):
        """List all books in the library."""

    def list_members(self):
        """List all registered members."""
```

### Inheritance: Member Types

- `StudentMember`: Can borrow up to 3 books, 14-day loan period
- `TeacherMember`: Can borrow up to 10 books, 30-day loan period

### Required Features

1. Add books with title, author, ISBN, and copy count
2. Register members (Student or Teacher)
3. Borrow a book (decrease available copies, add to member's list)
4. Return a book (increase available copies, remove from member's list)
5. List all books with availability
6. List all members with their borrowed books
7. Enforce borrowing limits per member type
8. Prevent borrowing unavailable books
9. Use `@property` for controlled attribute access
10. Implement `__str__` and `__repr__` on all classes

### Extension Ideas

- Add a `search_books(title)` or `search_by_author(author)` method
- Add a `get_borrowing_history(member_id)` method
- Add overdue tracking with fines
- Add a `@dataclass` version of `Book`
- Add `Reservable` mixin for reserving books

## Key Takeaways

- OOP organizes complex systems into interacting classes.  
- Inheritance models specialized behavior (Student vs Teacher members).  
- Encapsulation protects internal state (available copies, borrowed lists).  
- Dunder methods make objects work with Python built-ins.  
- A well-designed class hierarchy is reusable and extensible.

## Next Module

Continue to **Module 051** (Phase 6: Advanced OOP).

## Project Instructions

See `project/README.md` for detailed instructions. The `project/starter_code.py` file contains a skeleton to complete. A full solution is in `project/solution/library_system.py`.
