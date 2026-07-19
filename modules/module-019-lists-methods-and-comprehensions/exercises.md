# Module 019: Lists: Methods & Comprehensions — Exercises

## Exercise 1: Append vs Extend
Predict the output:
```python
a = [1, 2]
a.append([3, 4])
print(len(a))

b = [1, 2]
b.extend([3, 4])
print(len(b))
```

## Exercise 2: Shopping List Manager
Create a shopping list program:
1. Start with an empty list
2. Use a loop that shows: "1. Add item  2. Remove item  3. View list  4. Sort  5. Quit"
3. Add: ask for item and append
4. Remove: ask for item name and use `remove()`
5. View: print numbered list
6. Sort: sort the list alphabetically

## Exercise 3: List Comprehension Squares
Use a list comprehension to create a list of squares for numbers 1–20. Then filter to keep only the even squares (where the square itself is even).

## Exercise 4: Temperature Converter
Given `celsius = [0, 5, 10, 15, 20, 25, 30, 35, 40]`, use a list comprehension to convert to Fahrenheit: `f = c * 9/5 + 32`.

## Exercise 5: Word Lengths
Given `words = ["python", "is", "awesome", "and", "fun"]`, use a list comprehension to create a list of (word, length) tuples.

## Exercise 6: Unique Elements
Write a program that takes a list `[1, 2, 2, 3, 3, 3, 4, 5, 5]` and creates a new list with duplicates removed using a loop (don't use `set()`).

## Exercise 7: Sort by Last Character
Given `names = ["Alice", "Bob", "Charlie", "David", "Eve"]`, sort them by their last character using `sort()` with the `key` parameter.

## Exercise 8: Flatten a Matrix
Given `matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]`, flatten it into a single list using a nested list comprehension.
