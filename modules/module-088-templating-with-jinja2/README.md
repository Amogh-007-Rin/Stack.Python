# Module 088: Templating and Simple Web Frontends (Jinja2)

- **Phase:** 9. Databases & Web Apps
- **Duration:** 2 hours

## Learning Objectives

- Write Jinja2 templates with {{ }}, {% %}, and {# #} syntax
- Use template inheritance with extends, block, and include
- Apply variables, filters, loops, and conditionals in templates
- Integrate Jinja2 with Flask using render_template
- Build a simple web frontend

## Topics Covered

1. Jinja2 template syntax ({{ }}, {% %}, {# #})
2. Template inheritance: extends, block, include
3. Variables and filters
4. Loops and conditionals in templates
5. Flask integration with render_template
6. Creating a simple web frontend

## Prerequisites

Modules 000-087.

## Key Concepts

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template('base.html', title='Home')

@app.route('/items')
def items() -> str:
    item_list = ['Apple', 'Banana', 'Cherry']
    return render_template('items.html', items=item_list, count=len(item_list))
```

```html
{# templates/base.html #}
<!DOCTYPE html>
<html>
<head><title>{% block title %}My Site{% endblock %}</title></head>
<body>
  {% include 'nav.html' %}
  {% block content %}{% endblock %}
</body>
</html>
```

## Resources

- Jinja2 documentation: https://jinja.palletsprojects.com
- Flask templating guide
- Bootstrap for styling templates
