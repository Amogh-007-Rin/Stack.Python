# Exercises: Concurrency: Multiprocessing

## Exercise 1: Process Creation
Create 4 processes that each print their process ID and sleep for 2 seconds. Start all processes and join them.

## Exercise 2: Process Pool Map
Use `Pool.map` to compute the sum of squares for numbers 1 to 100. Compare with a sequential version.

## Exercise 3: Shared Value
Use `multiprocessing.Value` to share a counter between 5 processes. Each process increments it 1000 times.

## Exercise 4: IPC with Queue
Write a program where one process sends 10 messages and another receives them via `multiprocessing.Queue`.

## Exercise 5: IPC with Pipe
Implement bidirectional communication between two processes using `multiprocessing.Pipe`.

## Exercise 6: CPU-Bound Speedup
Compare threading vs multiprocessing for a CPU-heavy task (e.g., prime number calculation). Show that multiprocessing is faster.

## Challenge: Parallel File Search
Write a program that searches for a pattern in multiple files in parallel using a process pool. Return a list of matching filenames and line counts.
