# Module 035: Exercises

## Exercise 1: Recursive Sum
Write a recursive function `sum_n(n)` that returns the sum of numbers from 1 to n.

## Exercise 2: Recursive Power
Write a recursive function `power(base, exp)` that returns base raised to exp.

## Exercise 3: Recursive Count
Write a recursive function `count_items(lst)` that returns the number of items in a list without using `len()`.

## Exercise 4: Recursive Reverse
Write a recursive function `reverse_string(s)` that returns the reversed string.

## Exercise 5: Recursive Palindrome Check
Write a recursive function `is_palindrome(s)` that checks if a string is a palindrome.

## Exercise 6: Fibonacci with Memoization
Write a recursive Fibonacci function that uses a dictionary for memoization.

## Exercise 7: Recursive Flatten
Write a recursive function `flatten(nested_list)` that flattens a nested list one level.

## Exercise 8: Ackermann Function
Implement the Ackermann function (a classic deeply recursive function):
```
A(m, n) = n + 1                  if m == 0
A(m, n) = A(m - 1, 1)           if m > 0 and n == 0
A(m, n) = A(m - 1, A(m, n - 1)) if m > 0 and n > 0
```

## Exercise 9: Recursion Depth
Experiment: At what n does `factorial(n)` cause a RecursionError?

## Exercise 10: Iterative Fibonacci
Write a non-recursive (iterative) version of Fibonacci and compare performance with the recursive version for n=35.
