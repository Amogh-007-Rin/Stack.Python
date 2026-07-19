# Exercises: ORMs: Introduction to SQLAlchemy

Assume `from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey` and `from sqlalchemy.orm import declarative_base, relationship, sessionmaker`.

## Exercise 1: Define Models
Create `User` and `Post` models. User has id, username, email. Post has id, title, body, user_id FK. Set up the relationship so `user.posts` works.

## Exercise 2: Create Engine and Tables
Create an SQLite engine, generate all tables, and verify they exist (check the database file).

## Exercise 3: Insert Users
Create a session and insert 3 users. Commit and confirm by querying all users.

## Exercise 4: Insert Posts
Insert 2 posts for each user. Commit and verify with a query.

## Exercise 5: Query with filter
Query all posts by a specific user (by username). Print the title and body of each.

## Exercise 6: Update
Update the email of a user. Commit and verify.

## Exercise 7: Delete
Delete a post by its ID. Commit and verify.

## Exercise 8: Query with order_by
Query all posts ordered by title alphabetically, then by id descending.

## Challenge: Library Management Models
Create a complete model set for a library:
- `Author` (id, name, birth_year)
- `Book` (id, title, year, author_id FK, available: bool)
- `Borrower` (id, name, email)
- `Loan` (id, book_id FK, borrower_id FK, borrow_date, return_date)
Add relationships between all models. Write functions to borrow a book, return a book, and list overdue loans.
