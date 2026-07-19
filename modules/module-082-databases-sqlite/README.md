# Module 082: Working with Databases: SQLite (sqlite3)

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2 hours

## Learning Objectives

- Connect to an SQLite database using the sqlite3 module
- Create tables and perform CRUD operations (INSERT, SELECT, UPDATE, DELETE)
- Use parameterized queries to prevent SQL injection
- Commit transactions and close connections properly

## Topics Covered

1. SQLite overview
2. sqlite3 module
3. Connecting to a database with .connect
4. Creating tables with CREATE TABLE
5. Inserting data with INSERT
6. Querying with SELECT
7. Updating with UPDATE
8. Deleting with DELETE
9. Parameterized queries with ?
10. Committing and closing connections

## Prerequisites

Modules 000-081.

## Key Concepts

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)''')

cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
conn.commit()

cursor.execute('SELECT * FROM users WHERE age > ?', (25,))
rows = cursor.fetchall()
print(rows)

conn.close()
```

## Resources

- Python sqlite3 documentation
- SQLite official site: https://sqlite.org
- DB Browser for SQLite (GUI tool)
