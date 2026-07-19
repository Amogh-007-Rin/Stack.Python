# Solutions: Performance Optimization & Profiling

## Exercise 1: Basic Profiling
```python
import cProfile
from typing import List

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit: int) -> int:
    return sum(1 for n in range(limit) if is_prime(n))

cProfile.run('count_primes(10000)', sort='cumtime')
```

## Exercise 2: pstats Analysis
```python
import cProfile
import pstats
from typing import List

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit: int) -> int:
    return sum(1 for n in range(limit) if is_prime(n))

cProfile.run('count_primes(10000)', 'prime_stats')

p = pstats.Stats('prime_stats')
p.sort_stats('cumtime').print_stats(5)
```

## Exercise 3: timeit Benchmark
```python
import timeit
from typing import List

append_time: float = timeit.timeit(
    'lst.append(1)',
    setup='lst = []',
    number=10000,
)

concat_time: float = timeit.timeit(
    'lst = lst + [1]',
    setup='lst = []',
    number=10000,
)

print(f"list.append: {append_time / 10000:.8f}s per operation")
print(f"list + [item]: {concat_time / 10000:.8f}s per operation")
print(f"append is {concat_time / append_time:.1f}x faster")
```

## Exercise 4: List vs Set Lookup
```python
import timeit

setup: str = """
data_list = list(range(10000))
data_set = set(range(10000))
"""

list_time: float = timeit.timeit(
    '9999 in data_list',
    setup=setup,
    number=100000,
)

set_time: float = timeit.timeit(
    '9999 in data_set',
    setup=setup,
    number=100000,
)

print(f"List membership: {list_time:.4f}s")
print(f"Set membership:  {set_time:.4f}s")
print(f"Set is {list_time / set_time:.1f}x faster")
```

## Exercise 5: __slots__ Benchmark
```python
import sys
import timeit
from typing import List

setup: str = """
class Slotted:
    __slots__ = ('a', 'b', 'c', 'd', 'e')
    def __init__(self):
        self.a = self.b = self.c = self.d = self.e = 0

class Regular:
    def __init__(self):
        self.a = self.b = self.c = self.d = self.e = 0
"""

create_slotted: float = timeit.timeit(
    'Slotted()',
    setup=setup,
    number=100000,
)

create_regular: float = timeit.timeit(
    'Regular()',
    setup=setup,
    number=100000,
)

print(f"Slotted creation time:  {create_slotted:.4f}s")
print(f"Regular creation time:  {create_regular:.4f}s")
```

## Exercise 6: Algorithmic Optimization
```python
import cProfile
import random
from typing import List, Set

def find_duplicates_naive(items: List[int]) -> List[int]:
    duplicates: List[int] = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

def find_duplicates_optimized(items: List[int]) -> List[int]:
    seen: Set[int] = set()
    duplicates: Set[int] = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

data: List[int] = [random.randint(0, 1000) for _ in range(1000)]

cProfile.run('find_duplicates_naive(data)', sort='cumtime')
cProfile.run('find_duplicates_optimized(data)', sort='cumtime')
```

## Challenge: Profiling a Web Request
```python
import cProfile
import pstats
import io
from typing import Any
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/process")
def process_endpoint() -> dict:
    total: int = 0
    for i in range(100000):
        total += i ** 2
    return {"result": total}

client = TestClient(app)

# Profile
profiler = cProfile.Profile()
profiler.enable()
response = client.get("/process")
profiler.disable()

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumtime').print_stats(10)
print(stream.getvalue())
print(f"Response status: {response.status_code}")
```
