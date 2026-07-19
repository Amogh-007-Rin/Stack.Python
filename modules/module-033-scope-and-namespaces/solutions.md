# Module 033: Solutions

## Exercise 1
```
10
5
```
The `x = 10` inside `func` is local and does not affect the global `x = 5`.

## Exercise 2
```python
counter = 10

def reset_counter():
    """Reset the global counter to 0."""
    global counter
    counter = 0

reset_counter()
print(counter)  # 0
```

## Exercise 3
```python
def outer():
    """Demonstrate nonlocal with a list."""
    items = []
    def inner(item):
        nonlocal items
        items.append(item)
    inner("a")
    inner("b")
    print(items)

outer()  # ['a', 'b']
```

## Exercise 4
```python
name = "Python"

def shadow():
    name = "JavaScript"
    print(f"Inside: {name}")

shadow()        # Inside: JavaScript
print(f"Outside: {name}")  # Outside: Python
```

## Exercise 5
It finds `value` in the **enclosing** scope (the `outer` function) because `inner` does not have its own `value`.

## Exercise 6
Python treats the assignment as creating a new local variable. If you try to read before assignment, you get `UnboundLocalError`.

## Exercise 7
```python
def make_counter():
    """Return a counter function that increments each call."""
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

## Exercise 8
You shadow the built-in `print` function, so calling `print(...)` will fail with a TypeError (or whatever you assigned). Avoid shadowing built-ins.

## Exercise 9
```python
PI = 3.14159

def circle_area(radius):
    """Calculate area of a circle.

    Args:
        radius: The circle's radius

    Returns:
        Area of the circle
    """
    return PI * radius ** 2

print(circle_area(5))  # 78.53975
```

## Exercise 10
```python
def level1():
    x = 1
    def level2():
        nonlocal x
        x = 2
        def level3():
            nonlocal x
            x = 3
        level3()
    level2()
    print(x)  # 3

level1()
```
