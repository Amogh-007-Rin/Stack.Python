# Module 062: Context Managers and the with Statement — Quiz

1. **Which methods must a class-based context manager implement?**
   - a) `__enter__` and `__exit__`
   - b) `__enter__` and `__leave__`
   - c) `__open__` and `__close__`
   - d) `__start__` and `__stop__`

2. **What does `__exit__` receive if an exception occurs?**
   - a) Only the exception message
   - b) exc_type, exc_value, traceback
   - c) Just the exception object
   - d) Nothing — exceptions are suppressed automatically

3. **Which decorator from `contextlib` creates a generator-based context manager?**
   - a) `@contextmanager`
   - b) `@generator`
   - c) `@context`
   - d) `@with`

4. **If `__exit__` returns `True`, what happens to an exception?**
   - a) It is re-raised
   - b) It is suppressed
   - c) It is logged
   - d) It is ignored

5. **Which of the following is NOT a typical use of a context manager?**
   - a) File handling
   - b) Threading locks
   - c) Mathematical calculations
   - d) Temporarily changing environment variables

<details>
<summary>Answers</summary>
1-a, 2-b, 3-a, 4-b, 5-c
</details>
