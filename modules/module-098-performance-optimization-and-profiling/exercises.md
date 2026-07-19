# Exercises: Performance Optimization & Profiling

## Exercise 1: Basic Profiling
Write a function that computes prime numbers up to 10000. Profile it with `cProfile` and identify the most time-consuming part.

## Exercise 2: pstats Analysis
Take the profile from Exercise 1 and use `pstats` to sort by cumulative time. Print the top 5 functions.

## Exercise 3: timeit Benchmark
Use `timeit` to compare the speed of `list.append` vs `list = list + [item]` for building a list of 10000 items.

## Exercise 4: List vs Set Lookup
Create a list and a set of 10000 integers. Benchmark membership tests (`x in collection`) for both. Report the speed difference.

## Exercise 5: __slots__ Benchmark
Create two classes (with and without `__slots__`). Time the creation of 100000 instances and measure total memory.

## Exercise 6: Algorithmic Optimization
Write a naive O(n^2) function to find duplicates in a list. Then rewrite it as O(n) using a set. Profile both versions.

## Challenge: Profiling a Web Request
Write a FastAPI endpoint that processes a CSV file (calculating statistics). Profile the endpoint request with `cProfile` and optimize the bottleneck. Report before/after times.
