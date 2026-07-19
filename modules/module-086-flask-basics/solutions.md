# Solutions: Introduction to Web Development: Flask Basics

## Exercise 1: Hello World
```python
from flask import Flask

app: Flask = Flask(__name__)

@app.route('/')
def hello() -> str:
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 2: Dynamic Route
```python
from flask import Flask

app: Flask = Flask(__name__)

@app.route('/user/<name>')
def greet(name: str) -> str:
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 3: Query Parameters
```python
from flask import Flask, request

app: Flask = Flask(__name__)

@app.route('/search')
def search() -> str:
    q: str = request.args.get('q', '')
    if q:
        return f'<p>You searched for: {q}</p>'
    return '<p>No search term provided.</p>'

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 4: GET and POST Form
```python
from flask import Flask, request

app: Flask = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact() -> str:
    if request.method == 'POST':
        name: str = request.form.get('name', 'Unknown')
        message: str = request.form.get('message', '')
        return f'<h2>Thanks, {name}!</h2><p>Message received: {message}</p>'
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Message: <textarea name="message"></textarea><br>
            <button type="submit">Send</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 5: Redirect
```python
from flask import Flask, request, redirect, url_for

app: Flask = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact() -> str:
    if request.method == 'POST':
        name: str = request.form.get('name', 'Unknown')
        return redirect(url_for('thank_you', name=name))
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <button type="submit">Send</button>
        </form>
    '''

@app.route('/thank-you')
def thank_you() -> str:
    name: str = request.args.get('name', 'Guest')
    return f'<h2>Thank you, {name}!</h2>'

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 6: JSON Response
```python
from flask import Flask, jsonify

app: Flask = Flask(__name__)

@app.route('/api/status')
def status() -> dict:
    return jsonify({"status": "ok", "version": "1.0"})

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 7: URL Building
```python
from flask import Flask, url_for

app: Flask = Flask(__name__)

@app.route('/')
def home() -> str:
    return '<h1>Home</h1>'

@app.route('/about')
def about() -> str:
    return '<h1>About</h1>'

@app.route('/user/<name>')
def profile(name: str) -> str:
    return f'<h1>{name}\'s Profile</h1>'

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('home'))
        print(url_for('about'))
        print(url_for('profile', name='Alice'))
    app.run(debug=True)
```

## Exercise 8: Template Rendering
```python
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/items')
def items() -> str:
    item_list: list[str] = ['Apple', 'Banana', 'Cherry', 'Date']
    return render_template('items.html', items=item_list, count=len(item_list))

if __name__ == '__main__':
    app.run(debug=True)
```

```html
{# templates/items.html #}
<!DOCTYPE html>
<html>
<head><title>Items</title></head>
<body>
  <h1>Items List ({{ count }} total)</h1>
  <ul>
    {% for item in items %}
      <li>{{ item }}</li>
    {% endfor %}
  </ul>
</body>
</html>
```

## Challenge: Todo List API
```python
from flask import Flask, request, jsonify
from typing import Dict, List

app: Flask = Flask(__name__)
todos: List[Dict] = []
next_id: int = 1

@app.route('/todos', methods=['GET'])
def get_todos() -> list:
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo() -> dict:
    global next_id
    data: Dict = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Task is required"}), 400
    todo: Dict = {"id": next_id, "task": data['task'], "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id: int) -> tuple:
    todo: Dict = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"error": "Not found"}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int) -> tuple:
    global todos
    todo: Dict = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        todos = [t for t in todos if t['id'] != todo_id]
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
