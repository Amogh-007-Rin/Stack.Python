# Module 094: Memory Management & Garbage Collection in CPython

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2 hours

## Learning Objectives

- Understand the CPython memory model
- Explain reference counting and its role
- Use the gc module for cycle detection
- Understand generational garbage collection
- Handle circular references properly
- Use weak references with weakref module

## Topics Covered

1. CPython memory model
2. Reference counting (how it works, why it's used)
3. Garbage collection for cycles (gc module)
4. Generational GC (young/old objects)
5. Memory fragmentation
6. del and __del__ methods
7. Circular references
8. Weak references (weakref module)

## Prerequisites

Modules 000-093.

## Key Concepts

```python
import gc
import sys
import weakref
from typing import Any, List

# Reference counting
obj: List[int] = [1, 2, 3]
ref_count: int = sys.getrefcount(obj)  # Always >= 2

# Garbage collection
gc.collect()  # Force collection
gc.get_threshold()  # (threshold0, threshold1, threshold2)

# Weak references
class Container:
    def __init__(self, data: str) -> None:
        self.data = data

c = Container("hello")
wr = weakref.ref(c)
print(wr().data)  # Access via weakref
del c
print(wr())  # None (object collected)
```

## Resources

- Python gc module documentation
- Python weakref documentation
- CPython memory management internals
- "Inside the Python Virtual Machine" by Obi Ike-Nwosu

## Next Module

Module 095: Advanced Decorators & Metaprogramming
