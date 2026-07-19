# Solutions: Working with Databases: SQLite (sqlite3)

## Exercise 1: Create and Connect
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('company.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
''')
conn.commit()
conn.close()
```

## Exercise 2: Insert Data
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('company.db')
cursor: sqlite3.Cursor = conn.cursor()

employees: list[tuple[str, str, float]] = [
    ('Alice Johnson', 'Engineering', 75000),
    ('Bob Smith', 'Marketing', 55000),
    ('Carol Davis', 'Engineering', 82000),
    ('David Brown', 'Sales', 48000),
    ('Eve Wilson', 'Engineering', 91000),
]
cursor.executemany(
    'INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)',
    employees,
)
conn.commit()
conn.close()
```

## Exercise 3: Query All
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('company.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('SELECT * FROM employees')
rows: list[sqlite3.Row] = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Salary: ${row[3]:.2f}")
conn.close()
```

## Exercise 4: Filter with WHERE
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('company.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('SELECT name, salary FROM employees WHERE salary > ?', (50000,))
rows: list[sqlite3.Row] = cursor.fetchall()
for name, salary in rows:
    print(f"{name}: ${salary:.2f}")
conn.close()
```

## Exercise 5: Update
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('company.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute(
    'UPDATE employees SET salary = salary * 1.1 WHERE department = ?',
    ('Engineering',),
)
conn.commit()
print(f"Rows updated: {cursor.rowcount}")
cursor.execute('SELECT name, salary FROM employees WHERE department = ?', ('Engineering',))
for name, salary in cursor.fetchall():
    print(f"{name}: ${salary:.2f}")
conn.close()
```

## Exercise 6: Delete
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('company.db')
cursor: sqlite3.Cursor = conn.cursor()
emp_id: int = 4
cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
conn.commit()
if cursor.rowcount > 0:
    print(f"Employee {emp_id} deleted")
else:
    print(f"Employee {emp_id} not found")
cursor.execute('SELECT * FROM employees WHERE id = ?', (emp_id,))
assert cursor.fetchone() is None
conn.close()
```

## Exercise 7: Parameterized Query
```python
import sqlite3
from typing import List, Tuple

def get_employees_by_department(dept: str) -> List[Tuple]:
    conn: sqlite3.Connection = sqlite3.connect('company.db')
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE department = ?', (dept,))
    results: List[Tuple] = cursor.fetchall()
    conn.close()
    return results

eng_emps: List[Tuple] = get_employees_by_department('Engineering')
print(f"Engineering employees: {eng_emps}")
```

## Exercise 8: Error Handling
```python
import sqlite3
from typing import Any, Optional

def safe_execute(db_path: str, query: str, params: tuple = ()) -> Optional[list]:
    try:
        conn: sqlite3.Connection = sqlite3.connect(db_path)
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        results: list = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

result: Optional[list] = safe_execute('company.db', 'SELECT * FROM employees')
print(result)
```

## Challenge: Contact Manager
```python
import sqlite3
from typing import List, Optional, Tuple

class ContactManager:
    def __init__(self, db_path: str = 'contacts.db') -> None:
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.cursor: sqlite3.Cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def add(self, name: str, phone: str, email: str) -> None:
        self.cursor.execute(
            'INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)',
            (name, phone, email),
        )
        self.conn.commit()
        print(f"Added contact: {name}")

    def list_all(self) -> List[Tuple]:
        self.cursor.execute('SELECT * FROM contacts ORDER BY name')
        return self.cursor.fetchall()

    def search(self, name: str) -> List[Tuple]:
        self.cursor.execute(
            'SELECT * FROM contacts WHERE name LIKE ?',
            (f'%{name}%',),
        )
        return self.cursor.fetchall()

    def delete(self, contact_id: int) -> bool:
        self.cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self) -> None:
        self.conn.close()

mgr: ContactManager = ContactManager()
mgr.add('Alice', '555-0101', 'alice@example.com')
mgr.add('Bob', '555-0102', 'bob@example.com')
print('All contacts:', mgr.list_all())
print('Search:', mgr.search('Alice'))
mgr.delete(1)
print('After delete:', mgr.list_all())
mgr.close()
```
