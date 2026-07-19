# Personal Expense Tracker

A CSV-backed expense tracking application built with object-oriented Python.

## Requirements

- Python 3.10+
- No external dependencies (uses only `csv`, `datetime`, `pathlib`)

## Features

- Add an expense (date, category, amount, description)
- View all expenses in a formatted table
- Filter expenses by category
- View monthly summary with totals per category
- Export summary to a text file

## Usage

```bash
python project/solution/expense_tracker.py
```

The program presents a menu-driven CLI. Expenses are saved to `data/expenses.csv` automatically.

## Learning Objectives

- Build a multi-class OOP application
- Persist data with the `csv` module
- Handle file I/O and user-input errors
- Practice properties, dataclasses/enums, and composition

## Starter Code

Open `starter_code.py` — it contains class stubs and TODO comments to guide implementation.
