"""FastAPI application for the Task Manager."""

import csv
import io
import logging
from datetime import datetime, timedelta
from typing import List, Optional, Dict

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import func

from project.solution.database import init_db, get_db
from project.solution.models import Base, Task, Category, TaskStatus
from project.solution.schemas import (
    TaskCreate, TaskUpdate, TaskResponse,
    CategoryCreate, CategoryResponse,
    ImportResult, DashboardStats,
)

logger: logging.Logger = logging.getLogger(__name__)

app: FastAPI = FastAPI(title='Task Manager')
templates = Jinja2Templates(directory='project/solution/templates')


@app.on_event('startup')
def on_startup() -> None:
    """Initialize the database on application startup."""
    init_db()
    logger.info('Database initialized')


# ── Helper ──────────────────────────────────────────────────────────────


def _task_to_response(task: Task) -> TaskResponse:
    """Convert a Task ORM object to a TaskResponse schema.

    Args:
        task: The SQLAlchemy Task instance.

    Returns:
        TaskResponse with all fields populated.
    """
    return TaskResponse(
        id=task.id,
        title=task.title,
        description=task.description,
        status=task.status.value,
        priority=task.priority,
        created_at=task.created_at,
        updated_at=task.updated_at,
        category_id=task.category_id,
        category_name=task.category.name if task.category else None,
    )


# ── Category Endpoints ──────────────────────────────────────────────────


@app.get('/categories', response_model=List[CategoryResponse])
def list_categories(db: Session = Depends(get_db)) -> List[CategoryResponse]:
    """List all task categories.

    Args:
        db: Database session dependency.

    Returns:
        List of category response objects.
    """
    categories: List[Category] = db.query(Category).all()
    return [
        CategoryResponse(id=c.id, name=c.name, created_at=c.created_at)
        for c in categories
    ]


@app.post('/categories', response_model=CategoryResponse, status_code=201)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
) -> CategoryResponse:
    """Create a new category.

    Args:
        data: Category creation data.
        db: Database session dependency.

    Returns:
        The created category.

    Raises:
        HTTPException 400: If the category name already exists.
    """
    existing: Optional[Category] = db.query(Category).filter(
        Category.name == data.name
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail='Category already exists')

    category: Category = Category(name=data.name)
    db.add(category)
    db.commit()
    db.refresh(category)
    logger.info(f'Created category: {category.name}')
    return CategoryResponse(id=category.id, name=category.name, created_at=category.created_at)


# ── Task Endpoints ──────────────────────────────────────────────────────


@app.get('/tasks', response_model=List[TaskResponse])
def list_tasks(
    status: Optional[str] = None,
    priority: Optional[int] = None,
    category_id: Optional[int] = None,
    db: Session = Depends(get_db),
) -> List[TaskResponse]:
    """List tasks with optional filtering.

    Args:
        status: Filter by task status (pending, in_progress, completed).
        priority: Filter by priority (1-5).
        category_id: Filter by category ID.
        db: Database session dependency.

    Returns:
        Filtered list of task responses.
    """
    query = db.query(Task)

    if status:
        query = query.filter(Task.status == TaskStatus(status))
    if priority:
        query = query.filter(Task.priority == priority)
    if category_id:
        query = query.filter(Task.category_id == category_id)

    tasks: List[Task] = query.order_by(Task.created_at.desc()).all()
    return [_task_to_response(t) for t in tasks]


@app.get('/tasks/{task_id}', response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)) -> TaskResponse:
    """Get a single task by ID.

    Args:
        task_id: The task ID.
        db: Database session dependency.

    Returns:
        The task response.

    Raises:
        HTTPException 404: If the task is not found.
    """
    task: Optional[Task] = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return _task_to_response(task)


@app.post('/tasks', response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate, db: Session = Depends(get_db)) -> TaskResponse:
    """Create a new task.

    Args:
        data: Task creation data.
        db: Database session dependency.

    Returns:
        The created task response.

    Raises:
        HTTPException 404: If the specified category does not exist.
    """
    if data.category_id:
        category: Optional[Category] = db.query(Category).filter(
            Category.id == data.category_id
        ).first()
        if not category:
            raise HTTPException(status_code=404, detail='Category not found')

    task: Task = Task(
        title=data.title,
        description=data.description or '',
        status=TaskStatus(data.status),
        priority=data.priority,
        category_id=data.category_id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    logger.info(f'Created task: {task.title}')
    return _task_to_response(task)


@app.put('/tasks/{task_id}', response_model=TaskResponse)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
) -> TaskResponse:
    """Update an existing task.

    Args:
        task_id: The task ID to update.
        data: Fields to update.
        db: Database session dependency.

    Returns:
        The updated task response.

    Raises:
        HTTPException 404: If the task or category is not found.
    """
    task: Optional[Task] = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')

    if data.title is not None:
        task.title = data.title
    if data.description is not None:
        task.description = data.description
    if data.status is not None:
        task.status = TaskStatus(data.status)
    if data.priority is not None:
        task.priority = data.priority
    if data.category_id is not None:
        category: Optional[Category] = db.query(Category).filter(
            Category.id == data.category_id
        ).first()
        if not category:
            raise HTTPException(status_code=404, detail='Category not found')
        task.category_id = data.category_id

    db.commit()
    db.refresh(task)
    logger.info(f'Updated task: {task.title}')
    return _task_to_response(task)


@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> None:
    """Delete a task by ID.

    Args:
        task_id: The task ID to delete.
        db: Database session dependency.

    Raises:
        HTTPException 404: If the task is not found.
    """
    task: Optional[Task] = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    db.delete(task)
    db.commit()
    logger.info(f'Deleted task: {task.title}')


# ── Data Ingestion ──────────────────────────────────────────────────────


@app.post('/tasks/import', response_model=ImportResult)
async def import_tasks(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> ImportResult:
    """Import tasks from a CSV file upload.

    Expected CSV columns: title, description, status, priority, category_name.

    Args:
        file: The uploaded CSV file.
        db: Database session dependency.

    Returns:
        Import result summary with counts and any errors.
    """
    content: bytes = await file.read()
    text: str = content.decode('utf-8')
    reader = csv.DictReader(io.StringIO(text))

    total_rows: int = 0
    imported: int = 0
    skipped: int = 0
    errors: List[str] = []

    for row in reader:
        total_rows += 1
        try:
            title: str = row.get('title', '').strip()
            if not title:
                skipped += 1
                errors.append(f'Row {total_rows}: Empty title')
                continue

            existing: Optional[Task] = db.query(Task).filter(
                Task.title == title
            ).first()
            if existing:
                skipped += 1
                continue

            status_str: str = row.get('status', 'pending').strip()
            priority_str: str = row.get('priority', '3').strip()
            category_name: str = row.get('category_name', '').strip()

            category_id: Optional[int] = None
            if category_name:
                category: Optional[Category] = db.query(Category).filter(
                    Category.name == category_name
                ).first()
                if not category:
                    category = Category(name=category_name)
                    db.add(category)
                    db.flush()
                category_id = category.id

            task: Task = Task(
                title=title,
                description=row.get('description', '').strip(),
                status=TaskStatus(status_str) if status_str in [
                    'pending', 'in_progress', 'completed'
                ] else TaskStatus.PENDING,
                priority=int(priority_str) if priority_str.isdigit() else 3,
                category_id=category_id,
            )
            db.add(task)
            imported += 1
        except Exception as e:
            skipped += 1
            errors.append(f'Row {total_rows}: {str(e)}')

    db.commit()
    logger.info(f'Import: {imported} imported, {skipped} skipped from {total_rows} rows')
    return ImportResult(
        total_rows=total_rows,
        imported=imported,
        skipped=skipped,
        errors=errors,
    )


# ── Dashboard ───────────────────────────────────────────────────────────


@app.get('/dashboard', response_model=DashboardStats)
def get_dashboard(db: Session = Depends(get_db)) -> DashboardStats:
    """Get dashboard statistics.

    Args:
        db: Database session dependency.

    Returns:
        Dashboard statistics including counts by status and priority.
    """
    total_tasks: int = db.query(Task).count()

    by_status: Dict[str, int] = {}
    for status in TaskStatus:
        count: int = db.query(Task).filter(Task.status == status).count()
        by_status[status.value] = count

    by_priority: Dict[str, int] = {}
    for p in range(1, 6):
        count = db.query(Task).filter(Task.priority == p).count()
        by_priority[str(p)] = count

    recent_threshold: datetime = datetime.utcnow() - timedelta(hours=24)
    recent_updates: int = db.query(Task).filter(
        Task.updated_at >= recent_threshold
    ).count()

    return DashboardStats(
        total_tasks=total_tasks,
        by_status=by_status,
        by_priority=by_priority,
        recent_updates=recent_updates,
    )


# ── Web UI ──────────────────────────────────────────────────────────────


@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    """Render the main task list page.

    Args:
        request: The HTTP request.
        db: Database session dependency.

    Returns:
        HTML response with the task list template.
    """
    tasks: List[Task] = db.query(Task).order_by(Task.created_at.desc()).all()
    categories: List[Category] = db.query(Category).all()
    return templates.TemplateResponse('index.html', {
        'request': request,
        'tasks': tasks,
        'categories': categories,
    })


@app.get('/tasks/{task_id}/edit', response_class=HTMLResponse)
def edit_task_page(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db),
) -> HTMLResponse:
    """Render the task edit form page.

    Args:
        task_id: The task ID to edit.
        request: The HTTP request.
        db: Database session dependency.

    Returns:
        HTML response with the task edit template.

    Raises:
        HTTPException 404: If the task is not found.
    """
    task: Optional[Task] = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    categories = db.query(Category).all()
    return templates.TemplateResponse('tasks.html', {
        'request': request,
        'task': task,
        'categories': categories,
    })


@app.get('/dashboard/page', response_class=HTMLResponse)
def dashboard_page(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    """Render the dashboard statistics page.

    Args:
        request: The HTTP request.
        db: Database session dependency.

    Returns:
        HTML response with the dashboard template.
    """
    stats: DashboardStats = get_dashboard(db)
    return templates.TemplateResponse('dashboard.html', {
        'request': request,
        'stats': stats,
    })


# ── Error Handlers ──────────────────────────────────────────────────────


@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException) -> HTMLResponse:
    """Handle 404 errors with a custom template.

    Args:
        request: The HTTP request that caused the error.
        exc: The exception instance.

    Returns:
        HTML response with error details.
    """
    logger.warning(f'404: {request.url.path}')
    return templates.TemplateResponse('404.html', {
        'request': request,
        'detail': exc.detail,
    }, status_code=404)


@app.exception_handler(500)
async def internal_error_handler(request: Request, exc: Exception) -> HTMLResponse:
    """Handle 500 errors with logging.

    Args:
        request: The HTTP request that caused the error.
        exc: The exception instance.

    Returns:
        HTML response with error details.
    """
    logger.error(f'500: {request.url.path} - {str(exc)}', exc_info=True)
    return templates.TemplateResponse('500.html', {
        'request': request,
        'detail': 'Internal server error',
    }, status_code=500)


# ── Entry Point ─────────────────────────────────────────────────────────


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('project.solution.app:app', host='0.0.0.0', port=8000, reload=True)
