# Exercises: Asynchronous Python: asyncio

## Exercise 1: Basic Coroutine
Write a coroutine `say_hello` that takes a name and delay, waits, and prints a greeting. Run it with `asyncio.run`.

## Exercise 2: Gather Multiple Tasks
Create 5 coroutines that each simulate fetching data (sleep for varying times). Use `asyncio.gather` to run them concurrently.

## Exercise 3: Async Web Fetcher
Use `aiohttp` to fetch the status code of 5 different URLs concurrently.

## Exercise 4: Sequential vs Async Timing
Create 10 I/O-bound tasks. Run them sequentially (with `time.sleep`) and concurrently (with `asyncio.sleep`). Compare the total time.

## Exercise 5: Task Cancellation
Create a long-running coroutine and cancel it after a timeout using `asyncio.wait_for`.

## Exercise 6: Custom Awaitable
Create a class that implements `__await__` to be awaitable. Use it in an async function.

## Challenge: Async Rate-Limited Scraper
Build an async web scraper that fetches 20 URLs but limits concurrency to 5 simultaneous requests using `asyncio.Semaphore`.
