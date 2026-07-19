# Module 086: Introduction to Web Development: Flask Basics

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2.5 hours

## Learning Objectives

- Create routes with Flask's @app.route decorator
- Handle GET and POST requests
- Access request data via request.args and request.form
- Return responses and render Jinja2 templates
- Use redirect and url_for
- Run the development server

## Topics Covered

1. Flask framework overview
2. Routes with @app.route
3. HTTP methods (GET, POST)
4. Request object (request.args, request.form)
5. Response objects
6. Rendering templates with Jinja2 (brief introduction)
7. redirect and url_for
8. Running the dev server
9. Simple REST endpoints

## Prerequisites

Modules 000-085.

## Key Concepts

```python
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return '<h1>Hello, Flask!</h1>'

@app.route('/greet/<name>')
def greet(name: str) -> str:
    return f'<h1>Hello, {name}!</h1>'

@app.route('/submit', methods=['GET', 'POST'])
def submit() -> str:
    if request.method == 'POST':
        data = request.form['name']
        return redirect(url_for('greet', name=data))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Resources

- Flask documentation: https://flask.palletsprojects.com
- Flask Mega-Tutorial
- Jinja2 documentation
