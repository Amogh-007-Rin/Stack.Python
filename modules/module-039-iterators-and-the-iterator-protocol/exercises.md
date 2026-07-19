# Module 039: Exercises

## Exercise 1: Manual Iteration
Create a list `[10, 20, 30, 40, 50]`, get an iterator, and use `next()` to print the first 3 elements.

## Exercise 2: For Loop Simulation
Write a function `manual_for(iterable, func)` that simulates a for loop using the iterator protocol.

## Exercise 3: Custom Range
Implement a class `MyRange` that works like `range()` using the iterator protocol.

## Exercise 4: Infinite Iterator
Implement a class `Counter` that counts up from 0 infinitely.

## Exercise 5: Iterable Square
Implement a class `Squares(max_n)` that yields squares from 1^2 to max_n^2.

## Exercise 6: Iterable vs Iterator
Given a tuple `(1, 2, 3)`, show that it is iterable but not an iterator.

## Exercise 7: Reusable Iterable
Create an iterable class that can be iterated multiple times (hint: return a new iterator from `__iter__`).

## Exercise 8: Fibonacci Iterator
Implement a class `Fibonacci(n)` that iterates through the first n Fibonacci numbers.

## Exercise 9: Reverse Iterator
Implement a class `Reverse(seq)` that iterates through a sequence in reverse.

## Exercise 10: Sentinel Iterator
Implement `iter()` with a sentinel value to read from a file until a specific line.
