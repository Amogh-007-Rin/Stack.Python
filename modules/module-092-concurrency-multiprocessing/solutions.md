# Solutions: Concurrency: Multiprocessing

## Exercise 1: Process Creation
```python
import multiprocessing
import os
import time
from typing import List

def worker(name: str) -> None:
    print(f"Process {name} (PID: {os.getpid()}) sleeping")
    time.sleep(2)
    print(f"Process {name} done")

processes: List[multiprocessing.Process] = [
    multiprocessing.Process(target=worker, args=(f"P-{i}",))
    for i in range(4)
]

for p in processes:
    p.start()
for p in processes:
    p.join()
```

## Exercise 2: Process Pool Map
```python
from multiprocessing import Pool, cpu_count
from typing import List

def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(1, n + 1))

numbers: List[int] = list(range(1, 101))

with Pool(processes=cpu_count()) as pool:
    results: List[int] = pool.map(sum_of_squares, numbers)

print(f"Processed {len(results)} numbers")
```

## Exercise 3: Shared Value
```python
from multiprocessing import Process, Value
from typing import List

def increment(val: Value) -> None:
    for _ in range(1000):
        val.value += 1

shared: Value = Value('i', 0)
processes: List[Process] = [
    Process(target=increment, args=(shared,))
    for _ in range(5)
]

for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Shared value: {shared.value} (expected 5000)")
```

## Exercise 4: IPC with Queue
```python
from multiprocessing import Process, Queue
from typing import List

def sender(q: Queue) -> None:
    for i in range(10):
        q.put(f"Message-{i}")
    q.put(None)

def receiver(q: Queue) -> None:
    while True:
        msg = q.get()
        if msg is None:
            break
        print(f"Received: {msg}")

q: Queue = Queue()
p1: Process = Process(target=sender, args=(q,))
p2: Process = Process(target=receiver, args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()
```

## Exercise 5: IPC with Pipe
```python
from multiprocessing import Process, Pipe
from typing import Tuple

def ping(conn) -> None:
    conn.send("ping")
    msg = conn.recv()
    print(f"Ping received: {msg}")
    conn.close()

def pong(conn) -> None:
    msg = conn.recv()
    print(f"Pong received: {msg}")
    conn.send("pong")
    conn.close()

parent_conn, child_conn = Pipe()
p1: Process = Process(target=ping, args=(parent_conn,))
p2: Process = Process(target=pong, args=(child_conn,))

p1.start()
p2.start()
p1.join()
p2.join()
```

## Exercise 6: CPU-Bound Speedup
```python
import threading
import multiprocessing
import time
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

LIMIT: int = 50000

# Threading
start: float = time.time()
threads: List[threading.Thread] = [
    threading.Thread(target=count_primes, args=(LIMIT,))
    for _ in range(4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Threading: {time.time() - start:.2f}s")

# Multiprocessing
start = time.time()
processes: List[multiprocessing.Process] = [
    multiprocessing.Process(target=count_primes, args=(LIMIT,))
    for _ in range(4)
]
for p in processes:
    p.start()
for p in processes:
    p.join()
print(f"Multiprocessing: {time.time() - start:.2f}s")
```

## Challenge: Parallel File Search
```python
import os
from multiprocessing import Pool, cpu_count
from typing import List, Tuple

def search_file(args: Tuple[str, str]) -> Tuple[str, int]:
    filepath, pattern = args
    count: int = 0
    try:
        with open(filepath, 'r', errors='ignore') as f:
            for line in f:
                if pattern in line:
                    count += 1
        return (filepath, count)
    except Exception:
        return (filepath, -1)

def parallel_search(directory: str, pattern: str) -> None:
    files: List[str] = [
        os.path.join(root, f)
        for root, _, filenames in os.walk(directory)
        for f in filenames
    ]

    with Pool(cpu_count()) as pool:
        results: List[Tuple[str, int]] = pool.map(
            search_file,
            [(f, pattern) for f in files]
        )

    for path, count in results:
        if count > 0:
            print(f"{path}: {count} matches")

parallel_search('.', 'import')
```
