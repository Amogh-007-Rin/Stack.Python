# Milestone Project: Contact Book

## Objective
Build a command-line contact book application that stores contacts in memory using dictionaries. The app should present a menu and allow the user to perform CRUD operations.

## Requirements

### Core Features
1. **Add a contact** — Prompt for name, phone, and email. Store as a dict keyed by name.
2. **View all contacts** — Display all contacts in a formatted list.
3. **Search by name** — Look up a contact and display their details.
4. **Update a contact** — Change the phone and/or email for an existing contact.
5. **Delete a contact** — Remove a contact by name.

### Menu System
```
=== Contact Book ===
1. Add contact
2. View all contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit
====================
Choose an option (1-6):
```

### Data Structure
```python
# Each contact is a dict:
# {"name": str, "phone": str, "email": str}
#
# All contacts stored in a dict keyed by name:
# {"Alice": {"name": "Alice", "phone": "555-1234", "email": "alice@x.com"}}
```

### Edge Cases to Handle
- Adding a name that already exists (ask to overwrite or cancel)
- Searching for a name that doesn't exist (show "not found" message)
- Deleting a non-existent name (show error)
- Empty contact list when viewing (show "no contacts" message)
- Empty input for phone/email (allow blank values)

### Stretch Goals (Optional)
- Save contacts to a file and load them on startup
- Allow searching by partial name match
- Add a phone number format validator
- Sort contacts alphabetically when displaying

## Getting Started
Open `project/starter_code.py` and fill in the function bodies. Run your solution with:
```bash
python project/starter_code.py
```

Check `project/solution/contact_book.py` only after you've attempted the project yourself.
