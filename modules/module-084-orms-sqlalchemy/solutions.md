# Solutions: ORMs: Introduction to SQLAlchemy

## Exercise 1: Define Models
```python
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')
```

## Exercise 2: Create Engine and Tables
```python
engine = create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)
print('Tables created')
```

## Exercise 3: Insert Users
```python
Session = sessionmaker(bind=engine)
session = Session()

users: list[User] = [
    User(username='alice', email='alice@example.com'),
    User(username='bob', email='bob@example.com'),
    User(username='carol', email='carol@example.com'),
]
session.add_all(users)
session.commit()

all_users: list[User] = session.query(User).all()
for user in all_users:
    print(f"User: {user.username}, Email: {user.email}")
```

## Exercise 4: Insert Posts
```python
alice: User = session.query(User).filter_by(username='alice').first()
bob: User = session.query(User).filter_by(username='bob').first()
carol: User = session.query(User).filter_by(username='carol').first()

posts: list[Post] = [
    Post(title='Alice Post 1', body='First post by Alice', user=alice),
    Post(title='Alice Post 2', body='Second post by Alice', user=alice),
    Post(title='Bob Post 1', body='First post by Bob', user=bob),
    Post(title='Bob Post 2', body='Second post by Bob', user=bob),
    Post(title='Carol Post 1', body='First post by Carol', user=carol),
    Post(title='Carol Post 2', body='Second post by Carol', user=carol),
]
session.add_all(posts)
session.commit()

total_posts: int = session.query(Post).count()
print(f"Total posts: {total_posts}")
```

## Exercise 5: Query with filter
```python
user_posts: list[Post] = session.query(Post).join(User).filter(
    User.username == 'alice'
).all()
for post in user_posts:
    print(f"Title: {post.title}")
    print(f"Body: {post.body}\n")
```

## Exercise 6: Update
```python
user: User = session.query(User).filter_by(username='alice').first()
user.email = 'alice_new@example.com'
session.commit()

updated: User = session.query(User).filter_by(username='alice').first()
print(f"Updated email: {updated.email}")
```

## Exercise 7: Delete
```python
post: Post = session.query(Post).filter_by(id=1).first()
if post:
    session.delete(post)
    session.commit()
    print(f"Post {post.id} deleted")

remaining: int = session.query(Post).count()
print(f"Remaining posts: {remaining}")
```

## Exercise 8: Query with order_by
```python
ordered_posts: list[Post] = session.query(Post).order_by(
    Post.title.asc(), Post.id.desc()
).all()
for post in ordered_posts:
    print(f"ID: {post.id}, Title: {post.title}")
```

## Challenge: Library Management Models
```python
from datetime import datetime, timedelta, date
from typing import List, Optional

from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean, Date, DateTime, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(Integer)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer)
    available = Column(Boolean, default=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
    loans = relationship('Loan', back_populates='book')

class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    loans = relationship('Loan', back_populates='borrower')

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    borrower_id = Column(Integer, ForeignKey('borrowers.id'))
    borrow_date = Column(Date, default=date.today)
    return_date = Column(Date, nullable=True)
    book = relationship('Book', back_populates='loans')
    borrower = relationship('Borrower', back_populates='loans')

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def borrow_book(book_id: int, borrower_id: int) -> bool:
    book: Optional[Book] = session.query(Book).filter_by(id=book_id).first()
    if not book or not book.available:
        return False
    book.available = False
    loan: Loan = Loan(book_id=book_id, borrower_id=borrower_id)
    session.add(loan)
    session.commit()
    return True

def return_book(book_id: int) -> bool:
    loan: Optional[Loan] = session.query(Loan).filter(
        Loan.book_id == book_id, Loan.return_date.is_(None)
    ).first()
    if not loan:
        return False
    loan.return_date = date.today()
    book: Book = session.query(Book).filter_by(id=book_id).first()
    if book:
        book.available = True
    session.commit()
    return True

def list_overdue_loans(days: int = 14) -> List[Loan]:
    cutoff: date = date.today() - timedelta(days=days)
    return session.query(Loan).filter(
        Loan.borrow_date < cutoff, Loan.return_date.is_(None)
    ).all()

# Test it
author: Author = Author(name='J.K. Rowling', birth_year=1965)
book: Book = Book(title='Harry Potter', year=1997, author=author)
borrower: Borrower = Borrower(name='Alice', email='alice@example.com')
session.add_all([author, book, borrower])
session.commit()

borrow_book(book.id, borrower.id)
print(f"Book available: {book.available}")  # False
print(f"Overdue loans: {list_overdue_loans(1)}")  # Should show 1
return_book(book.id)
print(f"Book available after return: {book.available}")  # True
```
