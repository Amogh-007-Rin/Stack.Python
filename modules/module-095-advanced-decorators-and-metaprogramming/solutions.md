# Solutions: Advanced Decorators & Metaprogramming

## Exercise 1: Decorator with Arguments
```python
import functools
import signal
from typing import Any, Callable

class TimeoutError(Exception):
    pass

def timeout(seconds: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            def handler(signum: int, frame: Any) -> None:
                raise TimeoutError(f"Function timed out after {seconds}s")

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator

@timeout(seconds=2)
def slow_function() -> None:
    import time
    time.sleep(5)

# slow_function()  # Would raise TimeoutError
```

## Exercise 2: Class Decorator
```python
import functools
from typing import Any, Dict, Type

def singleton(cls: Type) -> Type:
    instances: Dict[Type, object] = {}

    @functools.wraps(cls, updated=())
    def get_instance(*args: Any, **kwargs: Any) -> object:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance  # type: ignore

@singleton
class Database:
    def __init__(self) -> None:
        self.connected: bool = True

db1 = Database()
db2 = Database()
print(f"Same instance: {db1 is db2}")
```

## Exercise 3: functools.wraps
```python
import functools
from typing import Any, Callable

def log_calls(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__}(args={args}, kwargs={kwargs})")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Without wraps: __name__ would be 'wrapper'
print(f"Name: {add.__name__}")
print(f"Doc: {add.__doc__}")
print(f"Result: {add(3, 4)}")
```

## Exercise 4: Dynamic Class Creation
```python
from typing import Any

def greet(self: Any) -> str:
    return f"Hello, I'm {self.name}, age {self.age}"

Person = type('Person', (), {
    '__init__': lambda self, name, age: setattr(self, 'name', name) or setattr(self, 'age', age),
    'greet': greet,
})

p = Person("Alice", 30)
print(p.greet())
print(f"Type: {type(p).__name__}")
```

## Exercise 5: Simple Metaclass
```python
from datetime import datetime
from typing import Any, Dict, Type

class TimestampMeta(type):
    def __call__(cls: Type, *args: Any, **kwargs: Any) -> Any:
        instance = super().__call__(*args, **kwargs)
        instance.created_at = datetime.now()
        return instance

class MyClass(metaclass=TimestampMeta):
    def __init__(self, value: str) -> None:
        self.value = value

obj = MyClass("test")
print(f"Value: {obj.value}")
print(f"Created at: {obj.created_at}")
```

## Exercise 6: __slots__ Optimization
```python
import sys
from typing import List

class SlottedClass:
    __slots__ = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

    def __init__(self) -> None:
        for attr in self.__slots__:
            setattr(self, attr, 0)

class RegularClass:
    def __init__(self) -> None:
        self.a = self.b = self.c = self.d = self.e = 0
        self.f = self.g = self.h = self.i = self.j = 0

N: int = 100000
slotted_list: List[SlottedClass] = [SlottedClass() for _ in range(N)]
regular_list: List[RegularClass] = [RegularClass() for _ in range(N)]

print(f"Slotted instance size: {sys.getsizeof(slotted_list[0])} bytes")
print(f"Regular instance size: {sys.getsizeof(regular_list[0])} bytes")
```

## Challenge: ORM-like Metaclass
```python
from typing import Any, ClassVar, Dict, List, Optional, Type

class ModelMeta(type):
    def __new__(mcs: Type, name: str, bases: tuple,
               namespace: Dict[str, Any]) -> Type:
        cls = super().__new__(mcs, name, bases, namespace)
        if name != 'Model':
            cls._table: List[Dict[str, Any]] = []
            cls._fields: List[str] = [
                k for k, v in namespace.get('__annotations__', {}).items()
                if not k.startswith('_')
            ]
        return cls

class Model(metaclass=ModelMeta):
    _table: ClassVar[List[Dict[str, Any]]]
    _fields: ClassVar[List[str]]

    def __init__(self, **kwargs: Any) -> None:
        for field in self._fields:
            setattr(self, field, kwargs.get(field))

    def save(self) -> None:
        record: Dict[str, Any] = {
            field: getattr(self, field) for field in self._fields
        }
        self._table.append(record)

    @classmethod
    def all(cls: Type) -> List[Dict[str, Any]]:
        return cls._table

class Person(Model):
    name: str
    age: int

p1 = Person(name="Alice", age=30)
p1.save()
p2 = Person(name="Bob", age=25)
p2.save()

for record in Person.all():
    print(record)
```
