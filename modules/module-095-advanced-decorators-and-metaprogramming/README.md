# Module 095: Advanced Decorators & Metaprogramming

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2 hours

## Learning Objectives

- Write decorators that accept arguments
- Create class decorators
- Use functools.wraps correctly
- Dynamically create classes with type()
- Understand metaclasses and when to use them
- Use __slots__ for memory optimization

## Topics Covered

1. Decorators with arguments (@decorator(args))
2. Class decorators
3. functools.wraps in depth
4. type() for dynamic class creation
5. Metaclasses (type as metaclass)
6. __new__ vs __init__
7. When metaclasses are/aren't needed
8. __slots__ for memory optimization

## Prerequisites

Modules 000-094.

## Key Concepts

```python
import functools
from typing import Any, Callable, Type, Dict

# Decorator with arguments
def repeat(n: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Metaclass
class Meta(type):
    def __new__(mcs: Type, name: str, bases: tuple, namespace: Dict[str, Any]) -> Type:
        namespace['version'] = 1
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=Meta):
    pass

# __slots__
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
```

## Resources

- Python datamodel documentation
- "Fluent Python" Metaclasses chapter
- Raymond Hettinger's PyCon talk on descriptors
- Python __slots__ documentation

## Next Module

Module 096: Introduction to Machine Learning with Python
