# Exercises: Working with Databases: SQLite (sqlite3)

All exercises use the built-in `sqlite3` module.

## Exercise 1: Create and Connect
Create a new SQLite database file called `company.db`. Create a table `employees` with columns: `id` (INTEGER PRIMARY KEY), `name` (TEXT NOT NULL), `department` (TEXT), `salary` (REAL).

## Exercise 2: Insert Data
Insert at least 5 employees with realistic data into the `employees` table. Commit the changes.

## Exercise 3: Query All
Write a query to fetch and print all employees. Display results in a formatted way.

## Exercise 4: Filter with WHERE
Query employees with a salary greater than 50000. Print their names and salaries.

## Exercise 5: Update
Give a 10% raise to all employees in the 'Engineering' department. Commit and verify with a SELECT.

## Exercise 6: Delete
Remove an employee by their ID. Confirm deletion by attempting to fetch that employee.

## Exercise 7: Parameterized Query
Write a function `get_employees_by_department(dept: str) -> list` that uses a parameterized query to prevent SQL injection.

## Exercise 8: Error Handling
Write a safe wrapper function that executes any SQL query and handles `sqlite3.Error` exceptions gracefully, returning `None` on failure.

## Challenge: Contact Manager
Build a CLI contact manager using SQLite:
- Create a `contacts` table (id, name, phone, email)
- Implement add, list, search (by name), delete operations
- All queries must be parameterized
- Handle database errors
