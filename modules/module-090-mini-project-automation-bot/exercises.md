# Exercises: Milestone Project: Personal Automation Bot / Mini API

These exercises guide you through building the automation bot. Complete all to finish the milestone.

## Exercise 1: FastAPI App Setup
Create a FastAPI app with a `GET /` endpoint returning `{"status": "Automation Bot running"}`.

## Exercise 2: File Listing Endpoint
Create `GET /files` that accepts a `path` query parameter and returns a list of files and directories at that path. Return name, size, type (file/dir) for each.

## Exercise 3: File Organization Endpoint
Create `POST /organize` that accepts a `directory` path in the request body. Organize files in that directory by extension (Images, Documents, etc.). Return a summary of what was moved.

## Exercise 4: System Info Endpoint
Create `GET /system-info` that returns CPU usage, memory usage, disk usage, and OS information. Use `psutil` if available, otherwise use `os` and `shutil`.

## Exercise 5: Scheduled Task Endpoint
Create `POST /schedule-task` that accepts a task name, interval (e.g., "daily", "hourly"), and action. Store scheduled tasks in memory and run them in a background thread.

## Exercise 6: Action Logging
Add logging to every endpoint. Log the timestamp, endpoint called, parameters, and result status. Use Python's `logging` module and write to `bot.log`.

## Exercise 7: Error Handling
Add proper error handling to all endpoints. Return appropriate HTTP status codes and error messages. Handle cases where directories don't exist or paths are invalid.

## Exercise 8: CLI Interface
Add a CLI mode that accepts commands: `list <path>`, `organize <dir>`, `info`, `schedule <name> <interval>`. Use `argparse`.

## Challenge: Full Auto-Bot
Enhance the bot with:
- Authentication via API key (header-based)
- A `GET /logs` endpoint that returns recent log entries
- A `DELETE /tasks/{task_id}` endpoint to remove scheduled tasks
- A webhook endpoint `POST /webhook` that accepts a JSON payload and triggers an action based on content
- Unit tests for at least 3 endpoints using FastAPI `TestClient`
