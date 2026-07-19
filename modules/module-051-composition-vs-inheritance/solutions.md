# Module 051: Composition vs Inheritance — Solutions

```python
# 1. Basic Inheritance
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


shapes: list[Shape] = [Circle(5), Rectangle(3, 4)]
for s in shapes:
    print(f"{type(s).__name__}: {s.area():.2f}")

# 2. Basic Composition
class Author:
    def __init__(self, name: str, nationality: str) -> None:
        self.name = name
        self.nationality = nationality


class Book:
    def __init__(self, title: str, year: int, author: Author) -> None:
        self.title = title
        self.year = year
        self.author = author  # composition


author = Author("George Orwell", "British")
book = Book("1984", 1949, author)
print(f"{book.title} by {book.author.name}")

# 3. University System
class Person:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


class Professor(Person):
    def __init__(self, name: str, email: str, department: str) -> None:
        super().__init__(name, email)
        self.department = department


class Student(Person):
    def __init__(self, name: str, email: str, student_id: str) -> None:
        super().__init__(name, email)
        self.student_id = student_id


class Course:
    def __init__(self, code: str, title: str, professor: Professor) -> None:
        self.code = code
        self.title = title
        self.professor = professor  # composition
        self.students: list[Student] = []  # composition

    def enroll(self, student: Student) -> None:
        self.students.append(student)


# 4. Refactor to Composition
class Engine:
    def start(self) -> str:
        return "Engine running"


class Transmission:
    def shift(self, gear: str) -> str:
        return f"Shifted to {gear}"


class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.transmission = Transmission()

    def drive(self) -> str:
        return f"{self.engine.start()} — {self.transmission.shift('D')} — Car moving"


car = Car()
print(car.drive())

# 5. UML to Code
class CPU:
    def process(self) -> str:
        return "Processing data"


class Computer:
    def __init__(self) -> None:
        self.cpu = CPU()

    def power_on(self) -> str:
        return f"Computer powered on. CPU: {self.cpu.process()}"


class Laptop(Computer):
    def __init__(self, battery_life: int) -> None:
        super().__init__()
        self.battery_life = battery_life
```
