# Module 049: Solutions

## Exercise 1
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

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

print(Circle(5).area())
print(Rectangle(3, 4).area())
```

## Exercise 2
```python
from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def play(self):
        ...

    @abstractmethod
    def stop(self):
        ...

class Audio(Media):
    def play(self):
        return "Playing audio..."

    def stop(self):
        return "Stopping audio..."

class Video(Media):
    def play(self):
        return "Playing video..."

    def stop(self):
        return "Stopping video..."

for media in [Audio(), Video()]:
    print(media.play())
    print(media.stop())
```

## Exercise 3
```python
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def required(self):
        ...

try:
    obj = Abstract()
except TypeError as e:
    print(f"Cannot instantiate ABC: {e}")

class Incomplete(Abstract):
    pass

try:
    obj = Incomplete()
except TypeError as e:
    print(f"Cannot instantiate incomplete: {e}")
```

## Exercise 4
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def role(self):
        ...

    @abstractmethod
    def calculate_pay(self):
        ...

class Manager(Employee):
    @property
    def role(self):
        return "Manager"

    def calculate_pay(self):
        return 80000

class Developer(Employee):
    @property
    def role(self):
        return "Developer"

    def calculate_pay(self):
        return 90000

for emp in [Manager(), Developer()]:
    print(f"{emp.role}: ${emp.calculate_pay()}")
```

## Exercise 5
```python
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        ...

    def info(self, message):
        self.log(f"[INFO] {message}")

    def error(self, message):
        self.log(f"[ERROR] {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

logger = ConsoleLogger()
logger.info("System started")
logger.error("Disk full")
```

## Exercise 6
```python
from abc import ABC, abstractmethod

class Iterable(ABC):
    @abstractmethod
    def __iter__(self):
        ...

Iterable.register(list)
Iterable.register(tuple)

print(f"[] is Iterable: {isinstance([], Iterable)}")
print(f"() is Iterable: {isinstance((), Iterable)}")
print(f"'' is Iterable: {isinstance('', Iterable)}")
```

## Exercise 7
```python
from collections.abc import Sequence

class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

print(f"MyList is Sequence: {isinstance(MyList([1, 2, 3]), Sequence)}")
```

## Exercise 8
```python
from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self):
        self.connected = False

    @abstractmethod
    def connect(self):
        ...

    def execute(self, sql):
        if not self.connected:
            self.connect()
        return f"Executing: {sql}"

class SQLiteDatabase(Database):
    def connect(self):
        self.connected = True
        return "Connected to SQLite"

db = SQLiteDatabase()
print(db.execute("SELECT * FROM users"))
```

## Exercise 9
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        ...

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def create_animal(animal_type, name):
    animals = {"dog": Dog, "cat": Cat}
    cls = animals.get(animal_type.lower())
    if not cls:
        raise ValueError(f"Unknown animal: {animal_type}")
    return cls(name)

a1 = create_animal("dog", "Rex")
a2 = create_animal("cat", "Luna")
print(a1.speak())
print(a2.speak())
```

## Exercise 10
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        ...

    @abstractmethod
    def refund(self, transaction_id):
        ...

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

    def refund(self, transaction_id):
        return f"Refunding transaction {transaction_id} via Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

    def refund(self, transaction_id):
        return f"Refunding transaction {transaction_id} via PayPal"

def checkout(processor, amount):
    print(processor.process_payment(amount))

checkout(CreditCardProcessor(), 100)
checkout(PayPalProcessor(), 50)
```
