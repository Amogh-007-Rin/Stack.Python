# Exercises: Capstone Project: Full-Stack Application

## Exercise 1: Database Models
Define SQLAlchemy models for `Task` (id, title, description, status, priority, created_at, updated_at, category_id) and `Category` (id, name).

## Exercise 2: CRUD Endpoints
Create FastAPI endpoints for full CRUD operations on tasks:
- `GET /tasks` - list all tasks
- `GET /tasks/{id}` - get a single task
- `POST /tasks` - create a task
- `PUT /tasks/{id}` - update a task
- `DELETE /tasks/{id}` - delete a task

## Exercise 3: Input Validation
Use Pydantic models for request/response validation. Include validation for task status (enum: pending, in_progress, completed) and priority (1-5).

## Exercise 4: Data Ingestion
Create a `POST /tasks/import` endpoint that accepts a CSV file upload and bulk-imports tasks into the database. Handle duplicates gracefully.

## Exercise 5: Web UI with Jinja2
Create Jinja2 templates for:
- A task list page with filtering by status
- A task creation form
- A task detail/edit page
Use Bootstrap or simple CSS for styling.

## Exercise 6: Error Handling
Implement global exception handlers for:
- 404 Not Found
- 422 Validation Error
- 500 Internal Server Error
Log all errors with traceback information.

## Challenge: Dashboard with Statistics
Create a dashboard endpoint that returns:
- Total tasks count
- Tasks by status (pending, in_progress, completed)
- Tasks by priority
- Recently updated tasks (last 24 hours)
Expose both as a JSON API and a Jinja2 template.
