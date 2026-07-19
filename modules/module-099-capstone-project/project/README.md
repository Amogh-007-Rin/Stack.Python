# Capstone Project: Task Manager (Full-Stack Application)

Build a complete Task Manager application with a FastAPI backend, SQLite database, data ingestion pipeline, and a Jinja2 web UI.

## Functional Requirements

### Phase 1: Database & Models
- Create SQLAlchemy models: `Task` (id, title, description, status, priority, created_at, updated_at, category_id) and `Category` (id, name)
- Use SQLite as the database engine
- Auto-create tables on startup

### Phase 2: API Endpoints
- `GET /tasks` - list all tasks (supports filtering by status, priority, category)
- `GET /tasks/{id}` - get a single task
- `POST /tasks` - create a task
- `PUT /tasks/{id}` - update a task
- `DELETE /tasks/{id}` - delete a task
- `POST /tasks/import` - bulk import tasks from CSV
- `GET /categories` - list all categories
- `GET /dashboard` - statistics endpoint

### Phase 3: Data Ingestion
- Accept CSV upload with columns: title, description, status, priority, category
- Validate each row before inserting
- Skip duplicates (same title)
- Return summary of imported/skipped rows

### Phase 4: Web UI (Jinja2 Templates)
- Task list page with search and filter controls
- Add/edit task form with dropdown for categories
- Task detail view
- Dashboard page with statistics (total tasks, by status, by priority)
- Responsive design with basic CSS styling

### Phase 5: Error Handling & Logging
- 404 handler for missing tasks
- 422 handler for validation errors
- 500 handler for unexpected errors
- Log all API requests and errors to `app.log`

## Stretch Goals

1. Add user authentication (simple token-based)
2. Add pagination to task listing
3. Add task due dates and overdue highlighting
4. Add export to CSV endpoint
5. Add unit tests with pytest
6. Dockerize the application

## Setup

```bash
pip install -r requirements.txt
python -m app
```

Open http://localhost:8000 in your browser.
API docs are at http://localhost:8000/docs.

## Project Structure

```
project/
├── README.md
├── starter_code.py
├── requirements.txt
└── solution/
    ├── app.py
    ├── models.py
    ├── database.py
    ├── schemas.py
    └── templates/
        ├── base.html
        ├── index.html
        └── tasks.html
```
