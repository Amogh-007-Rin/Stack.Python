# Module 062: Context Managers and the with Statement — Exercises

1. **File context manager**: Open a file called `test.txt` using `with open(...) as f` and write three lines to it. The file should auto-close after the block.

2. **Class-based manager**: Implement a class `Timer` that measures elapsed time. `__enter__` records the start time, `__exit__` prints the elapsed time. Use it with `with Timer():` to time a short loop.

3. **Exception handling**: Create a context manager `IgnoreError` that suppresses a specific exception type (e.g., `ValueError`). Demonstrate by dividing by zero inside the block and verifying no exception propagates.

4. **contextlib.contextmanager**: Use the `@contextmanager` decorator to implement a `temporary_change` context manager that temporarily changes a variable's value and restores it after the block.

5. **Lock simulation**: Write a simple `Lock` context manager that simulates acquiring/releasing a resource. Use a boolean flag to track the lock state and prevent re-entry.

6. **Database connection mock**: Implement a `DatabaseConnection` context manager that "opens" a connection on enter and "closes" it on exit. Include a `query` method. Demonstrate with a `with` block.
