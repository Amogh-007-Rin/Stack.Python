# Quiz: Asynchronous Python: asyncio

## Question 1
What keyword is used to define a coroutine?
- A) `async`
- B) `await`
- C) `def`
- D) `coroutine`

## Question 2
What does `asyncio.run(main())` do?
- A) Defines a coroutine
- B) Creates an event loop, runs the coroutine, and closes the loop
- C) Starts a new thread
- D) Schedules a task for later

## Question 3
Which function is used to run multiple coroutines concurrently?
- A) `asyncio.run`
- B) `asyncio.create_task`
- C) `asyncio.gather`
- D) `asyncio.wait_for`

## Question 4
When is asyncio most beneficial?
- A) CPU-bound computations
- B) I/O-bound operations with many concurrent connections
- C) Memory-intensive tasks
- D) Disk encryption

## Question 5
What happens when a coroutine calls `await asyncio.sleep()`?
- A) The entire program sleeps
- B) The coroutine yields control back to the event loop
- C) A new thread is spawned
- D) The GIL is released

## Answer Key
1-A, 2-B, 3-C, 4-B, 5-B
