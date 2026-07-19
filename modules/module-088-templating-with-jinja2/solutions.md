# Solutions: Templating and Simple Web Frontends (Jinja2)

## Exercise 1: Template Basics
```python
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template('hello.html', name='World')

if __name__ == '__main__':
    app.run(debug=True)
```
```html
{# templates/hello.html #}
<!DOCTYPE html>
<html>
<head><title>Hello</title></head>
<body>
  <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

## Exercise 2: Variables and Filters
```python
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/items')
def items() -> str:
    item_list: list[str] = ['apple', 'banana', 'cherry']
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True)
```
```html
{# templates/items.html #}
<!DOCTYPE html>
<html>
<head><title>Items</title></head>
<body>
  <h1>Items ({{ items|length }} total)</h1>
  <ul>
    {% for item in items %}
      <li>{{ item|capitalize }}</li>
    {% endfor %}
  </ul>
</body>
</html>
```

## Exercise 3: Conditionals
```python
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/score/<int:score>')
def score(score: int) -> str:
    return render_template('score.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
```
```html
{# templates/score.html #}
<!DOCTYPE html>
<html>
<head><title>Score</title></head>
<body>
  <h1>Score: {{ score }}</h1>
  {% if score >= 90 %}
    <p>Excellent!</p>
  {% elif score >= 70 %}
    <p>Good</p>
  {% else %}
    <p>Needs Improvement</p>
  {% endif %}
</body>
</html>
```

## Exercise 4: Loops with Table
```python
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/products')
def products() -> str:
    product_list: list[dict] = [
        {"name": "Laptop", "price": 999, "stock": 5},
        {"name": "Mouse", "price": 25, "stock": 50},
        {"name": "Keyboard", "price": 75, "stock": 3},
        {"name": "Monitor", "price": 300, "stock": 8},
    ]
    return render_template('products.html', products=product_list)

if __name__ == '__main__':
    app.run(debug=True)
```
```html
{# templates/products.html #}
<!DOCTYPE html>
<html>
<head><title>Products</title></head>
<body>
  <h1>Product Catalog</h1>
  <table border="1">
    <tr><th>Name</th><th>Price</th><th>Stock</th></tr>
    {% for product in products %}
    <tr {% if product.stock < 10 %}style="background: #ffcccc"{% endif %}>
      <td>{{ product.name }}</td>
      <td>${{ product.price }}</td>
      <td>{{ product.stock }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>
```

## Exercise 5: Template Inheritance
```html
{# templates/base.html #}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
  <nav>
    <a href="{{ url_for('home') }}">Home</a> |
    <a href="{{ url_for('about') }}">About</a>
  </nav>
  <main>
    {% block content %}{% endblock %}
  </main>
  <footer>&copy; 2024 My Site</footer>
</body>
</html>
```
```html
{# templates/home.html #}
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome to My Site</h1>
  <p>This is the home page.</p>
{% endblock %}
```
```html
{# templates/about.html #}
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
  <h1>About Us</h1>
  <p>We are learning Jinja2 templating.</p>
{% endblock %}
```
```python
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template('home.html')

@app.route('/about')
def about() -> str:
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
```

## Exercise 6: Include
```html
{# templates/_form.html #}
<form method="post">
  <label>Name: <input type="text" name="name"></label><br>
  <label>Email: <input type="email" name="email"></label><br>
  <label>Message: <textarea name="message"></textarea></label><br>
  <button type="submit">Send</button>
</form>
```
```html
{# templates/contact.html #}
{% extends "base.html" %}
{% block title %}Contact{% endblock %}
{% block content %}
  <h1>Contact Us</h1>
  {% include "_form.html" %}
{% endblock %}
```

## Exercise 7: URL Generation in Templates
```html
{# templates/base.html #}
<nav>
  <a href="{{ url_for('home') }}">Home</a> |
  <a href="{{ url_for('about') }}">About</a> |
  <a href="{{ url_for('contact') }}">Contact</a>
</nav>
```

## Exercise 8: Flask + Jinja2 Integration
```python
from flask import Flask, render_template, abort

app: Flask = Flask(__name__)

posts: list[dict] = [
    {"id": 1, "title": "First Post", "body": "Content of first post."},
    {"id": 2, "title": "Second Post", "body": "Content of second post."},
    {"id": 3, "title": "Third Post", "body": "Content of third post."},
]

@app.route('/')
def home() -> str:
    return render_template('blog_home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id: int) -> str:
    post: dict | None = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        abort(404)
    return render_template('blog_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
```

## Challenge: Product Catalog Frontend
```python
from flask import Flask, render_template, request

app: Flask = Flask(__name__)

products: list[dict] = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 24.99, "category": "Accessories"},
    {"id": 3, "name": "Keyboard", "price": 79.99, "category": "Accessories"},
    {"id": 4, "name": "Monitor", "price": 299.99, "category": "Electronics"},
    {"id": 5, "name": "Desk Lamp", "price": 39.99, "category": "Office"},
]

@app.route('/')
def home() -> str:
    search: str = request.args.get('q', '').lower()
    filtered: list[dict] = [
        p for p in products if search in p['name'].lower()
    ] if search else products
    return render_template('catalog.html', products=filtered, query=search)

@app.route('/product/<int:product_id>')
def product_detail(product_id: int) -> str:
    product: dict | None = next(
        (p for p in products if p['id'] == product_id), None
    )
    if not product:
        return "Not found", 404
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
```
```html
{# templates/base.html #}
<!DOCTYPE html>
<html>
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <title>{% block title %}Product Catalog{% endblock %}</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="{{ url_for('home') }}">Product Catalog</a>
    </div>
  </nav>
  <div class="container mt-4">
    {% block content %}{% endblock %}
  </div>
</body>
</html>
```
```html
{# templates/catalog.html #}
{% extends "base.html" %}
{% block content %}
<h1>Products</h1>
<form method="get" class="mb-3">
  <input type="text" name="q" value="{{ query }}" placeholder="Search products...">
  <button type="submit" class="btn btn-primary">Search</button>
</form>
<div class="row">
  {% for product in products %}
  <div class="col-md-4 mb-3">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ product.name }}</h5>
        <p class="card-text">${{ product.price }} - {{ product.category }}</p>
        <a href="{{ url_for('product_detail', product_id=product.id) }}" class="btn btn-sm btn-info">View</a>
      </div>
    </div>
  </div>
  {% endfor %}
</div>
{% endblock %}
```
```html
{# templates/product_detail.html #}
{% extends "base.html" %}
{% block title %}{{ product.name }}{% endblock %}
{% block content %}
<h1>{{ product.name }}</h1>
<p>Price: ${{ product.price }}</p>
<p>Category: {{ product.category }}</p>
<a href="{{ url_for('home') }}" class="btn btn-secondary">Back</a>
{% endblock %}
```
