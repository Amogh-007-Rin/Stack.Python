# Exercises: Building REST APIs with FastAPI

Assume `from fastapi import FastAPI` and Pydantic's `BaseModel`.

## Exercise 1: Basic FastAPI App
Create a FastAPI app with a root endpoint `GET /` returning `{"message": "Hello, FastAPI!"}`. Run with uvicorn.

## Exercise 2: Path Parameters
Create an endpoint `GET /items/{item_id}` that returns the item ID and an optional query parameter `q`.

## Exercise 3: Query Parameters
Create `GET /products/` that accepts `skip` (int, default 0) and `limit` (int, default 10) query parameters. Return a dict with these values plus a sample product list.

## Exercise 4: Request Body
Define a Pydantic model `Item` (name, price, is_offer: bool = False). Create `POST /items/` that accepts the model and returns it.

## Exercise 5: PUT Update
Create `PUT /items/{item_id}` that accepts an `Item` body and returns a confirmation message with the updated data.

## Exercise 6: DELETE
Create `DELETE /items/{item_id}` that returns `{"message": "Item deleted"}`.

## Exercise 7: Response Model
Create a Pydantic model `UserResponse` (id, name, email). Create `GET /users/{user_id}` that returns a `UserResponse`. Use `response_model` in the decorator.

## Exercise 8: Error Handling
Add proper HTTP exception handling: return 404 when an item is not found, 400 for validation errors.

## Challenge: Task Manager API
Build a full CRUD task manager API:
- `GET /tasks` — list all tasks with optional `status` filter
- `POST /tasks` — create a task (title, description, status)
- `GET /tasks/{id}` — get a single task
- `PUT /tasks/{id}` — update a task
- `DELETE /tasks/{id}` — delete a task
Use an in-memory list/dict. Add proper error handling and response models.
