# Exercises: Mutability vs Immutability

## Exercise 1: Mutable vs Immutable Identification
Classify each type as mutable or immutable: `int`, `list`, `str`, `tuple`, `dict`, `set`, `float`, `frozenset`.

## Exercise 2: Immutable Behavior
Given `a = "hello"`, try to change the first character to `"H"`. What happens? Then create a new string `"Hello"` and assign it to `a`.

## Exercise 3: Mutable Behavior
Given `lst = [1, 2, 3]`, change the first element to `99`. Print the list.

## Exercise 4: Function Argument — Immutable
Write a function `try_to_modify_int(x)` that tries to increment `x` inside the function. Call it with `n = 5` and print `n` afterward. Did `n` change?

## Exercise 5: Function Argument — Mutable
Write a function `add_element(lst, item)` that appends `item` to `lst`. Call it with `my_list = [1, 2]` and print `my_list`. Did it change?

## Exercise 6: Dict Keys
Create a dictionary with a tuple key `(1, 2)`. Then try to use a list key `[1, 2]`. Catch the error and explain.

## Exercise 7: Set Elements
Try to add a list to a set. Catch the error. Then try adding a tuple — does it work?

## Exercise 8: Reference Aliasing
Given `a = [1, 2, 3]` and `b = a`, modify `b[0] = 99`. Print `a`. Explain what happened.

## Exercise 9: Avoiding the Trap
Write a function `safe_append(lst, item)` that does NOT modify the original list — it returns a new list instead.

## Exercise 10: Tuple with Mutable Elements
Create a tuple containing a list: `t = (1, [2, 3])`. Modify the list inside the tuple. Does this work? Why or why not?
