# Module 045: Solutions

## Exercise 1
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

e = Employee("Alice", 70000)
print(f"{e.name} earns ${e.get_salary()}")
```

## Exercise 2
```python
class Secret:
    def __init__(self, secret):
        self.__secret = secret

    def reveal(self):
        return self.__secret

s = Secret("my_password")
# print(s.__secret)  # AttributeError!
print(s._Secret__secret)  # works (but don't do this)
print(s.reveal())
```

## Exercise 3
```python
class Temperature:
    def __init__(self, celsius=0):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self.__celsius = value

t = Temperature(25)
print(f"{t.get_celsius()}C")
t.set_celsius(30)
print(f"{t.get_celsius()}C")
```

## Exercise 4
```python
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not (0 < age < 150):
            raise ValueError("Age must be between 0 and 150")
        self.__age = age

p = Person("Alice")
p.set_age(30)
print(f"{p.name} is {p.get_age()}")
```

## Exercise 5
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return 3.14159 * self.__radius ** 2

c = Circle(5)
print(f"Radius: {c.get_radius()}, Area: {c.get_area():.2f}")
```

## Exercise 6
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        raise ValueError("Invalid withdrawal")

acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Balance: ${acc.get_balance()}")
```

## Exercise 7
```python
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__width * self.__height

r = Rectangle(5, 3)
print(f"Area: {r.get_area()}")
```

## Exercise 8
```python
class Parent:
    def __init__(self):
        self.__value = "parent"

    def get_value(self):
        return self.__value

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "child"  # _Child__value, different from _Parent__value

c = Child()
print(c.get_value())             # parent (parent's __value)
print(c._Parent__value)          # parent
print(c._Child__value)           # child
```

## Exercise 9
```python
class Logger:
    def __init__(self):
        self.__data = {}

    def set(self, key, value):
        print(f"LOG: Setting {key} = {value!r}")
        self.__data[key] = value

    def get(self, key):
        return self.__data.get(key)

l = Logger()
l.set("name", "Alice")
l.set("age", 30)
print(l.get("name"))
```

## Exercise 10
```python
class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []

    def get_name(self):
        return self.__name

    def get_grades(self):
        return self.__grades.copy()

    def add_grade(self, grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be 0-100")
        self.__grades.append(grade)

    def average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

s = Student("Alice")
s.add_grade(90)
s.add_grade(85)
print(f"{s.get_name()}'s average: {s.average():.2f}")
```
