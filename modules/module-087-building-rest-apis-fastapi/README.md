# Module 087: Building REST APIs with FastAPI

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2.5 hours

## Learning Objectives

- Create REST API endpoints with FastAPI path operations
- Handle path parameters, query parameters, and request bodies
- Use Pydantic models for request/response validation
- Leverage automatic interactive documentation at /docs
- Understand dependency injection basics

## Topics Covered

1. FastAPI framework overview
2. Path operations (GET, POST, PUT, DELETE)
3. Path parameters and query parameters
4. Request body with Pydantic models
5. Response models
6. Automatic interactive docs (/docs, /redoc)
7. Dependency injection basics
8. Running with uvicorn

## Prerequisites

Modules 000-086.

## Key Concepts

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

items_db: list[Item] = []

@app.get("/")
def read_root() -> dict:
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(item: Item) -> Item:
    items_db.append(item)
    return item
```

## Resources

- FastAPI documentation: https://fastapi.tiangolo.com
- Pydantic documentation
- Uvicorn documentation
