# Module 053: Dataclasses — Solutions

```python
from dataclasses import dataclass, field
from typing import List


# 1. Basic Dataclass
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0


p1 = Product("Laptop", 999.99, 5)
p2 = Product("Mouse", 19.99)
print(p1)
print(p2)

# 2. field() with default_factory
@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)

    def add_member(self, name: str) -> None:
        self.members.append(name)


team = Team("Devs")
team.add_member("Alice")
team.add_member("Bob")
print(team)

# 3. Frozen Dataclass
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float


coord = Coordinate(51.5, -0.12)
print(coord)
try:
    coord.lat = 40.0  # type: ignore
except AttributeError as e:
    print(f"Frozen error: {e}")

# 4. Dataclass Inheritance
@dataclass
class Employee:
    name: str
    salary: float


@dataclass
class Manager(Employee):
    bonus: float = 0.0

    @property
    def total_compensation(self) -> float:
        return self.salary + self.bonus


mgr = Manager("Carol", 80000, 15000)
print(f"{mgr.name}: ${mgr.total_compensation:.2f}")

# 5. Ordered Dataclass
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int


versions = [
    Version(2, 0, 0),
    Version(1, 9, 0),
    Version(2, 0, 1),
    Version(1, 10, 0),
]
versions.sort()
for v in versions:
    print(v)
```
