# Module 044: Solutions

## Exercise 1
```python
class Animal:
    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

animals = [Animal("A"), Animal("B"), Animal("C"), Animal("D"), Animal("E")]
print(f"Total animals: {Animal.count}")
```

## Exercise 2
```python
class Employee:
    company = "Inc"

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")
print(f"e1: {e1.name} works at {e1.company}")
print(f"e2: {e2.name} works at {e2.company}")
```

## Exercise 3
```python
class Employee:
    company = "Inc"

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")

Employee.company = "NewCo"
print(f"After class change: e1={e1.company}, e2={e2.company}")

e1.company = "PersonalCo"  # shadows class var
print(f"After instance assign: e1={e1.company}, e2={e2.company}")
print(f"Class still: {Employee.company}")
```

## Exercise 4
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

s = Student("Alice")
s.add_grade(90)
s.add_grade(85)
print(f"{s.name}'s avg: {s.average():.2f}")
```

## Exercise 5
```python
class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

cars = [Car("Toyota", "Camry"), Car("Honda", "Accord"), Car("Ford", "Focus")]
for c in cars:
    print(f"{c.make} {c.model}: {c.wheels} wheels")
```

## Exercise 6
```python
class Team:
    members = []  # BAD: shared mutable

t1 = Team()
t2 = Team()
t1.members.append("Alice")
print(f"t1: {t1.members}, t2: {t2.members}")  # both have Alice!

# Fixed version:
class TeamFixed:
    def __init__(self):
        self.members = []

t3 = TeamFixed()
t4 = TeamFixed()
t3.members.append("Alice")
print(f"t3: {t3.members}, t4: {t4.members}")  # independent
```

## Exercise 7
```python
class Point:
    origin = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(f"Instance __dict__: {p.__dict__}")
print(f"Class __dict__ (origin): {'origin' in Point.__dict__}")
```

## Exercise 8
```python
class Database:
    host = "localhost"
    port = 5432

    def __init__(self, host=None, port=None):
        if host:
            self.host = host
        if port:
            self.port = port

db1 = Database()
db2 = Database("prod.example.com", 5433)
print(f"db1: {db1.host}:{db1.port}")
print(f"db2: {db2.host}:{db2.port}")
```

## Exercise 9
```python
class Animal:
    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

class Dog(Animal):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        Dog.count += 1

class Cat(Animal):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        Cat.count += 1

d = Dog("Rex")
c1 = Cat("Luna")
c2 = Cat("Milo")
print(f"Animals: {Animal.count}, Dogs: {Dog.count}, Cats: {Cat.count}")
```

## Exercise 10
```python
class Logger:
    def __setattr__(self, name, value):
        print(f"Setting {name} = {value!r}")
        super().__setattr__(name, value)

l = Logger()
l.x = 10
l.name = "test"
```
