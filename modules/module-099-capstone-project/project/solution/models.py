"""SQLAlchemy ORM models for the Task Manager application."""

from datetime import datetime
from typing import Any

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship

from project.solution.database import Base
import enum


class TaskStatus(str, enum.Enum):
    """Enumeration of possible task statuses."""

    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


class Category(Base):
    """Represents a task category."""

    __tablename__ = 'categories'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), unique=True, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)

    tasks: Any = relationship('Task', back_populates='category')

    def __repr__(self) -> str:
        """Return string representation of the category."""
        return f'<Category(id={self.id}, name="{self.name}")>'


class Task(Base):
    """Represents a task in the task manager."""

    __tablename__ = 'tasks'

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(Text, default='')
    status: TaskStatus = Column(SAEnum(TaskStatus), default=TaskStatus.PENDING)
    priority: int = Column(Integer, default=3)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id: int = Column(Integer, ForeignKey('categories.id'), nullable=True)

    category: Any = relationship('Category', back_populates='tasks')

    def __repr__(self) -> str:
        """Return string representation of the task."""
        return f'<Task(id={self.id}, title="{self.title}", status={self.status})>'
