# Module 083: Introduction to SQL from Python

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2 hours

## Learning Objectives

- Write SQL queries with WHERE, ORDER BY, GROUP BY, HAVING, and JOIN
- Use aggregate functions: COUNT, SUM, AVG, MAX, MIN
- Execute SQL from Python with sqlite3
- Fetch results with fetchone, fetchall, fetchmany
- Use row factories for dict-like access

## Topics Covered

1. SELECT with WHERE clause
2. ORDER BY for sorting
3. GROUP BY and HAVING for aggregation
4. INNER JOIN and LEFT JOIN
5. Aggregate functions (COUNT, SUM, AVG, MAX, MIN)
6. Executing SQL from Python with sqlite3
7. Fetching results: fetchone, fetchall, fetchmany
8. Row factories for dict-like access

## Prerequisites

Modules 000-082.

## Key Concepts

```python
import sqlite3

conn = sqlite3.connect('store.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
    SELECT category, COUNT(*) as count, AVG(price) as avg_price
    FROM products
    WHERE price > ?
    GROUP BY category
    HAVING count > 1
    ORDER BY avg_price DESC
''', (10.0,))

for row in cursor.fetchall():
    print(row['category'], row['count'], row['avg_price'])

conn.close()
```

## Resources

- SQLite documentation: https://sqlite.org/lang.html
- SQL Tutorial (W3Schools)
- Mode Analytics SQL Tutorial
