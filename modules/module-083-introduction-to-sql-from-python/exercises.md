# Exercises: Introduction to SQL from Python

All exercises use `sqlite3` with a sample database.

## Exercise 1: Setup
Create a database `store.db` with tables:
- `customers` (id, name, email, joined_date)
- `orders` (id, customer_id FK, product, amount, order_date)
Insert at least 5 customers and 10 orders.

## Exercise 2: WHERE and ORDER BY
Query all orders with amount greater than 100, sorted by amount descending.

## Exercise 3: GROUP BY and Aggregation
Write a query that groups orders by product and shows total sales per product. Use `SUM` and `COUNT`.

## Exercise 4: GROUP BY with HAVING
Find products with total sales amount greater than 200 (HAVING).

## Exercise 5: INNER JOIN
Join customers with their orders to show customer name, product, and amount.

## Exercise 6: LEFT JOIN
Show all customers and their orders, including customers who have never placed an order (LEFT JOIN).

## Exercise 7: Aggregate Functions
Write queries to find: total number of customers, average order amount, maximum order amount, minimum order amount, and total revenue.

## Exercise 8: fetchone and fetchmany
Fetch orders one at a time using `fetchone()`, then fetch in batches of 3 using `fetchmany(3)`.

## Exercise 9: Row Factory
Enable `sqlite3.Row` as the row factory and redo the JOIN query from Exercise 5, accessing columns by name.

## Challenge: Sales Dashboard Queries
Write a Python function for each analytical query:
- `top_customers(n: int) -> list`: Top n customers by total spend
- `monthly_revenue(year: int) -> list`: Revenue by month for a given year
- `product_rankings() -> list`: Products ranked by sales volume
All functions must use parameterized queries and return typed results.
