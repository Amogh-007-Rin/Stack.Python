# Module 084: ORMs: Introduction to SQLAlchemy

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2.5 hours

## Learning Objectives

- Understand the ORM (object-relational mapping) concept
- Define database models with SQLAlchemy's declarative base
- Perform CRUD operations through the ORM
- Define relationships between models
- Query with filter and order_by

## Topics Covered

1. ORM concept: mapping classes to database tables
2. SQLAlchemy overview
3. Declarative base (declarative_base)
4. Defining models (Column, Integer, String, Float, DateTime, ForeignKey)
5. Creating engine and session
6. CRUD operations with ORM
7. Relationships (relationship, back_populates)
8. Querying with filter and order_by

## Prerequisites

Modules 000-083.

## Key Concepts

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

## Resources

- SQLAlchemy documentation: https://www.sqlalchemy.org
- SQLAlchemy ORM tutorial
- Flask-SQLAlchemy (for web integration)
