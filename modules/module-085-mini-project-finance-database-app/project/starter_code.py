"""
Personal Finance Database App - Starter Code

TODO: Implement each function following the type hints and docstrings.
"""

from datetime import datetime, date
from typing import List, Tuple, Dict, Optional

from sqlalchemy import (
    create_engine, Column, Integer, Float, String, DateTime, func,
)
from sqlalchemy.orm import declarative_base, sessionmaker, Session

Base = declarative_base()


class Transaction(Base):
    """Transaction model representing a financial transaction."""

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now)
    amount = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(String(255), default='')


# TODO: Implement this function
def init_db(db_path: str = 'finance.db') -> Session:
    """Initialize the database and return a configured session.

    Args:
        db_path: Path to the SQLite database file.

    Returns:
        SQLAlchemy Session instance.
    """
    pass


# TODO: Implement this function
def add_transaction(
    session: Session,
    date: date,
    amount: float,
    category: str,
    description: str,
) -> Transaction:
    """Add a new transaction to the database.

    Args:
        session: Active database session.
        date: Transaction date.
        amount: Transaction amount (positive for income, negative for expense).
        category: Transaction category.
        description: Optional description.

    Returns:
        The created Transaction object.
    """
    pass


# TODO: Implement this function
def get_all_transactions(session: Session) -> List[Transaction]:
    """Retrieve all transactions ordered by date descending.

    Args:
        session: Active database session.

    Returns:
        List of Transaction objects.
    """
    pass


# TODO: Implement this function
def delete_transaction(session: Session, transaction_id: int) -> bool:
    """Delete a transaction by its ID.

    Args:
        session: Active database session.
        transaction_id: ID of the transaction to delete.

    Returns:
        True if the transaction was deleted, False if not found.
    """
    pass


# TODO: Implement this function
def spending_by_category(session: Session) -> List[Tuple[str, float]]:
    """Calculate total spending (positive amounts) grouped by category.

    Args:
        session: Active database session.

    Returns:
        List of (category, total) tuples sorted by total descending.
    """
    pass


# TODO: Implement this function
def monthly_summary(session: Session) -> List[Dict[str, object]]:
    """Generate a monthly summary of income, expenses, and net.

    Args:
        session: Active database session.

    Returns:
        List of dicts with keys: month, income, expenses, net.
    """
    pass


# TODO: Implement CLI entry point
def main() -> None:
    """Run the Personal Finance CLI application."""
    pass


if __name__ == '__main__':
    main()
