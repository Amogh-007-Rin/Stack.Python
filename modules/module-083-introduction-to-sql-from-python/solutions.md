# Solutions: Introduction to SQL from Python

## Exercise 1: Setup
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        joined_date TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT NOT NULL,
        amount REAL,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
''')

customers: list[tuple] = [
    ('Alice', 'alice@example.com', '2024-01-15'),
    ('Bob', 'bob@example.com', '2024-02-20'),
    ('Carol', 'carol@example.com', '2024-03-10'),
    ('David', 'david@example.com', '2024-04-05'),
    ('Eve', 'eve@example.com', '2024-05-01'),
]
cursor.executemany(
    'INSERT INTO customers (name, email, joined_date) VALUES (?, ?, ?)',
    customers,
)

orders: list[tuple] = [
    (1, 'Laptop', 1200, '2024-06-01'),
    (1, 'Mouse', 25, '2024-06-02'),
    (2, 'Keyboard', 80, '2024-06-03'),
    (3, 'Monitor', 300, '2024-06-04'),
    (3, 'USB Hub', 40, '2024-06-05'),
    (4, 'Laptop', 1100, '2024-06-06'),
    (2, 'Mouse', 25, '2024-06-07'),
    (5, 'Webcam', 75, '2024-06-08'),
    (1, 'Keyboard', 85, '2024-06-09'),
    (5, 'Monitor', 320, '2024-06-10'),
]
cursor.executemany(
    'INSERT INTO orders (customer_id, product, amount, order_date) VALUES (?, ?, ?, ?)',
    orders,
)
conn.commit()
conn.close()
```

## Exercise 2: WHERE and ORDER BY
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('SELECT * FROM orders WHERE amount > ? ORDER BY amount DESC', (100,))
rows: list = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
```

## Exercise 3: GROUP BY and Aggregation
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('''
    SELECT product, SUM(amount) as total_sales, COUNT(*) as units_sold
    FROM orders
    GROUP BY product
''')
rows: list = cursor.fetchall()
for row in rows:
    print(f"{row[0]}: ${row[1]:.2f} ({row[2]} units)")
conn.close()
```

## Exercise 4: GROUP BY with HAVING
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('''
    SELECT product, SUM(amount) as total_sales
    FROM orders
    GROUP BY product
    HAVING total_sales > 200
''')
rows: list = cursor.fetchall()
for row in rows:
    print(f"{row[0]}: ${row[1]:.2f}")
conn.close()
```

## Exercise 5: INNER JOIN
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('''
    SELECT c.name, o.product, o.amount
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    ORDER BY c.name
''')
rows: list = cursor.fetchall()
for name, product, amount in rows:
    print(f"{name}: {product} (${amount:.2f})")
conn.close()
```

## Exercise 6: LEFT JOIN
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('''
    SELECT c.name, o.product, o.amount
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    ORDER BY c.name
''')
rows: list = cursor.fetchall()
for name, product, amount in rows:
    if product:
        print(f"{name}: {product} (${amount:.2f})")
    else:
        print(f"{name}: No orders")
conn.close()
```

## Exercise 7: Aggregate Functions
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()

queries: list[str] = [
    'SELECT COUNT(*) FROM customers',
    'SELECT AVG(amount) FROM orders',
    'SELECT MAX(amount) FROM orders',
    'SELECT MIN(amount) FROM orders',
    'SELECT SUM(amount) FROM orders',
]
labels: list[str] = [
    'Total customers', 'Avg order amount', 'Max order amount',
    'Min order amount', 'Total revenue',
]
for label, query in zip(labels, queries):
    cursor.execute(query)
    print(f"{label}: {cursor.fetchone()[0]}")
conn.close()
```

## Exercise 8: fetchone and fetchmany
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('SELECT * FROM orders')

print("One at a time:")
row = cursor.fetchone()
while row:
    print(f"  {row}")
    row = cursor.fetchone()

print("\nIn batches of 3:")
cursor.execute('SELECT * FROM orders')
batch = cursor.fetchmany(3)
while batch:
    print(f"  Batch: {batch}")
    batch = cursor.fetchmany(3)
conn.close()
```

## Exercise 9: Row Factory
```python
import sqlite3

conn: sqlite3.Connection = sqlite3.connect('store.db')
conn.row_factory = sqlite3.Row
cursor: sqlite3.Cursor = conn.cursor()
cursor.execute('''
    SELECT c.name, o.product, o.amount
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    ORDER BY c.name
''')
for row in cursor.fetchall():
    print(f"{row['name']}: {row['product']} (${row['amount']:.2f})")
conn.close()
```

## Challenge: Sales Dashboard Queries
```python
import sqlite3
from typing import List, Tuple, Dict

conn: sqlite3.Connection = sqlite3.connect('store.db')
conn.row_factory = sqlite3.Row

def top_customers(n: int) -> List[Dict]:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute('''
        SELECT c.name, SUM(o.amount) as total_spent
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        GROUP BY c.id
        ORDER BY total_spent DESC
        LIMIT ?
    ''', (n,))
    return [dict(row) for row in cursor.fetchall()]

def monthly_revenue(year: int) -> List[Dict]:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute('''
        SELECT strftime('%m', order_date) as month,
               SUM(amount) as revenue
        FROM orders
        WHERE strftime('%Y', order_date) = ?
        GROUP BY month
        ORDER BY month
    ''', (str(year),))
    return [dict(row) for row in cursor.fetchall()]

def product_rankings() -> List[Dict]:
    cursor: sqlite3.Cursor = conn.cursor()
    cursor.execute('''
        SELECT product, COUNT(*) as units_sold, SUM(amount) as total_revenue
        FROM orders
        GROUP BY product
        ORDER BY units_sold DESC
    ''')
    return [dict(row) for row in cursor.fetchall()]

print('Top customers:', top_customers(3))
print('Monthly revenue 2024:', monthly_revenue(2024))
print('Product rankings:', product_rankings())
conn.close()
```
