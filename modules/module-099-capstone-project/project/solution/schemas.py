"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional, List, Dict

from pydantic import BaseModel, Field, field_validator


class CategoryCreate(BaseModel):
    """Schema for creating a new category."""

    name: str = Field(..., min_length=1, max_length=100)


class CategoryResponse(BaseModel):
    """Schema for category response data."""

    id: int
    name: str
    created_at: datetime

    model_config = {'from_attributes': True}


class TaskCreate(BaseModel):
    """Schema for creating a new task."""

    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(default='', max_length=5000)
    status: str = Field(default='pending')
    priority: int = Field(default=3, ge=1, le=5)
    category_id: Optional[int] = Field(default=None)

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: str) -> str:
        """Validate that status is one of the allowed values."""
        allowed: List[str] = ['pending', 'in_progress', 'completed']
        if v not in allowed:
            raise ValueError(f'Status must be one of {allowed}')
        return v


class TaskUpdate(BaseModel):
    """Schema for updating an existing task (all fields optional)."""

    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=5000)
    status: Optional[str] = Field(default=None)
    priority: Optional[int] = Field(default=None, ge=1, le=5)
    category_id: Optional[int] = Field(default=None)

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: Optional[str]) -> Optional[str]:
        """Validate status if provided."""
        if v is not None:
            allowed: List[str] = ['pending', 'in_progress', 'completed']
            if v not in allowed:
                raise ValueError(f'Status must be one of {allowed}')
        return v


class TaskResponse(BaseModel):
    """Schema for task response data."""

    id: int
    title: str
    description: str
    status: str
    priority: int
    created_at: datetime
    updated_at: datetime
    category_id: Optional[int]
    category_name: Optional[str] = None

    model_config = {'from_attributes': True}


class ImportResult(BaseModel):
    """Schema for CSV import result summary."""

    total_rows: int
    imported: int
    skipped: int
    errors: List[str]


class DashboardStats(BaseModel):
    """Schema for dashboard statistics."""

    total_tasks: int
    by_status: Dict[str, int]
    by_priority: Dict[str, int]
    recent_updates: int
