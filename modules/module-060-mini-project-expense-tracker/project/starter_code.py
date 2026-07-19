"""
Personal Expense Tracker — Starter Code.

TODO: Implement the Expense and ExpenseTracker classes, then build a CLI menu.

Usage:
    python project/starter_code.py
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Expense:
    """Represents a single expense entry.

    Attributes:
        date: Date in YYYY-MM-DD format.
        category: Expense category (e.g., Food, Transport).
        amount: Monetary amount.
        description: Free-text description.
    """
    date: str
    category: str
    amount: float
    description: str

    @property
    def month(self) -> str:
        """Return the YYYY-MM portion of the date."""
        # TODO: return self.date[:7]
        raise NotImplementedError


class ExpenseTracker:
    """Manages expenses with CSV file persistence."""

    def __init__(self, filepath: str = "data/expenses.csv") -> None:
        """Initialize tracker and ensure CSV file exists with headers."""
        # TODO: store filepath, create parent dir, write headers if missing
        raise NotImplementedError

    def add_expense(self, expense: Expense) -> None:
        """Append a single expense row to the CSV file."""
        # TODO: open file in append mode, write expense fields as a row
        raise NotImplementedError

    def get_all(self) -> List[Expense]:
        """Return all expenses as a list of Expense objects."""
        # TODO: read CSV, parse each row into Expense, return list
        raise NotImplementedError

    def get_by_category(self, category: str) -> List[Expense]:
        """Filter expenses by category."""
        # TODO: call get_all() and filter
        raise NotImplementedError

    def get_monthly_summary(self, year_month: str) -> dict[str, float]:
        """Return {category: total} for a given YYYY-MM month."""
        # TODO: filter expenses by month, sum amounts per category
        raise NotImplementedError

    def export_summary(self, filepath: str) -> None:
        """Write a human-readable summary report to a text file."""
        # TODO: write grouped summary to filepath
        raise NotImplementedError


def main() -> None:
    """Run the expense tracker CLI."""
    tracker = ExpenseTracker()
    # TODO: implement menu loop with options:
    # 1. Add expense
    # 2. View all expenses
    # 3. View by category
    # 4. Monthly summary
    # 5. Export summary
    # 6. Exit
    print("Expense Tracker CLI")
    print("Coming soon...")


if __name__ == "__main__":
    main()
