# Module 092: Concurrency: Multiprocessing

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2.5 hours

## Learning Objectives

- Create and manage processes with the multiprocessing module
- Bypass the GIL using separate processes
- Share data between processes with Value and Array
- Communicate via Queue and Pipe for IPC
- Use Pool for parallel task execution
- Decide between multiprocessing and threading

## Topics Covered

1. multiprocessing module: Process, Pool, cpu_count
2. bypassing GIL with processes
3. Shared memory: Value, Array
4. Queue and Pipe for IPC
5. Process Pool for parallel execution
6. Multiprocessing vs threading decision guide
7. Performance comparison examples

## Prerequisites

Modules 000-091.

## Key Concepts

```python
from multiprocessing import Process, Pool, cpu_count, Value, Array, Queue
from typing import List

# Basic process
def worker(name: str) -> None:
    print(f"Process {name} running")

p = Process(target=worker, args=("P-1",))
p.start()
p.join()

# Process Pool
def square(n: int) -> int:
    return n * n

with Pool(processes=cpu_count()) as pool:
    results: List[int] = pool.map(square, range(10))

# Shared memory
counter = Value('i', 0)
arr = Array('d', [1.0, 2.0, 3.0])
```

## Resources

- Python multiprocessing documentation
- "Effective Python" concurrency items
- Python's multiprocessing guide: https://docs.python.org/3/library/multiprocessing.html

## Next Module

Module 093: Asynchronous Python: asyncio
