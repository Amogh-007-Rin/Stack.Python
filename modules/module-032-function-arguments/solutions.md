# Module 032: Solutions

## Exercise 1
```python
def repeat(text, times=2):
    """Return text repeated times times.

    Args:
        text: The string to repeat
        times: How many times to repeat (default 2)

    Returns:
        Repeated string
    """
    return text * times

print(repeat("Ha"))       # HaHa
print(repeat("Ha", 3))    # HaHaHa
print(repeat("Ha", times=5))  # HaHaHaHaHa
```

## Exercise 2
```python
def introduce(name, age):
    """Print an introduction.

    Args:
        name: Person's name
        age: Person's age
    """
    print(f"I'm {name} and I'm {age} years old.")

introduce(age=25, name="Bob")
```

## Exercise 3
```python
def product(*args):
    """Return the product of all arguments.

    Args:
        *args: Variable number of numeric arguments

    Returns:
        Product of all numbers
    """
    result = 1
    for n in args:
        result *= n
    return result

print(product(2, 3, 4))  # 24
print(product(5, 10))    # 50
print(product())         # 1
```

## Exercise 4
```python
def show_settings(**kwargs):
    """Print all settings as key-value pairs.

    Args:
        **kwargs: Settings as keyword arguments
    """
    for k, v in kwargs.items():
        print(f"{k} = {v}")

show_settings(theme="dark", lang="en", fontSize=14)
```

## Exercise 5
```python
def build_url(base, *paths, **params):
    """Build a URL from components.

    Args:
        base: Base URL
        *paths: URL path segments
        **params: Query parameters

    Returns:
        Constructed URL string
    """
    url = base.rstrip("/")
    for p in paths:
        url += "/" + p.strip("/")
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url += "?" + query
    return url

print(build_url("http://example.com", "api", "v1", search="python", page=1))
```

## Exercise 6
```python
def multiply(a, b, c):
    """Return product of three numbers."""
    return a * b * c

nums = [2, 3, 4]
print(multiply(*nums))  # 24
```

## Exercise 7
```python
def display(title, year, rating):
    """Print movie info."""
    print(f"{title} ({year}): {rating}/10")

movie = {"title": "Inception", "year": 2010, "rating": 8.8}
display(**movie)
```

## Exercise 8
```
['a']
['a', 'b']
```
The default `[]` is created once when the function is defined, not each call. So `items` accumulates across calls. Fix with `items=None` and create a new list inside.

## Exercise 9
Yes, it's valid. `*args` captures positional args, and `default=5` can only be used as a keyword argument. This is fine, though some prefer to put defaults before `*args` for clarity.

## Exercise 10
```python
def log_message(level, *messages, **metadata):
    """Log messages with level and metadata.

    Args:
        level: Log level (INFO, WARN, ERROR)
        *messages: One or more message strings
        **metadata: Additional key-value metadata
    """
    print(f"[{level}]", " ".join(messages))
    if metadata:
        for k, v in metadata.items():
            print(f"  {k}: {v}")

log_message("INFO", "Server started", "on port 8080", user="admin")
```
