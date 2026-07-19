# Module 042: Solutions

## Exercise 1
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ${self.price:.2f}")

p = Product("Widget", 9.99)
p.display()
```

## Exercise 2
```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

s = Square(5)
print(f"Area: {s.area()}")
```

## Exercise 3
```python
class Empty:
    pass

obj = Empty()
obj.x = 10
obj.y = 20
print(f"x={obj.x}, y={obj.y}")
```

## Exercise 4
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

acc = BankAccount("Alice", 100)
acc.withdraw(50)
acc.withdraw(100)  # Insufficient funds!
print(acc.balance)
```

## Exercise 5
```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

s = Student("Alice")
s.add_grade(90)
s.add_grade(85)
s.add_grade(92)
print(f"{s.name}'s GPA: {s.gpa():.2f}")
```

## Exercise 6
```python
def greet(name):
    return f"Hello {name}"

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

print(greet("World"))      # function: greet("World")
p = Person("World")
print(p.greet())           # method: instance.method()
```

## Exercise 7
```python
class Item:
    count = 0

    def __init__(self, name):
        self.name = name
        Item.count += 1

items = [Item("A"), Item("B"), Item("C")]
print(f"Total items: {Item.count}")
```

## Exercise 8
```python
class Config:
    def __init__(self, host="localhost", port=8080):
        self.host = host
        self.port = port

c1 = Config()
c2 = Config("example.com", 443)
print(f"c1: {c1.host}:{c1.port}")
print(f"c2: {c2.host}:{c2.port}")
```

## Exercise 9
```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self

    def decrement(self):
        self.value -= 1
        return self

    def get_value(self):
        return self.value

c = Counter()
c.increment().increment().decrement().increment()
print(f"Final value: {c.get_value()}")  # 2
```

## Exercise 10
```python
class Person:
    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = name

    def get_name(self):
        return self._name

p = Person()
p.set_name("Alice")
print(p.get_name())
# p.set_name("")  # ValueError!
```
