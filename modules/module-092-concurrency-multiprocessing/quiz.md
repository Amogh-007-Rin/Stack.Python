# Quiz: Concurrency: Multiprocessing

## Question 1
What function returns the number of CPU cores?
- A) `os.cpu_count()`
- B) `multiprocessing.cpu_count()`
- C) `platform.cores()`
- D) `sys.cpu_cores()`

## Question 2
How does multiprocessing bypass the GIL?
- A) By using C extensions
- B) By creating separate processes, each with its own GIL
- C) By disabling the GIL at runtime
- D) By using JIT compilation

## Question 3
Which of the following is NOT a valid way to share data between processes?
- A) `multiprocessing.Value`
- B) `multiprocessing.Array`
- C) Global variables
- D) `multiprocessing.Queue`

## Question 4
What is the main advantage of multiprocessing over threading?
- A) Lower memory usage
- B) True parallelism for CPU-bound tasks
- C) Faster startup time
- D) Simpler code

## Question 5
Which IPC mechanism allows two-way communication between two processes?
- A) Queue
- B) Pipe
- C) Value
- D) Lock

## Answer Key
1-B, 2-B, 3-C, 4-B, 5-B
