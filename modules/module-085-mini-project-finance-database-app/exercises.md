# Exercises: Milestone Project: Personal Finance Database App

These exercises guide you through building the finance application. Complete all to finish the milestone.

## Exercise 1: Transaction Model
Define a `Transaction` model using SQLAlchemy with fields: id, date (DateTime), amount (Float), category (String), description (String).

## Exercise 2: Database Setup
Create the engine and session. Add a `Base.metadata.create_all` call. Write a function `init_db()` that returns a configured session.

## Exercise 3: Add Transaction
Write a function `add_transaction(session, date, amount, category, description) -> Transaction` that creates and commits a new transaction.

## Exercise 4: View All Transactions
Write a function `get_all_transactions(session) -> list[Transaction]` that returns all transactions ordered by date descending.

## Exercise 5: Delete Transaction
Write a function `delete_transaction(session, transaction_id: int) -> bool` that deletes by ID and returns True if successful.

## Exercise 6: Spending by Category
Write a function `spending_by_category(session) -> list[tuple]` that groups transactions by category and sums the amounts (positive amounts only).

## Exercise 7: Monthly Summary
Write a function `monthly_summary(session) -> list[dict]` that returns total income, total expenses, and net for each month.

## Exercise 8: CLI Menu
Build an interactive CLI menu that loops until the user chooses to exit. Options: Add, View, Delete, Category Report, Monthly Summary, Exit.

## Challenge: Budget Alerts
Add a `Budget` model (category, monthly_limit). When adding a transaction, check if the category's monthly spending exceeds the budget. Print a warning if so.
