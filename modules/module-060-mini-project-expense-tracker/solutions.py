"""
Personal Expense Tracker — solutions.py

This file provides alternative solutions to the project exercises as standalone
Python functions, useful for quick testing or reference.

Usage:
    python modules/module-060-mini-project-expense-tracker/solutions.py
"""

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional
from collections import defaultdict


@dataclass
class Expense:
    """Represents a single expense entry.

    Attributes:
        date: Date in YYYY-MM-DD format.
        category: Expense category.
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
        return self.date[:7]


class ExpenseTracker:
    """Manages expenses with CSV file persistence.

    Attributes:
        filepath: Path to the CSV file storing expense data.
    """

    def __init__(self, filepath: str = "data/expenses.csv") -> None:
        """Initialize tracker and ensure CSV file exists with headers.

        Args:
            filepath: Path to the CSV data file.
        """
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        if not self.filepath.exists():
            with open(self.filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "category", "amount", "description"])

    def add_expense(self, expense: Expense) -> None:
        """Append a single expense row to the CSV file.

        Args:
            expense: The Expense object to persist.
        """
        with open(self.filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                expense.date,
                expense.category,
                f"{expense.amount:.2f}",
                expense.description,
            ])

    def get_all(self) -> List[Expense]:
        """Return all expenses as a list of Expense objects.

        Returns:
            List of all Expense entries from the CSV file.
        """
        result: List[Expense] = []
        try:
            with open(self.filepath, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    result.append(Expense(
                        date=row["date"],
                        category=row["category"],
                        amount=float(row["amount"]),
                        description=row["description"],
                    ))
        except FileNotFoundError:
            pass
        return result

    def get_by_category(self, category: str) -> List[Expense]:
        """Filter expenses by category.

        Args:
            category: The category to filter by (case-insensitive).

        Returns:
            List of Expense objects matching the category.
        """
        return [
            e for e in self.get_all()
            if e.category.lower() == category.lower()
        ]

    def get_monthly_summary(self, year_month: str) -> dict[str, float]:
        """Return category totals for a given month.

        Args:
            year_month: Month in YYYY-MM format.

        Returns:
            Dictionary mapping category names to total amounts.
        """
        summary: dict[str, float] = {}
        for expense in self.get_all():
            if expense.month == year_month:
                summary[expense.category] = (
                    summary.get(expense.category, 0.0) + expense.amount
                )
        return summary

    def export_summary(self, filepath: str) -> None:
        """Write a human-readable summary report to a text file.

        Args:
            filepath: Destination path for the summary text file.
        """
        monthly: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
        for expense in self.get_all():
            monthly[expense.month][expense.category] += expense.amount

        with open(filepath, "w", encoding="utf-8") as f:
            for month in sorted(monthly):
                f.write(f"=== Monthly Summary: {month} ===\n")
                month_total = 0.0
                for category in sorted(monthly[month]):
                    total = monthly[month][category]
                    f.write(f"  {category}: ${total:.2f}\n")
                    month_total += total
                f.write(f"  {'─' * 30}\n")
                f.write(f"  Total: ${month_total:.2f}\n\n")


def demo() -> None:
    """Demonstrate ExpenseTracker with sample data."""
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmpdir:
        tracker = ExpenseTracker(os.path.join(tmpdir, "test.csv"))
        tracker.add_expense(Expense("2025-06-01", "Food", 12.50, "Lunch"))
        tracker.add_expense(Expense("2025-06-02", "Transport", 5.00, "Bus fare"))
        tracker.add_expense(Expense("2025-06-03", "Food", 8.75, "Coffee"))
        tracker.add_expense(Expense("2025-06-04", "Entertainment", 15.00, "Movie"))
        tracker.add_expense(Expense("2025-07-01", "Rent", 1000.00, "July rent"))

        print("All expenses:")
        for e in tracker.get_all():
            print(f"  {e.date} | {e.category:15s} | ${e.amount:.2f} | {e.description}")

        print(f"\nFood expenses:")
        for e in tracker.get_by_category("Food"):
            print(f"  {e.date} | ${e.amount:.2f} | {e.description}")

        print("\nMonthly summary 2025-06:")
        for cat, total in tracker.get_monthly_summary("2025-06").items():
            print(f"  {cat}: ${total:.2f}")

        summary_path = os.path.join(tmpdir, "summary.txt")
        tracker.export_summary(summary_path)
        print(f"\nSummary exported to {summary_path}")
        with open(summary_path) as f:
            print(f.read())


if __name__ == "__main__":
    demo()
