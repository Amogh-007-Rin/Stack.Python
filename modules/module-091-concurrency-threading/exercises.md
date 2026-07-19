# Exercises: Concurrency: Threading

## Exercise 1: Basic Threads
Create 5 threads that each print their name and sleep for a random time. Use `start` and `join`.

## Exercise 2: Daemon Thread
Create a daemon thread that prints a heartbeat message every second. Let the main thread sleep for 3 seconds, then exit.

## Exercise 3: Race Condition
Write a script where 10 threads concurrently increment a shared counter 1000 times each. Show that the result is incorrect without locking.

## Exercise 4: Thread-Safe Counter
Fix Exercise 3 using `threading.Lock`. Verify the counter reaches the expected value.

## Exercise 5: Producer-Consumer with Queue
Implement a producer that generates 10 numbers and a consumer that squares them. Use `queue.Queue` for communication.

## Exercise 6: RLock Reentrancy
Write code that demonstrates `RLock` allowing reentrant acquisition by the same thread, while `Lock` would deadlock.

## Challenge: Thread Pool
Implement a simple thread pool class that accepts a number of worker threads and a task queue. Workers pull tasks from the queue and execute them.
