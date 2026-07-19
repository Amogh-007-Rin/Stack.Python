# Module 047: Solutions

## Exercise 1
```python
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Duck:
    def sound(self):
        return "Quack!"

def make_sounds(animals):
    for a in animals:
        print(a.sound())

make_sounds([Dog(), Cat(), Duck()])
```

## Exercise 2
```python
class Car:
    def drive(self):
        return "Driving on road!"

class Boat:
    def drive(self):
        return "Sailing on water!"

def travel(vehicle):
    print(vehicle.drive())

travel(Car())
travel(Boat())
```

## Exercise 3
```python
print(len("hello"))
print(len([1, 2, 3]))
print(len((1, 2, 3, 4)))
print(len({"a": 1, "b": 2}))
print(len({1, 2, 3, 4, 5}))
```

## Exercise 4
```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def print_area(shape):
    print(f"Area: {shape.area():.2f}")

print_area(Circle(5))
print_area(Square(4))
```

## Exercise 5
```python
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

c = MyCollection([10, 20, 30])
print(len(c))
print(c[1])
for item in c:
    print(item)
```

## Exercise 6
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

## Exercise 7
```python
class Printer:
    def display(self, text):
        return f"Printing: {text}"

class Screen:
    def display(self, text):
        return f"Displaying: {text}"

def show_output(device, text):
    print(device.display(text))

show_output(Printer(), "Hello")
show_output(Screen(), "Hello")
```

## Exercise 8
```python
def handle(obj):
    if isinstance(obj, str):
        return f"String: {obj.upper()}"
    elif isinstance(obj, int):
        return f"Int: {obj * 2}"
    elif isinstance(obj, list):
        return f"List: {len(obj)} items"
    else:
        return f"Unknown type: {type(obj).__name__}"

print(handle("hello"))
print(handle(42))
print(handle([1, 2, 3]))
```

## Exercise 9
```python
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

for f in Fibonacci(10):
    print(f, end=" ")
```

## Exercise 10
```python
class PDFReport:
    def generate(self, data):
        return f"PDF Report:\n{chr(10).join(f'- {k}: {v}' for k, v in data.items())}"

class CSVReport:
    def generate(self, data):
        return "CSV:\n" + ",".join(data.keys()) + "\n" + ",".join(str(v) for v in data.values())

def generate_report(report, data):
    print(report.generate(data))

data = {"name": "Alice", "score": 95}
generate_report(PDFReport(), data)
generate_report(CSVReport(), data)
```
