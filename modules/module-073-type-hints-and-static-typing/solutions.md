# Solutions: Type Hints and Static Typing

## Exercise 1: Basic Function Hints
```python
def add(a: int, b: int) -> int:
    return a + b
```

## Exercise 2: Optional Parameter
```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"
```

## Exercise 3: Collection Types
```python
from typing import List

def double_values(values: List[int]) -> List[int]:
    return [x * 2 for x in values]
```

## Exercise 4: Dict and Tuple
```python
from typing import Dict, List, Tuple

def sorted_by_value(data: Dict[str, int]) -> List[Tuple[str, int]]:
    return sorted(data.items(), key=lambda item: item[1])
```

## Exercise 5: Union Type
```python
from typing import Union

def parse_id(id_value: Union[int, str]) -> int:
    if isinstance(id_value, str):
        return int(id_value)
    return id_value
```

## Exercise 6: Callable
```python
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def square(n: int) -> int:
    return n * n

print(apply_twice(square, 2))  # ((2^2)^2) = 16
```

## Exercise 7: Generic Function
```python
from typing import TypeVar, List

T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

print(first([1, 2, 3]))  # 1
print(first(['a', 'b']))  # 'a'
```

## Challenge: Generic Stack Class
```python
from typing import Generic, TypeVar, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
print(stack.is_empty())  # False
```
