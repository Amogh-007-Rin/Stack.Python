"""
Solutions: Milestone Project - Personal Automation Bot / Mini API

FastAPI-based automation bot with file management, system info,
task scheduling, and action logging.
Google-style docstrings and complete type hints throughout.
"""

import logging
import os
import shutil
import time
import threading
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

app: FastAPI = FastAPI(title='Automation Bot')

scheduled_tasks: Dict[int, Dict] = {}
task_counter: int = 0


# ---------------------------------------------------------------------------
# Pydantic Models
# ---------------------------------------------------------------------------

class FileInfo(BaseModel):
    name: str
    size: int
    type: str
    path: str


class OrganizeRequest(BaseModel):
    directory: str


class OrganizeResponse(BaseModel):
    summary: Dict[str, int]
    total: int


class TaskRequest(BaseModel):
    name: str
    interval: str
    action: str


class TaskResponse(BaseModel):
    id: int
    name: str
    interval: str
    action: str
    status: str


class SystemInfo(BaseModel):
    os: str
    cpu_count: int
    cwd: str
    disk_usage: Dict[str, str]


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def log_action(endpoint: str, params: object, status: str = 'ok') -> None:
    """Log an API action to the log file.

    Args:
        endpoint: The API endpoint called.
        params: Parameters passed to the endpoint.
        status: Result status ('ok' or 'error').
    """
    logging.info(f'{endpoint} | params={params} | status={status}')


def get_file_type(filename: str) -> str:
    """Determine file type category from extension.

    Args:
        filename: Name of the file.

    Returns:
        Category string (Images, Documents, Audio, Archives, Videos, Others).
    """
    ext: str = Path(filename).suffix.lower()
    mapping: Dict[str, str] = {
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
        '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
        '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
        '.zip': 'Archives', '.tar': 'Archives', '.gz': 'Archives', '.rar': 'Archives',
        '.mp4': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
    }
    return mapping.get(ext, 'Others')


# ---------------------------------------------------------------------------
# Background Task Runner
# ---------------------------------------------------------------------------

def run_scheduled_task(task_id: int) -> None:
    """Run a scheduled task at the specified interval.

    Args:
        task_id: ID of the task to run.
    """
    task: Dict = scheduled_tasks.get(task_id, {})
    if not task:
        return

    interval_seconds: int = {
        'hourly': 3600,
        'daily': 86400,
        'weekly': 604800,
    }.get(task.get('interval', ''), 86400)

    while task.get('status') == 'running':
        logging.info(f'Running scheduled task: {task["name"]} - {task["action"]}')
        print(f'[{datetime.now()}] Task {task["name"]}: executing {task["action"]}')
        time.sleep(interval_seconds)


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get('/')
def read_root() -> Dict[str, str]:
    """Root endpoint returning bot status.

    Returns:
        Status message.
    """
    log_action('GET /', {})
    return {'status': 'Automation Bot running'}


@app.get('/files', response_model=List[FileInfo])
def list_files(path: str = '.') -> List[FileInfo]:
    """List files and directories at the specified path.

    Args:
        path: Directory path to list.

    Returns:
        List of FileInfo objects.

    Raises:
        HTTPException: If the path is not a valid directory.
    """
    log_action('GET /files', {'path': path})

    if not os.path.isdir(path):
        logging.error(f'Invalid directory: {path}')
        raise HTTPException(status_code=404, detail=f'Directory not found: {path}')

    entries: List[FileInfo] = []
    for entry in sorted(os.listdir(path)):
        full_path: str = os.path.join(path, entry)
        is_dir: bool = os.path.isdir(full_path)
        entries.append(FileInfo(
            name=entry,
            size=os.path.getsize(full_path) if not is_dir else 0,
            type='directory' if is_dir else 'file',
            path=full_path,
        ))
    return entries


@app.post('/organize', response_model=OrganizeResponse)
def organize_directory(request: OrganizeRequest) -> OrganizeResponse:
    """Organize files in a directory by type into subfolders.

    Args:
        request: OrganizeRequest with the directory path.

    Returns:
        OrganizeResponse with a summary of what was moved.

    Raises:
        HTTPException: If the directory does not exist.
    """
    log_action('POST /organize', {'directory': request.directory})

    target_dir: str = request.directory
    if not os.path.isdir(target_dir):
        raise HTTPException(status_code=404, detail=f'Directory not found: {target_dir}')

    summary: Dict[str, int] = {}
    total: int = 0

    for filename in os.listdir(target_dir):
        filepath: str = os.path.join(target_dir, filename)
        if os.path.isdir(filepath):
            continue

        category: str = get_file_type(filename)
        category_dir: str = os.path.join(target_dir, category)
        os.makedirs(category_dir, exist_ok=True)

        dest: str = os.path.join(category_dir, filename)
        shutil.move(filepath, dest)
        summary[category] = summary.get(category, 0) + 1
        total += 1

    logging.info(f'Organized {total} files in {target_dir}: {summary}')
    return OrganizeResponse(summary=summary, total=total)


@app.get('/system-info', response_model=SystemInfo)
def get_system_info() -> SystemInfo:
    """Get system information.

    Returns:
        SystemInfo with OS, CPU count, CWD, and disk usage.
    """
    log_action('GET /system-info', {})

    total, used, free = shutil.disk_usage('.')
    return SystemInfo(
        os=os.name,
        cpu_count=os.cpu_count() or 0,
        cwd=os.getcwd(),
        disk_usage={
            'total': f'{total / (1024**3):.1f} GB',
            'used': f'{used / (1024**3):.1f} GB',
            'free': f'{free / (1024**3):.1f} GB',
        },
    )


@app.post('/schedule-task', response_model=TaskResponse)
def schedule_task(request: TaskRequest) -> TaskResponse:
    """Schedule a recurring task.

    Args:
        request: TaskRequest with name, interval, and action.

    Returns:
        TaskResponse with the created task details.
    """
    global task_counter
    task_counter += 1
    task_id: int = task_counter

    task: Dict = {
        'id': task_id,
        'name': request.name,
        'interval': request.interval,
        'action': request.action,
        'status': 'running',
    }
    scheduled_tasks[task_id] = task

    thread: threading.Thread = threading.Thread(
        target=run_scheduled_task, args=(task_id,), daemon=True
    )
    thread.start()

    logging.info(f'Scheduled task {task_id}: {request.name}')
    log_action('POST /schedule-task', request.model_dump())

    return TaskResponse(**task)


@app.get('/logs')
def get_logs(lines: int = 20) -> Dict[str, List[str]]:
    """Return recent log entries.

    Args:
        lines: Number of log lines to return (default 20).

    Returns:
        Dict containing the log lines.
    """
    log_action('GET /logs', {'lines': lines})

    if not os.path.exists('bot.log'):
        return {'logs': []}

    with open('bot.log', 'r') as f:
        all_lines: List[str] = f.readlines()

    return {'logs': all_lines[-lines:]}


@app.delete('/tasks/{task_id}')
def delete_task(task_id: int) -> Dict[str, str]:
    """Remove a scheduled task.

    Args:
        task_id: ID of the task to remove.

    Returns:
        Confirmation message.

    Raises:
        HTTPException: If the task ID is not found.
    """
    log_action('DELETE /tasks', {'task_id': task_id})

    if task_id not in scheduled_tasks:
        raise HTTPException(status_code=404, detail=f'Task {task_id} not found')

    scheduled_tasks[task_id]['status'] = 'stopped'
    del scheduled_tasks[task_id]
    return {'message': f'Task {task_id} removed'}


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def cli_main() -> None:
    """Run the automation bot in CLI mode."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Automation Bot CLI'
    )
    subparsers = parser.add_subparsers(dest='command')

    list_parser = subparsers.add_parser('list', help='List files in a directory')
    list_parser.add_argument('path', nargs='?', default='.', help='Directory path')

    organize_parser = subparsers.add_parser('organize', help='Organize a directory')
    organize_parser.add_argument('directory', help='Directory to organize')

    info_parser = subparsers.add_parser('info', help='Show system info')

    schedule_parser = subparsers.add_parser('schedule', help='Schedule a task')
    schedule_parser.add_argument('name', help='Task name')
    schedule_parser.add_argument('interval', choices=['hourly', 'daily', 'weekly'], help='Interval')

    args: argparse.Namespace = parser.parse_args()

    if args.command == 'list':
        path: str = args.path
        if not os.path.isdir(path):
            print(f'Error: {path} is not a directory')
            return
        for entry in sorted(os.listdir(path)):
            full: str = os.path.join(path, entry)
            size: str = f'({os.path.getsize(full)} bytes)' if os.path.isfile(full) else '[DIR]'
            print(f'{size:>12}  {entry}')

    elif args.command == 'organize':
        from fastapi.testclient import TestClient
        client = TestClient(app)
        response = client.post('/organize', json={'directory': args.directory})
        if response.status_code == 200:
            data: Dict = response.json()
            print(f'Organized {data["total"]} files:')
            for category, count in data['summary'].items():
                print(f'  {category}: {count}')
        else:
            print(f'Error: {response.json()}')

    elif args.command == 'info':
        client = TestClient(app)
        response = client.get('/system-info')
        if response.status_code == 200:
            data = response.json()
            for key, value in data.items():
                print(f'{key}: {value}')

    elif args.command == 'schedule':
        client = TestClient(app)
        response = client.post(
            '/schedule-task',
            json={'name': args.name, 'interval': args.interval, 'action': 'cli_task'},
        )
        if response.status_code == 200:
            data = response.json()
            print(f'Scheduled task #{data["id"]}: {data["name"]} ({data["interval"]})')
        else:
            print(f'Error: {response.json()}')

    else:
        parser.print_help()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        cli_main()
    else:
        import uvicorn
        uvicorn.run(app, host='0.0.0.0', port=8000)
