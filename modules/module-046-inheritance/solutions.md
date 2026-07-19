# Module 046: Solutions

## Exercise 1
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

print(Dog("Rex").speak())
print(Cat("Luna").speak())
```

## Exercise 2
```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

c = Car("Toyota", "Camry", 4)
print(f"{c.make} {c.model}, {c.doors} doors")
```

## Exercise 3
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()
print(f"d is Dog: {isinstance(d, Dog)}")
print(f"d is Animal: {isinstance(d, Animal)}")
print(f"Dog subclass Animal: {issubclass(Dog, Animal)}")
print(f"Cat subclass Dog: {issubclass(Cat, Dog)}")
```

## Exercise 4
```python
class Employee:
    def work(self):
        return "Working..."

class Manager(Employee):
    def work(self):
        parent = super().work()
        return f"Managing... ({parent})"

e = Employee()
m = Manager()
print(e.work())
print(m.work())
```

## Exercise 5
```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"d.who(): {d.who()}")
print(f"MRO: {[c.__name__ for c in D.__mro__]}")
```

## Exercise 6
```python
class ReverseList(list):
    def __getitem__(self, index):
        return super().__getitem__(len(self) - 1 - index)

rl = ReverseList([1, 2, 3, 4, 5])
print(rl[0])  # 5
print(rl[1])  # 4
print(rl[2])  # 3
```

## Exercise 7
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

s = Student("Alice", 20, "S123")
t = Teacher("Bob", 45, "T456")
print(f"{s.name}, {s.student_id}")
print(f"{t.name}, {t.employee_id}")
```

## Exercise 8
```python
class Base:
    def __init__(self):
        self.__init_internal()

    def __init_internal(self):
        self.value = "base"

    def get_value(self):
        return self.value

class Child(Base):
    def __init__(self):
        super().__init__()
        # __init_internal is mangled to _Base__init_internal
        # so defining __init_internal here won't override

c = Child()
print(c.get_value())  # base
```

## Exercise 9
```python
from datetime import datetime

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()

class Log:
    def __init__(self, message):
        self.message = message

class TimestampedLog(TimestampMixin, Log):
    pass

log = TimestampedLog("Test message")
print(f"{log.message} at {log.created_at}")
```

## Exercise 10
```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(3, 4)]
for s in shapes:
    print(f"{type(s).__name__}: {s.area():.2f}")
```
