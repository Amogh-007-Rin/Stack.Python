# Module 091: Concurrency: Threading

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2.5 hours

## Learning Objectives

- Understand concurrency vs parallelism
- Create and manage threads with the threading module
- Use daemon threads for background tasks
- Ensure thread safety with Lock and RLock
- Explain the GIL and its implications
- Avoid race conditions with proper synchronization
- Use queue for thread-safe communication

## Topics Covered

1. Concurrency vs parallelism
2. threading module: Thread, start, join
3. Daemon threads
4. Thread safety: Lock, RLock
5. GIL (Global Interpreter Lock)
6. Race conditions
7. queue module for thread-safe communication
8. Producer-consumer pattern

## Prerequisites

Modules 000-090.

## Key Concepts

```python
import threading
from typing import List, Thread

# Create and start threads
def worker(name: str) -> None:
    print(f"Thread {name} running")

threads: List[Thread] = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"T-{i}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()  # Wait for completion

# Thread safety with Lock
lock: threading.Lock = threading.Lock()
shared_counter: int = 0

def safe_increment() -> None:
    global shared_counter
    with lock:
        shared_counter += 1

# Thread-safe queue
from queue import Queue
q: Queue = Queue()
q.put("item")
item = q.get()
```

## Resources

- Python threading documentation
- Python queue documentation
- "Python Concurrency" chapter in Fluent Python
- GIL explained: https://realpython.com/python-gil

## Next Module

Module 092: Concurrency: Multiprocessing
