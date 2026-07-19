# Module 041: Solutions

## Exercise 1
```python
class Car:
    pass

my_car = Car()
print(type(my_car))  # <class '__main__.Car'>
```

## Exercise 2
```python
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
```

## Exercise 3
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 30)
bob = Person("Bob", 25)
print(f"{alice.name} is {alice.age}")
print(f"{bob.name} is {bob.age}")
```

## Exercise 4
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(5, 3)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")
```

## Exercise 5
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
print(f"c1: {c1.get_count()}, c2: {c2.get_count()}")
```

## Exercise 6
```python
# A class is like a blueprint for a house.
# The blueprint defines the structure (rooms, doors, windows),
# but each actual house built from that blueprint is an object (instance).
# Different houses can have different paint colors (attribute values),
# but they all share the same basic structure defined by the blueprint.
```

## Exercise 7
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = [
    Student("Alice", "A"),
    Student("Bob", "B"),
    Student("Charlie", "A-"),
]

for s in students:
    print(s.name)
```

## Exercise 8
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

c = Circle(5)
print(f"Circumference: {c.circumference():.2f}")
```

## Exercise 9
```python
class Book:
    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.pages = pages

b1 = Book("Python 101", "Alice")
b2 = Book("Advanced Python", "Bob", 350)
print(f"{b1.title}: {b1.pages} pages")
print(f"{b2.title}: {b2.pages} pages")
```

## Exercise 10
```python
# Procedural approach:
def create_student(name, grade):
    return {"name": name, "grade": grade}

s1 = create_student("Alice", "A")

# OOP approach:
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        return f"{self.name}: {self.grade}"

s2 = Student("Alice", "A")

# The class is clearer because it bundles data with behavior (info method),
# ensures consistent structure, and can be extended with inheritance.
```
