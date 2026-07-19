# Solutions: Building REST APIs with FastAPI

## Exercise 1: Basic FastAPI App
```python
from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
def read_root() -> dict:
    return {"message": "Hello, FastAPI!"}
```

## Exercise 2: Path Parameters
```python
from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "q": q}
```

## Exercise 3: Query Parameters
```python
from fastapi import FastAPI

app: FastAPI = FastAPI()

sample_products: list[dict] = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mouse"},
    {"id": 3, "name": "Keyboard"},
]

@app.get("/products/")
def list_products(skip: int = 0, limit: int = 10) -> dict:
    return {
        "skip": skip,
        "limit": limit,
        "products": sample_products[skip:skip + limit],
    }
```

## Exercise 4: Request Body
```python
from fastapi import FastAPI
from pydantic import BaseModel

app: FastAPI = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item) -> Item:
    return item
```

## Exercise 5: PUT Update
```python
from fastapi import FastAPI
from pydantic import BaseModel

app: FastAPI = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict:
    return {"message": f"Item {item_id} updated", "data": item.model_dump()}
```

## Exercise 6: DELETE
```python
from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict:
    return {"message": f"Item {item_id} deleted"}
```

## Exercise 7: Response Model
```python
from fastapi import FastAPI
from pydantic import BaseModel

app: FastAPI = FastAPI()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

users_db: dict[int, UserResponse] = {
    1: UserResponse(id=1, name="Alice", email="alice@example.com"),
    2: UserResponse(id=2, name="Bob", email="bob@example.com"),
}

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> UserResponse:
    return users_db[user_id]
```

## Exercise 8: Error Handling
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app: FastAPI = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items_db: Dict[int, Item] = {
    1: Item(name="Laptop", price=999.99),
    2: Item(name="Mouse", price=19.99),
}

@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.post("/items/")
def create_item(item: Item) -> Item:
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    new_id: int = max(items_db.keys()) + 1 if items_db else 1
    items_db[new_id] = item
    return item
```

## Challenge: Task Manager API
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional

app: FastAPI = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    status: str = "pending"

class Task(TaskCreate):
    id: int

tasks_db: Dict[int, Task] = {}
next_id: int = 1

@app.get("/tasks", response_model=List[Task])
def list_tasks(status: Optional[str] = None) -> List[Task]:
    tasks: List[Task] = list(tasks_db.values())
    if status:
        tasks = [t for t in tasks if t.status == status]
    return tasks

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate) -> Task:
    global next_id
    new_task: Task = Task(id=next_id, **task.model_dump())
    tasks_db[next_id] = new_task
    next_id += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate) -> Task:
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    updated: Task = Task(id=task_id, **task.model_dump())
    tasks_db[task_id] = updated
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict:
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"message": "Task deleted"}
```
