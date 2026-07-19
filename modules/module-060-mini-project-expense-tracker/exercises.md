# Module 060: Milestone Project — Personal Expense Tracker — Exercises

Complete the project in `project/starter_code.py`. The solution is at `project/solution/expense_tracker.py`.

## Requirements

### Expense Class
- Fields: `date` (str, YYYY-MM-DD), `category` (str), `amount` (float), `description` (str)
- Property `month` returning `YYYY-MM` from the date

### ExpenseTracker Class
- `__init__(filepath="data/expenses.csv")` — creates the CSV with headers if not exists
- `add_expense(expense)` — appends one expense row
- `get_all() -> list[Expense]` — returns all expenses
- `get_by_category(category) -> list[Expense]` — filters by category
- `get_monthly_summary(year_month) -> dict[str, float]` — returns category -> total for a given month
- `export_summary(filepath)` — writes a human-readable summary text file

### CLI (in `if __name__ == "__main__"`)
- Menu-driven loop with options: Add, View All, View by Category, Monthly Summary, Export, Exit
- Handle all input errors gracefully (bad floats, empty input, file I/O errors)

## Steps

1. Implement the `Expense` class (use `@dataclass`)
2. Implement the `ExpenseTracker` class with all methods
3. Write the CLI menu
4. Test with sample data
5. Run `export_summary()` and verify the output
