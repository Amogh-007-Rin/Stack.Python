# Contact Book — Project Instructions

## Goal
Build a CLI contact book that lets users manage contacts in memory.

## Files
- `starter_code.py` — incomplete template to fill in
- `solution/contact_book.py` — complete reference solution

## Running
```bash
python starter_code.py
```

## Requirements
1. Menu-driven: Add, View All, Search, Update, Delete, Exit
2. Store contacts as `{"name": str, "phone": str, "email": str}` in a dict keyed by name
3. Handle edge cases: duplicate names, missing contacts, empty list

## Tips
- Start with `add_contact()` and `view_all()` — they're the simplest
- Use `contacts.get(name)` for safe lookup
- Test each feature as you go
- Only peek at the solution after attempting each function
