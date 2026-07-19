# Module 038: Exercises

## Exercise 1: Simple Generator
Write a generator `odds(n)` that yields odd numbers up to n.

## Exercise 2: Generator Expression
Use a generator expression to compute the sum of squares from 1 to 100.

## Exercise 3: Manual Iteration
Create a generator `letters = (c for c in "Python")` and use `next()` to print each letter.

## Exercise 4: yield from
Write a generator `flatten(lists)` that uses `yield from` to flatten a list of lists.

## Exercise 5: Infinite Counter
Write an infinite generator `counter(start=0)` that yields consecutive integers starting from `start`.

## Exercise 6: Generator Pipeline
Chain two generators: one yields numbers, another yields their squares.

## Exercise 7: Read Large File
Write a generator `read_lines(filename)` that yields lines from a file one at a time.

## Exercise 8: Generator with send()
Write a generator that accepts values via `send()` and maintains a running average.

## Exercise 9: Generator for Primes
Write a generator `primes()` that yields prime numbers infinitely.

## Exercise 10: Compare Performance
Create a list of 1 million squares and a generator of 1 million squares. Compare memory usage with `sys.getsizeof()`.
