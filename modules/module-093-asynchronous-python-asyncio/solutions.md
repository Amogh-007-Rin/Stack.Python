# Solutions: Asynchronous Python: asyncio

## Exercise 1: Basic Coroutine
```python
import asyncio

async def say_hello(name: str, delay: float) -> None:
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main() -> None:
    await say_hello("Alice", 1)
    await say_hello("Bob", 0.5)

asyncio.run(main())
```

## Exercise 2: Gather Multiple Tasks
```python
import asyncio
from typing import List

async def fetch_data(id: int, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Data from source {id}"

async def main() -> None:
    tasks: List[asyncio.Task] = [
        asyncio.create_task(fetch_data(i, i * 0.3))
        for i in range(1, 6)
    ]
    results: List[str] = await asyncio.gather(*tasks)
    for r in results:
        print(r)

asyncio.run(main())
```

## Exercise 3: Async Web Fetcher
```python
import asyncio
import aiohttp
from typing import List

async def fetch_status(session: aiohttp.ClientSession, url: str) -> int:
    async with session.get(url) as response:
        return response.status

async def main() -> None:
    urls: List[str] = [
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/301",
        "https://httpbin.org/status/404",
        "https://httpbin.org/status/500",
        "https://httpbin.org/status/503",
    ]
    async with aiohttp.ClientSession() as session:
        tasks: List[asyncio.Task] = [
            asyncio.create_task(fetch_status(session, url))
            for url in urls
        ]
        results: List[int] = await asyncio.gather(*tasks)
        for url, status in zip(urls, results):
            print(f"{url}: {status}")

asyncio.run(main())
```

## Exercise 4: Sequential vs Async Timing
```python
import asyncio
import time
from typing import List

def sync_task(n: int) -> None:
    time.sleep(0.5)

async def async_task(n: int) -> None:
    await asyncio.sleep(0.5)

# Sequential
start: float = time.time()
for i in range(10):
    sync_task(i)
print(f"Sequential: {time.time() - start:.2f}s")

# Async
async def run_async() -> None:
    start = time.time()
    tasks: List[asyncio.Task] = [
        asyncio.create_task(async_task(i))
        for i in range(10)
    ]
    await asyncio.gather(*tasks)
    print(f"Async: {time.time() - start:.2f}s")

asyncio.run(run_async())
```

## Exercise 5: Task Cancellation
```python
import asyncio

async def long_running() -> None:
    try:
        for i in range(100):
            await asyncio.sleep(0.5)
            print(f"Working... {i}")
    except asyncio.CancelledError:
        print("Task was cancelled!")

async def main() -> None:
    task = asyncio.create_task(long_running())
    try:
        await asyncio.wait_for(task, timeout=2.0)
    except asyncio.TimeoutError:
        print("Timeout reached, task cancelled")

asyncio.run(main())
```

## Exercise 6: Custom Awaitable
```python
import asyncio
from typing import Any, Generator

class AwaitableTimer:
    def __init__(self, delay: float) -> None:
        self.delay: float = delay

    def __await__(self) -> Generator[Any, None, None]:
        return self._wait().__await__()

    async def _wait(self) -> None:
        await asyncio.sleep(self.delay)

async def main() -> None:
    print("Waiting for custom awaitable...")
    await AwaitableTimer(1.0)
    print("Done!")

asyncio.run(main())
```

## Challenge: Async Rate-Limited Scraper
```python
import asyncio
import aiohttp
from typing import List

async def fetch(session: aiohttp.ClientSession, url: str,
                semaphore: asyncio.Semaphore) -> int:
    async with semaphore:
        async with session.get(url) as response:
            return response.status

async def main() -> None:
    urls: List[str] = [f"https://httpbin.org/delay/{i % 3 + 1}"
                       for i in range(20)]
    semaphore: asyncio.Semaphore = asyncio.Semaphore(5)

    async with aiohttp.ClientSession() as session:
        tasks: List[asyncio.Task] = [
            asyncio.create_task(fetch(session, url, semaphore))
            for url in urls
        ]
        results: List[int] = await asyncio.gather(*tasks)
        print(f"Fetched {len(results)} URLs")
        print(f"Status codes: {set(results)}")

asyncio.run(main())
```
