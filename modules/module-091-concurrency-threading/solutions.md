# Solutions: Concurrency: Threading

## Exercise 1: Basic Threads
```python
import threading
import time
import random
from typing import List

def worker(name: str) -> None:
    sleep_time: float = random.uniform(0.5, 2.0)
    time.sleep(sleep_time)
    print(f"Thread {name} slept for {sleep_time:.2f}s")

threads: List[threading.Thread] = [
    threading.Thread(target=worker, args=(f"T-{i}",))
    for i in range(5)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("All threads completed")
```

## Exercise 2: Daemon Thread
```python
import threading
import time

stop_heartbeat: bool = False

def heartbeat() -> None:
    count: int = 0
    while not stop_heartbeat:
        count += 1
        print(f"Heartbeat #{count}")
        time.sleep(1)

daemon: threading.Thread = threading.Thread(target=heartbeat, daemon=True)
daemon.start()

time.sleep(3)
stop_heartbeat = True
print("Main thread exiting")
```

## Exercise 3: Race Condition
```python
import threading
from typing import List

counter: int = 0
ITERATIONS: int = 1000
NUM_THREADS: int = 10

def increment() -> None:
    global counter
    for _ in range(ITERATIONS):
        counter += 1

threads: List[threading.Thread] = [
    threading.Thread(target=increment) for _ in range(NUM_THREADS)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected: {ITERATIONS * NUM_THREADS}, Got: {counter}")
```

## Exercise 4: Thread-Safe Counter
```python
import threading
from typing import List

counter: int = 0
lock: threading.Lock = threading.Lock()
ITERATIONS: int = 1000
NUM_THREADS: int = 10

def safe_increment() -> None:
    global counter
    for _ in range(ITERATIONS):
        with lock:
            counter += 1

threads: List[threading.Thread] = [
    threading.Thread(target=safe_increment) for _ in range(NUM_THREADS)
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Expected: {ITERATIONS * NUM_THREADS}, Got: {counter}")
```

## Exercise 5: Producer-Consumer with Queue
```python
import threading
import time
from queue import Queue
from typing import List

def producer(q: Queue) -> None:
    for i in range(10):
        q.put(i)
        time.sleep(0.1)
    q.put(None)

def consumer(q: Queue) -> None:
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Squared: {item} -> {item * item}")
        q.task_done()

q: Queue = Queue()
prod: threading.Thread = threading.Thread(target=producer, args=(q,))
cons: threading.Thread = threading.Thread(target=consumer, args=(q,))

prod.start()
cons.start()
prod.join()
cons.join()
```

## Exercise 6: RLock Reentrancy
```python
import threading

lock: threading.Lock = threading.Lock()
rlock: threading.RLock = threading.RLock()

def reentrant_with_lock() -> None:
    with lock:
        print("Lock acquired")
        with lock:  # Deadlock!
            print("This won't print")

def reentrant_with_rlock() -> None:
    with rlock:
        print("RLock acquired (outer)")
        with rlock:
            print("RLock acquired (inner)")

# Uncomment to see deadlock:
# reentrant_with_lock()

reentrant_with_rlock()
```

## Challenge: Thread Pool
```python
import threading
from queue import Queue
from typing import Any, Callable, List

class ThreadPool:
    def __init__(self, num_workers: int) -> None:
        self.tasks: Queue = Queue()
        self.workers: List[threading.Thread] = []
        self._stop: bool = False

        for _ in range(num_workers):
            t = threading.Thread(target=self._worker_loop)
            t.start()
            self.workers.append(t)

    def _worker_loop(self) -> None:
        while not self._stop:
            try:
                func, args, kwargs = self.tasks.get(timeout=1)
                func(*args, **kwargs)
                self.tasks.task_done()
            except Exception:
                if self._stop:
                    break

    def submit(self, func: Callable, *args: Any, **kwargs: Any) -> None:
        self.tasks.put((func, args, kwargs))

    def shutdown(self) -> None:
        self._stop = True
        for t in self.workers:
            t.join()

def task(n: int) -> None:
    print(f"Processing {n}")

pool = ThreadPool(3)
for i in range(10):
    pool.submit(task, i)
pool.tasks.join()
pool.shutdown()
```
