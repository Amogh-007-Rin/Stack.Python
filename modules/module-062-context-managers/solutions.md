# Module 062: Context Managers and the with Statement — Solutions

```python
import time
from contextlib import contextmanager


# 1. File context manager
with open("test.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")


# 2. Class-based Timer
class Timer:
    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")


with Timer():
    total = sum(range(1000000))
    print(f"Sum: {total}")


# 3. Exception suppression
class IgnoreError:
    def __init__(self, exc_type: type) -> None:
        self.exc_type = exc_type

    def __enter__(self) -> "IgnoreError":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return exc_type is not None and issubclass(exc_type, self.exc_type)


with IgnoreError(ValueError):
    int("not_a_number")
print("No exception raised")


# 4. contextlib.contextmanager
@contextmanager
def temporary_change(obj, attr: str, new_val):
    old_val = getattr(obj, attr)
    setattr(obj, attr, new_val)
    try:
        yield
    finally:
        setattr(obj, attr, old_val)


class Config:
    debug = False


cfg = Config()
with temporary_change(cfg, "debug", True):
    print(f"Inside: debug={cfg.debug}")
print(f"Outside: debug={cfg.debug}")


# 5. Lock simulation
class Lock:
    def __init__(self) -> None:
        self._locked = False

    def __enter__(self) -> "Lock":
        if self._locked:
            raise RuntimeError("Lock already acquired")
        self._locked = True
        print("Lock acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._locked = False
        print("Lock released")


with Lock():
    print("Doing work...")


# 6. Database connection mock
class DatabaseConnection:
    def __enter__(self) -> "DatabaseConnection":
        print("Opening database connection")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        print("Closing database connection")
        self.connected = False

    def query(self, sql: str) -> str:
        if not self.connected:
            raise RuntimeError("Not connected")
        return f"Results for: {sql}"


with DatabaseConnection() as db:
    print(db.query("SELECT * FROM users"))


import os
os.remove("test.txt")
```
