"""Database configuration and session management."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator

DATABASE_URL: str = 'sqlite:///./tasks.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db() -> None:
    """Create all database tables.

    Should be called once on application startup.
    """
    import project.solution.models  # noqa: F401  # Register models
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency providing a database session.

    Yields:
        SQLAlchemy Session instance.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
