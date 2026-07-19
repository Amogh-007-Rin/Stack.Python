# Exercises: Introduction to Web Development: Flask Basics

Assume `from flask import Flask, request, render_template, redirect, url_for`.

## Exercise 1: Hello World
Create a Flask app with a single route `/` that returns "Hello, World!" as an HTML string.

## Exercise 2: Dynamic Route
Create a route `/user/<name>` that returns a personalized greeting: "Hello, [name]!".

## Exercise 3: Query Parameters
Create a route `/search` that reads a `q` query parameter and returns "You searched for: [q]". Handle the case where q is missing.

## Exercise 4: GET and POST Form
Create a route `/contact` that displays a simple HTML form (name, message) on GET and processes the form data on POST, returning a confirmation.

## Exercise 5: Redirect
After a successful POST on `/contact`, redirect to a `/thank-you` page instead of rendering directly.

## Exercise 6: JSON Response
Create an endpoint `/api/status` that returns a JSON response `{"status": "ok", "version": "1.0"}`.

## Exercise 7: URL Building
Use `url_for` to generate URLs for all the routes in your app. Print them at startup.

## Exercise 8: Template Rendering
Create a simple template (inline or file) and use `render_template` to display a list of items passed from the route.

## Challenge: Todo List API
Build a minimal Flask todo API:
- `GET /todos` — return all todos as JSON
- `POST /todos` — accept JSON `{"task": "..."}`, add to an in-memory list
- `GET /todos/<int:id>` — return a single todo
- `DELETE /todos/<int:id>` — remove a todo
Use an in-memory Python list as storage.
