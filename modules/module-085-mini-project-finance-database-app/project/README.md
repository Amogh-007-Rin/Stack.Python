# Personal Finance Database App

A SQLite-backed personal finance manager built with SQLAlchemy. Track income and expenses, view spending reports by category, and generate monthly summaries.

## Features

- Add transactions (date, amount, category, description)
- View all transactions sorted by date
- Delete transactions by ID
- Spending by category report
- Monthly income/expense/net summary
- Interactive CLI menu

## Setup

```bash
pip install sqlalchemy
```

## Usage

```bash
python finance_app.py
```

Interactive menu:
```
1. Add Transaction
2. View All Transactions
3. Delete Transaction
4. Spending by Category
5. Monthly Summary
6. Exit
```

## Starter Code

Open `starter_code.py` and follow the TODO comments to implement each function. The solution is in `solution/finance_app.py`.

## Requirements

- Python 3.9+
- SQLAlchemy
