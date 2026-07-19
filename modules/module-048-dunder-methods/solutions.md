# Module 048: Solutions

## Exercise 1
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age})"

p = Person("Alice", 30)
print(repr(p))
print(str(p))
print(p)
```

## Exercise 2
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(f"p1 == p2: {p1 == p2}")
print(f"Unique points: {len({p1, p2, p3})}")
```

## Exercise 3
```python
class Team:
    def __init__(self, members):
        self._members = list(members)

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]

team = Team(["Alice", "Bob", "Charlie"])
print(f"Size: {len(team)}")
print(f"First: {team[0]}")
for m in team:
    print(m)
```

## Exercise 4
```python
class Team:
    def __init__(self, members):
        self._members = list(members)

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]

    def __contains__(self, member):
        return member in self._members

team = Team(["Alice", "Bob"])
print(f"Alice in team: {'Alice' in team}")
print(f"Zoe in team: {'Zoe' in team}")
```

## Exercise 5
```python
class Power:
    def __init__(self, exp):
        self.exp = exp

    def __call__(self, base):
        return base ** self.exp

square = Power(2)
cube = Power(3)
print(f"square(5): {square(5)}")
print(f"cube(5): {cube(5)}")
```

## Exercise 6
```python
class Inventory:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __bool__(self):
        return len(self._items) > 0

inv1 = Inventory()
inv2 = Inventory()
inv2.add("sword")

print(f"inv1 truthy: {bool(inv1)}")
print(f"inv2 truthy: {bool(inv2)}")
if inv2:
    print("Has items!")
```

## Exercise 7
```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies must match")
        return Money(self.amount + other.amount, self.currency)

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

m1 = Money(100, "USD")
m2 = Money(50, "USD")
m3 = m1 + m2
print(m3)
```

## Exercise 8
```python
class Config:
    def __init__(self, host="localhost", port=8080, debug=False):
        self.host = host
        self.port = port
        self.debug = debug

    def __repr__(self):
        return f"Config(host={self.host!r}, port={self.port}, debug={self.debug})"

c = Config("example.com", 443, True)
print(repr(c))
# Output: Config(host='example.com', port=443, debug=True)
```

## Exercise 9
```python
class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self._cards = [(r, s) for s in self.SUITS for r in self.RANKS]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __contains__(self, card):
        return card in self._cards

    def __repr__(self):
        return f"Deck({len(self)} cards)"

d = Deck()
print(len(d))
print(d[0])
print(("A", "Hearts") in d)
```

## Exercise 10
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

d = Date(2024, 1, 15)
print(repr(d))
print(str(d))
```
