# Module 098: Performance Optimization & Profiling

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2 hours

## Learning Objectives

- Profile Python code with cProfile and profile
- Analyze profiling results with pstats
- Benchmark small code snippets with timeit
- Identify and fix performance bottlenecks
- Understand algorithmic complexity (Big O)
- Use __slots__ for memory optimization
- Compare list vs array vs set performance

## Topics Covered

1. Profiling with cProfile and profile
2. pstats for analysis
3. timeit module for micro-benchmarks
4. Identifying bottlenecks
5. Algorithmic optimization (Big O)
6. Using __slots__
7. List vs array vs set performance
8. C extensions briefly (Cython, cffi)
9. PyPy as alternative interpreter

## Prerequisites

Modules 000-097.

## Key Concepts

```python
import cProfile
import pstats
import timeit
from typing import List

# Profiling
def slow_function(n: int) -> int:
    total: int = 0
    for i in range(n):
        total += i * i
    return total

cProfile.run('slow_function(1000000)', 'profile_stats')
p = pstats.Stats('profile_stats')
p.sort_stats('cumtime').print_stats(10)

# Micro-benchmarks
time: float = timeit.timeit(
    'sum(range(1000))',
    number=10000
)
print(f"Average: {time / 10000:.6f}s")
```

## Resources

- Python profiling documentation
- cProfile docs: https://docs.python.org/3/library/profile.html
- timeit docs: https://docs.python.org/3/library/timeit.html
- Cython documentation: https://cython.readthedocs.io
- PyPy: https://pypy.org

## Next Module

Module 099: Capstone Project: Full-Stack Application
