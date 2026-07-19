# Personal Automation Bot / Mini API

A FastAPI-based automation bot that provides file management, system information, scheduled tasks, and action logging through a REST API and CLI interface.

## Features

- List files and directories at any path (`GET /files`)
- Organize files by type into subdirectories (`POST /organize`)
- System information endpoint (`GET /system-info`)
- Schedule recurring tasks (`POST /schedule-task`)
- View recent logs (`GET /logs`)
- Remove scheduled tasks (`DELETE /tasks/{id}`)
- CLI mode for common operations

## Setup

```bash
pip install fastapi uvicorn schedule
```

## Usage

### API Mode

```bash
python automation_bot.py
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

### CLI Mode

```bash
# List files
python automation_bot.py list /path/to/dir

# Organize a directory
python automation_bot.py organize ~/Downloads

# Show system info
python automation_bot.py info

# Schedule a task
python automation_bot.py schedule my_task daily
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Bot status |
| GET | `/files?path=...` | List files in directory |
| POST | `/organize` | Organize files by type |
| GET | `/system-info` | System information |
| POST | `/schedule-task` | Schedule a recurring task |
| GET | `/logs?lines=20` | View recent log entries |
| DELETE | `/tasks/{id}` | Remove a scheduled task |

## Starter Code

Open `starter_code.py` and follow the TODO comments. The solution is in `solution/automation_bot.py`.

## Requirements

- Python 3.9+
- FastAPI
- uvicorn
