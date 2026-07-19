# Module 061: Working with JSON — Solutions

```python
import json
import os
from datetime import date


# 1. json.dumps
data = {"name": "Alice", "age": 30, "city": "New York"}
json_str = json.dumps(data)
print(json_str)


# 2. json.dump
with open("person.json", "w") as f:
    json.dump(data, f)

with open("person.json", "r") as f:
    print(f.read())


# 3. json.loads
parsed = json.loads('{"product": "Laptop", "price": 1200.50, "in_stock": true}')
print(parsed["price"])


# 4. json.load
with open("person.json", "r") as f:
    loaded = json.load(f)
loaded["age"] = 31
with open("person.json", "w") as f:
    json.dump(loaded, f)


# 5. Pretty-printing
nested = {
    "name": "Root",
    "children": [
        {"name": "Child1", "props": {"color": "red", "size": 10}},
        {"name": "Child2", "props": {"color": "blue", "size": 20}},
    ],
}
compact = json.dumps(nested)
pretty = json.dumps(nested, indent=2, sort_keys=True)
print("Compact:", compact)
print("Pretty:", pretty)


# 6. Custom serialization
class Person:
    def __init__(self, name: str, birth_date: date) -> None:
        self.name = name
        self.birth_date = birth_date


class PersonEncoder(json.JSONEncoder):
    def default(self, obj: object) -> dict:
        if isinstance(obj, Person):
            return {"name": obj.name, "birth_date": obj.birth_date.isoformat()}
        return super().default(obj)


people = [Person("Alice", date(1990, 5, 15)), Person("Bob", date(1985, 10, 3))]
print(json.dumps(people, cls=PersonEncoder, indent=2))


# Cleanup
os.remove("person.json")
```
