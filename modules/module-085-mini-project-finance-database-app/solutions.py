"""
Solutions: Milestone Project - Personal Finance Database App

SQLite-backed personal finance manager using SQLAlchemy.
Google-style docstrings and complete type hints throughout.
"""

from datetime import datetime, date
from typing import List, Tuple, Dict, Optional

from sqlalchemy import (
    create_engine, Column, Integer, Float, String, DateTime, func,
)
from sqlalchemy.orm import declarative_base, sessionmaker, Session

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.now)
    amount = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(String(255), default='')

    def __repr__(self) -> str:
        return (
            f"Transaction(id={self.id}, date={self.date.date()}, "
            f"amount={self.amount}, category='{self.category}')"
        )


def init_db(db_path: str = 'finance.db') -> Session:
    """Initialize the database and return a configured session.

    Args:
        db_path: Path to the SQLite database file.

    Returns:
        SQLAlchemy Session instance.
    """
    engine = create_engine(f'sqlite:///{db_path}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


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
    transaction: Transaction = Transaction(
        date=datetime.combine(date, datetime.min.time()),
        amount=amount,
        category=category,
        description=description,
    )
    session.add(transaction)
    session.commit()
    return transaction


def get_all_transactions(session: Session) -> List[Transaction]:
    """Retrieve all transactions ordered by date descending.

    Args:
        session: Active database session.

    Returns:
        List of Transaction objects.
    """
    return session.query(Transaction).order_by(Transaction.date.desc()).all()


def delete_transaction(session: Session, transaction_id: int) -> bool:
    """Delete a transaction by its ID.

    Args:
        session: Active database session.
        transaction_id: ID of the transaction to delete.

    Returns:
        True if the transaction was deleted, False if not found.
    """
    transaction: Optional[Transaction] = session.query(Transaction).filter_by(
        id=transaction_id
    ).first()
    if transaction:
        session.delete(transaction)
        session.commit()
        return True
    return False


def spending_by_category(session: Session) -> List[Tuple[str, float]]:
    """Calculate total spending (positive amounts) grouped by category.

    Args:
        session: Active database session.

    Returns:
        List of (category, total) tuples sorted by total descending.
    """
    results: List[Tuple[str, float]] = (
        session.query(
            Transaction.category,
            func.sum(Transaction.amount).label('total'),
        )
        .filter(Transaction.amount > 0)
        .group_by(Transaction.category)
        .order_by(func.sum(Transaction.amount).desc())
        .all()
    )
    return results


def monthly_summary(session: Session) -> List[Dict[str, object]]:
    """Generate a monthly summary of income, expenses, and net.

    Args:
        session: Active database session.

    Returns:
        List of dicts with keys: month, income, expenses, net.
    """
    rows: List[Tuple[str, float, float]] = (
        session.query(
            func.strftime('%Y-%m', Transaction.date).label('month'),
            func.sum(Transaction.amount).filter(Transaction.amount > 0).label('income'),
            func.sum(Transaction.amount).filter(Transaction.amount < 0).label('expenses'),
        )
        .group_by('month')
        .order_by('month')
        .all()
    )
    summaries: List[Dict[str, object]] = []
    for month, income, expenses in rows:
        income_val: float = income or 0.0
        expenses_val: float = abs(expenses) if expenses else 0.0
        summaries.append({
            'month': month,
            'income': income_val,
            'expenses': expenses_val,
            'net': income_val - expenses_val,
        })
    return summaries


def display_transactions(transactions: List[Transaction]) -> None:
    """Print transactions in a formatted table.

    Args:
        transactions: List of Transaction objects to display.
    """
    if not transactions:
        print('No transactions found.')
        return
    print(f'\n{"ID":<4} {"Date":<12} {"Amount":<10} {"Category":<15} {"Description"}')
    print('-' * 65)
    for t in transactions:
        print(
            f'{t.id:<4} {t.date.strftime("%Y-%m-%d"):<12} '
            f'{t.amount:<10.2f} {t.category:<15} {t.description}'
        )
    print()


def display_category_report(report: List[Tuple[str, float]]) -> None:
    """Print spending by category report.

    Args:
        report: List of (category, total) tuples.
    """
    if not report:
        print('No spending data.')
        return
    print(f'\n{"Category":<20} {"Total Spent"}')
    print('-' * 35)
    for category, total in report:
        print(f'{category:<20} ${total:.2f}')
    print()


def display_monthly_summary(summaries: List[Dict[str, object]]) -> None:
    """Print monthly summary report.

    Args:
        summaries: List of monthly summary dicts.
    """
    if not summaries:
        print('No data for monthly summary.')
        return
    print(f'\n{"Month":<10} {"Income":<12} {"Expenses":<12} {"Net"}')
    print('-' * 50)
    for s in summaries:
        print(
            f'{s["month"]:<10} ${s["income"]:<8.2f} '
            f'${s["expenses"]:<8.2f} ${s["net"]:<.2f}'
        )
    print()


def main() -> None:
    """Run the Personal Finance CLI application."""
    session: Session = init_db()

    while True:
        print('\n=== Personal Finance Manager ===')
        print('1. Add Transaction')
        print('2. View All Transactions')
        print('3. Delete Transaction')
        print('4. Spending by Category')
        print('5. Monthly Summary')
        print('6. Exit')
        choice: str = input('\nChoose an option: ').strip()

        if choice == '1':
            date_str: str = input('Date (YYYY-MM-DD) [today]: ').strip() or date.today().isoformat()
            try:
                trans_date: date = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                print('Invalid date format.')
                continue
            try:
                amount: float = float(input('Amount (+income / -expense): ').strip())
            except ValueError:
                print('Invalid amount.')
                continue
            category: str = input('Category: ').strip()
            description: str = input('Description: ').strip()
            add_transaction(session, trans_date, amount, category, description)
            print('Transaction added.')

        elif choice == '2':
            transactions: List[Transaction] = get_all_transactions(session)
            display_transactions(transactions)

        elif choice == '3':
            try:
                t_id: int = int(input('Transaction ID to delete: ').strip())
            except ValueError:
                print('Invalid ID.')
                continue
            if delete_transaction(session, t_id):
                print('Transaction deleted.')
            else:
                print('Transaction not found.')

        elif choice == '4':
            report: List[Tuple[str, float]] = spending_by_category(session)
            display_category_report(report)

        elif choice == '5':
            summaries: List[Dict[str, object]] = monthly_summary(session)
            display_monthly_summary(summaries)

        elif choice == '6':
            print('Goodbye!')
            break

        else:
            print('Invalid option. Please choose 1-6.')

    session.close()


if __name__ == '__main__':
    main()
