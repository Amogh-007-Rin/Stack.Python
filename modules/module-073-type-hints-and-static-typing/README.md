# Module 073: Type Hints and Static Typing (mypy)

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2 hours

## Learning Objectives

- Write function signatures with type hints
- Use the typing module (List, Dict, Tuple, Set, Optional, Union, Any, Callable)
- Define generic functions with TypeVar and Generic
- Run mypy for static type checking
- Understand gradual typing benefits

## Topics Covered

1. Type hint syntax for functions and variables
2. typing module types
3. Optional and Union types
4. Callable type for functions
5. TypeVar and Generic for generics
6. Running mypy
7. Gradual typing approach

## Prerequisites

Modules 000-072.

## Key Concepts

```python
from typing import List, Dict, Optional, Union, Callable, TypeVar, Generic

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"
```

**Note:** From this module forward, ALL code examples include type hints.

## Resources

- Python docs: typing module
- mypy documentation
- PEP 484 – Type Hints
