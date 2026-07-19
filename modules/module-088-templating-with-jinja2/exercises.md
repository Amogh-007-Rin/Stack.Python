# Exercises: Templating and Simple Web Frontends (Jinja2)

Assume Flask with `render_template`.

## Exercise 1: Template Basics
Create a template `hello.html` that takes a `name` variable and displays "Hello, [name]!". Render it from a Flask route.

## Exercise 2: Variables and Filters
Create a template that displays a list of `items` (list of strings). Use the `length` filter to show the count. Capitalize each item with the `capitalize` filter.

## Exercise 3: Conditionals
Create a template that displays a different message based on a `score` variable: "Excellent!" if >= 90, "Good" if >= 70, "Needs Improvement" otherwise.

## Exercise 4: Loops
Create a template that renders an HTML table of products (name, price, stock). Pass a list of dicts from the route. Highlight rows where stock < 10.

## Exercise 5: Template Inheritance
Create a base template `base.html` with a navbar, a `{% block content %}`, and a footer. Extend it in `home.html` and `about.html`.

## Exercise 6: Include
Create a reusable `_form.html` partial for a contact form (name, email, message fields). Include it in multiple pages.

## Exercise 7: URL Generation in Templates
Use `url_for` inside a template to link to other pages. Create navigation links between Home, About, and Contact.

## Exercise 8: Flask + Jinja2 Integration
Build a small Flask app with:
- Home page listing blog posts (from a list of dicts)
- Individual post page using a dynamic route
- Use template inheritance throughout

## Challenge: Product Catalog Frontend
Build a product catalog web frontend:
- `GET /` — renders a page listing all products (from a hardcoded list)
- `GET /product/<id>` — renders a product detail page
- Use Bootstrap classes in templates for styling
- Add a search form on the home page that filters products by name
- Use template inheritance for consistent layout
