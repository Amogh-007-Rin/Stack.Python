"""
Capstone: Task Manager - Starter Code

TODO: Implement each function following the type hints and docstrings.
"""

import logging
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

logging.basicConfig(
    filename='app.log', level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger: logging.Logger = logging.getLogger(__name__)

app: FastAPI = FastAPI(title='Task Manager')

# TODO: Database setup
# engine = create_engine(...)
# SessionLocal = sessionmaker(...)
# Base = declarative_base()


# TODO: Define SQLAlchemy models
# class Category(Base): ...
# class Task(Base): ...


# TODO: Define Pydantic schemas
# class TaskCreate(BaseModel): ...
# class TaskResponse(BaseModel): ...
# class CategoryCreate(BaseModel): ...
# class CategoryResponse(BaseModel): ...


# TODO: Dependency for DB session
# def get_db(): ...


# TODO: Implement CRUD endpoints
# @app.get('/tasks')
# def list_tasks(status: Optional[str] = None, db=Depends(get_db)): ...


# TODO: Implement CSV import
# @app.post('/tasks/import')
# def import_tasks(file: UploadFile, db=Depends(get_db)): ...


# TODO: Implement Jinja2 templates
# @app.get('/', response_class=HTMLResponse)
# def index(request: Request): ...


# TODO: Implement error handlers
# @app.exception_handler(HTTPException)
# async def http_exception_handler(request, exc): ...


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
