# Solutions: Memory Management & Garbage Collection in CPython

## Exercise 1: Reference Counting
```python
import sys
from typing import List

obj: List[int] = [1, 2, 3]
print(f"Initial: {sys.getrefcount(obj)}")

ref1: List[int] = obj
print(f"After ref1: {sys.getrefcount(obj)}")

ref2: List[int] = obj
print(f"After ref2: {sys.getrefcount(obj)}")

del ref1
print(f"After del ref1: {sys.getrefcount(obj)}")

del ref2
print(f"After del ref2: {sys.getrefcount(obj)}")
```

## Exercise 2: Circular Reference
```python
import gc
from typing import Optional

class Parent:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.child: Optional[Child] = None

    def __del__(self) -> None:
        print(f"Parent {self.name} deleted")

class Child:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.parent: Optional[Parent] = None

    def __del__(self) -> None:
        print(f"Child {self.name} deleted")

gc.collect()
p = Parent("P1")
c = Child("C1")
p.child = c
c.parent = p

del p
del c
gc.collect()
print("GC cleaned the cycle")
```

## Exercise 3: GC Collection
```python
import gc
from typing import List

gc.collect()
count_before: int = len(gc.get_objects())

temp_objects: List[List[int]] = []
for i in range(10000):
    temp_objects.append([i] * 100)

count_during: int = len(gc.get_objects())
print(f"Before: {count_before}, During: {count_during}")

del temp_objects
collected: int = gc.collect()
print(f"Collected: {collected} objects")
count_after: int = len(gc.get_objects())
print(f"After GC: {count_after}")
```

## Exercise 4: Generational GC
```python
import gc
from typing import List, Tuple

print(f"Thresholds: {gc.get_threshold()}")
print(f"Counts: {gc.get_count()}")

temp: List[List[int]] = []
for _ in range(10000):
    temp.append([1, 2, 3])

print(f"After allocations: {gc.get_count()}")

del temp
gc.collect(0)
print(f"After gen 0 collect: {gc.get_count()}")

gc.collect(1)
print(f"After gen 1 collect: {gc.get_count()}")

gc.collect(2)
print(f"After gen 2 collect: {gc.get_count()}")
```

## Exercise 5: `__del__` Danger
```python
import gc
from typing import Optional

class Leak:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ref: Optional[Leak] = None

    def __del__(self) -> None:
        print(f"Deleting {self.name}")

a = Leak("A")
b = Leak("B")
a.ref = b
b.ref = a

del a
del b

collected: int = gc.collect()
print(f"GC collected: {collected} (0 means __del__ prevented collection)")
```

## Exercise 6: Weak References
```python
import gc
import weakref
from typing import Any

class Data:
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value

cache: weakref.WeakValueDictionary = weakref.WeakValueDictionary()

d1 = Data("user1", "Alice")
d2 = Data("user2", "Bob")

cache["user1"] = d1
cache["user2"] = d2

print(f"Cache size: {len(cache)}")
print(f"user1: {cache['user1'].value}")

del d1
gc.collect()

print(f"Cache size after del: {len(cache)}")
```

## Challenge: Memory Leak Detector
```python
import gc
from typing import Any, Dict, List, Set

class MemoryLeakDetector:
    def __init__(self) -> None:
        self.before: Set[int] = set()

    def __enter__(self) -> 'MemoryLeakDetector':
        gc.collect()
        self.before = {id(o) for o in gc.get_objects()}
        return self

    def __exit__(self, *args: Any) -> None:
        gc.collect()
        after: List[object] = gc.get_objects()
        leaked: List[object] = [
            o for o in after if id(o) not in self.before
        ]
        if leaked:
            print(f"WARNING: {len(leaked)} objects leaked:")
            for obj in leaked[:10]:
                print(f"  {type(obj).__name__}: {repr(obj)[:50]}")

def leaky_function() -> None:
    _leaked: List[List[int]] = []
    for i in range(1000):
        _leaked.append([i] * 10)
    # Note: normally this would be a real leak

with MemoryLeakDetector() as detector:
    leaky_function()
```
