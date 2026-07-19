# Module 093: Asynchronous Python: asyncio

- **Phase:** 10. Concurrency & Internals
- **Duration:** 2.5 hours

## Learning Objectives

- Write async code using async/await syntax
- Understand the event loop and how it drives coroutines
- Create and manage tasks with asyncio.create_task and asyncio.gather
- Recognize awaitable objects (coroutines, tasks, futures)
- Perform async I/O with aiohttp
- Decide when async helps (I/O-bound vs CPU-bound)

## Topics Covered

1. async/await syntax
2. Event loop
3. Coroutines
4. Tasks: asyncio.create_task, asyncio.gather
5. Awaitable objects
6. asyncio.sleep for cooperative yielding
7. Running async code: asyncio.run
8. aiohttp for async HTTP
9. I/O-bound vs CPU-bound decisions

## Prerequisites

Modules 000-092.

## Key Concepts

```python
import asyncio
from typing import List

async def fetch(url: str) -> str:
    await asyncio.sleep(0.1)
    return f"Data from {url}"

async def main() -> None:
    tasks: List[asyncio.Task] = [
        asyncio.create_task(fetch(f"https://api.example.com/{i}"))
        for i in range(5)
    ]
    results: List[str] = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

## Resources

- Python asyncio documentation
- aiohttp documentation
- "Using asyncio" by Caleb Hattingh (O'Reilly)

## Next Module

Module 094: Memory Management & Garbage Collection in CPython
