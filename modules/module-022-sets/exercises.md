# Exercises: Sets

## Exercise 1: Creating Sets
Create a set called `fruits` containing `"apple"`, `"banana"`, `"cherry"`. Then create another set from the list `["a", "b", "c", "a", "b"]` and observe what happens to duplicates.

## Exercise 2: Set Methods
Start with `s = {1, 2, 3}`. Perform and print the result of each step:
- Add `4`
- Remove `2` (use both `remove` and `discard`)
- Try to remove `99` with `discard` (should not error)
- Try to remove `99` with `remove` (catch the error)
- Pop an element and print it
- Copy the set

## Exercise 3: Union
Given `A = {1, 2, 3, 4}` and `B = {3, 4, 5, 6}`, compute and print their union using both the `|` operator and the `.union()` method.

## Exercise 4: Intersection
Using the same sets from exercise 3, find elements common to both `A` and `B` using `&` and `.intersection()`.

## Exercise 5: Difference
Using `A` and `B`, find:
- Elements in `A` but not in `B` (using `-`)
- Elements in `B` but not in `A`

## Exercise 6: Symmetric Difference
Find elements in either `A` or `B` but not both, using both `^` and `.symmetric_difference()`.

## Exercise 7: Set Comprehension
Create a set of squares for numbers 0–9 that are even: `{0, 4, 16, 36, 64}` using a set comprehension.

## Exercise 8: Frozenset
Create a frozenset from `[1, 2, 3, 2, 1]`. Try to add an element to it and catch the resulting error. Then use the frozenset as a dictionary key.

## Exercise 9: Removing Duplicates
Given `names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]`, use a set to get unique names. Then convert back to a sorted list.

## Exercise 10: Set Membership
Generate 100 random integers between 1 and 20. Use a set to determine how many unique numbers were generated, and list which numbers from 1–20 never appeared.
