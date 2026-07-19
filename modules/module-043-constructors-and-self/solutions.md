# Module 043: Solutions

## Exercise 1
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

b = Book("Python 101", "Alice", 2024)
print(f"{b.title} by {b.author} ({b.year})")
```

## Exercise 2
```python
class Timer:
    def __init__(self, duration=10, unit="seconds"):
        self.duration = duration
        self.unit = unit

t1 = Timer()
t2 = Timer(30)
t3 = Timer(60, "minutes")
print(f"t1: {t1.duration} {t1.unit}")
print(f"t2: {t2.duration} {t2.unit}")
print(f"t3: {t3.duration} {t3.unit}")
```

## Exercise 3
```python
class Team:
    def __init__(self, members=None):
        self.members = members if members is not None else []

t1 = Team()
t2 = Team()
t1.members.append("Alice")
print(f"t1: {t1.members}")
print(f"t2: {t2.members}")  # [] — independent!
```

## Exercise 4
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

r = Rectangle(5, 3)
print(f"Area: {r.area}")
```

## Exercise 5
```python
class Point:
    pass

p = Point()
p.x = 3
p.y = 4
print(f"({p.x}, {p.y})")
```

## Exercise 6
```python
class Example:
    def show(self):
        print(f"id(self) = {id(self)}")

e = Example()
e.show()                   # implicit self
Example.show(e)            # explicit self — same id
```

## Exercise 7
```python
class Email:
    def __init__(self, email):
        parts = email.split("@")
        self.username = parts[0]
        self.domain = parts[1] if len(parts) > 1 else None

e = Email("alice@example.com")
print(f"Username: {e.username}, Domain: {e.domain}")
```

## Exercise 8
```python
class Person:
    def __init__(self, name, age):
        if not (0 < age < 150):
            raise ValueError("Age must be between 0 and 150")
        self.name = name
        self.age = age

p = Person("Alice", 30)
# Person("Bob", 200)  # ValueError!
```

## Exercise 9
```python
class Config:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

c = Config(host="localhost", port=8080, debug=True)
print(c.host, c.port, c.debug)
```

## Exercise 10
```python
class FixedPoint:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = FixedPoint(3, 4)
# p.z = 5  # AttributeError: 'FixedPoint' object has no attribute 'z'
```
