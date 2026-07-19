#!/usr/bin/env python3
"""
Personal Expense Tracker — Full Solution.

A CSV-backed expense tracker with OOP design, error handling, and a CLI menu.

Usage:
    python project/solution/expense_tracker.py
"""

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


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

        Raises:
            IOError: If the file cannot be written to.
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

        The report groups expenses by month and shows category totals.

        Args:
            filepath: Destination path for the summary text file.
        """
        from collections import defaultdict

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


def get_float(prompt: str) -> Optional[float]:
    """Prompt the user for a float value with error handling.

    Args:
        prompt: The input prompt string.

    Returns:
        Float value if valid, None if the user cancels.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number. Please enter a valid numeric value.")
        return None


def main() -> None:
    """Run the expense tracker CLI main loop."""
    tracker = ExpenseTracker()

    while True:
        print("\n" + "=" * 40)
        print("  PERSONAL EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Monthly Summary")
        print("5. Export Summary")
        print("6. Exit")
        print("=" * 40)

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            category = input("Category: ").strip()
            amount = get_float("Amount: ")
            if amount is None:
                continue
            description = input("Description: ").strip()
            if not date or not category:
                print("Date and category are required.")
                continue
            tracker.add_expense(Expense(date, category, amount, description))
            print("Expense added!")

        elif choice == "2":
            expenses = tracker.get_all()
            if not expenses:
                print("No expenses recorded.")
                continue
            print(f"\n{'Date':<12} {'Category':<16} {'Amount':<8} Description")
            print("-" * 60)
            for e in expenses:
                print(f"{e.date:<12} {e.category:<16} ${e.amount:<6.2f} {e.description}")

        elif choice == "3":
            category = input("Category to filter: ").strip()
            expenses = tracker.get_by_category(category)
            if not expenses:
                print(f"No expenses found for category '{category}'.")
                continue
            total = sum(e.amount for e in expenses)
            print(f"\nExpenses in '{category}':")
            print("-" * 40)
            for e in expenses:
                print(f"{e.date}  ${e.amount:.2f}  {e.description}")
            print(f"{'─' * 40}")
            print(f"Total: ${total:.2f}")

        elif choice == "4":
            year_month = input("Month (YYYY-MM): ").strip()
            summary = tracker.get_monthly_summary(year_month)
            if not summary:
                print(f"No expenses for {year_month}.")
                continue
            total = sum(summary.values())
            print(f"\n=== Monthly Summary: {year_month} ===")
            for category in sorted(summary):
                print(f"  {category}: ${summary[category]:.2f}")
            print(f"  {'─' * 30}")
            print(f"  Total: ${total:.2f}")

        elif choice == "5":
            path = input("Export filename (default: summary.txt): ").strip()
            if not path:
                path = "summary.txt"
            try:
                tracker.export_summary(path)
                print(f"Summary exported to {path}")
            except IOError as e:
                print(f"Export failed: {e}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
