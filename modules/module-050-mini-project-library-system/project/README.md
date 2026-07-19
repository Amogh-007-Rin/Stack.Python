# Module 050 Milestone Project: Library/Inventory Management System

## Overview

Build a Library Management System using Object-Oriented Programming. This project brings together everything from Phase 5 (Modules 041-049).

## Core Requirements

### Book Class
- `title`, `author`, `isbn`, `_copies`, `_available` attributes
- `borrow()` — decrements available copies, returns bool
- `return_copy()` — increments available copies, returns bool
- `@property` for `available` and `copies`
- `__str__`, `__repr__`, `__eq__` (by ISBN), `__hash__`

### Member Class Hierarchy
- **`Member`** (base):
  - `name`, `member_id`, `borrowed_books`
  - `can_borrow()`, `borrow_book()`, `return_book()`
  - `borrowing_limit` property returning 0
- **`StudentMember(Member)`**: borrowing_limit = 3, loan_period = 14 days
- **`TeacherMember(Member)`**: borrowing_limit = 10, loan_period = 30 days

### Library Class
- `name`, `_books` (dict keyed by ISBN), `_members` (dict keyed by member_id)
- `add_book(book)`, `add_member(member)`
- `borrow_book(member_id, isbn)`, `return_book(member_id, isbn)`
- `list_books()`, `list_members()`
- `__str__`, `__len__`

### Error Handling
- Borrowing when no copies available → RuntimeError
- Borrowing when at limit → RuntimeError
- Returning a book not borrowed → ValueError
- Invalid member or book ID → ValueError

## Getting Started

1. Open `starter_code.py`
2. Implement each class following the docstrings and type hints
3. Test each class as you go
4. Run your final solution to verify

## Testing

Run your solution:
```bash
python3 project/starter_code.py
```

A full solution is available at `project/solution/library_system.py`.

## Extension Ideas

- Add `search_books(title)` or `search_by_author(author)` methods
- Add `get_borrowing_history(member_id)` with timestamps
- Add overdue tracking with fine calculation
- Implement a `Reservable` mixin for reserving books
- Add data persistence with JSON or a database
