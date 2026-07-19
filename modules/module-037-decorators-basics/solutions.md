# Module 037: Solutions

## Exercise 1
```python
from functools import wraps

def announce(func):
    """Announce when a function starts and ends."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

@announce
def work():
    print("Working...")

work()
```

## Exercise 2
```python
import time
from functools import wraps

def timer_ms(func):
    """Print execution time in milliseconds."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} took {elapsed:.2f}ms")
        return result
    return wrapper

@timer_ms
def slow():
    time.sleep(0.1)

slow()
```

## Exercise 3
```python
from functools import wraps

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@uppercase
@exclaim
def greet():
    return "hello"

print(greet())  # HELLO!
```

## Exercise 4
```python
from functools import wraps

def no_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@no_wraps
def f1():
    """Docstring"""
    pass

@with_wraps
def f2():
    """Docstring"""
    pass

print(f"Without @wraps: {f1.__name__}")  # wrapper
print(f"With @wraps: {f2.__name__}")     # f2
```

## Exercise 5
```python
from functools import wraps

def double_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double_return
def get_value():
    return 21

print(get_value())  # 42
```

## Exercise 6
```python
from functools import wraps

def positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative argument: {arg}")
        for v in kwargs.values():
            if isinstance(v, (int, float)) and v < 0:
                raise ValueError(f"Negative argument: {v}")
        return func(*args, **kwargs)
    return wrapper

@positive
def sqrt_val(x):
    return x ** 0.5

print(sqrt_val(9))  # 3.0
# sqrt_val(-1)  # ValueError
```

## Exercise 7
```python
from functools import wraps

def cache(func):
    """Cache results of function calls."""
    stored = {}
    @wraps(func)
    def wrapper(*args):
        if args in stored:
            return stored[args]
        result = func(*args)
        stored[args] = result
        return result
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(35))  # 9227465 (fast due to caching)
```

## Exercise 8
```python
from functools import wraps

def repeat(n):
    """Decorator that calls a function n times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)

say("Hello!")
```

## Exercise 9
```python
from functools import wraps

def log_to_file(filename):
    """Log function calls to a file."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, "a") as f:
                f.write(f"Calling {func.__name__}(args={args}, kwargs={kwargs})\n")
            result = func(*args, **kwargs)
            with open(filename, "a") as f:
                f.write(f"  Returned: {result}\n")
            return result
        return wrapper
    return decorator

@log_to_file("log.txt")
def add(a, b):
    return a + b

add(3, 4)
```

## Exercise 10
```
<i><b>Hello</b></i>
```
The decorator closest to the function (`@italic`) is applied first, then `@bold` wraps it. So `italic` wraps the original, then `bold` wraps that result.
