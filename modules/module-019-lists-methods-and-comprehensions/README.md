# Module 019: Lists: Methods & Comprehensions

> **Phase:** 2. Control Flow & Data | **Estimated time:** 2 hours | **Milestone Project:** No

## Prerequisites
- [Module 018: Lists: Basics](../module-018-lists-basics/README.md)

## Learning Objectives
- Use all common list methods: `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `index`, `count`, `sort`, `reverse`, `copy`
- Write list comprehensions to create lists concisely
- Filter lists with `if` in comprehensions
- Sort lists with the `key` parameter and `reverse`

## Why This Matters
List methods give you a toolkit for manipulating data — adding, removing, searching, and reordering elements. List comprehensions are one of Python's most distinctive features: they let you create new lists from existing ones in a single, readable line. Mastering these will make your code shorter, faster, and more Pythonic.

## Concept Explanation

### List Methods

Lists are objects, and they come with built-in methods:

#### Adding Elements

```python
fruits = ["apple", "banana"]

# Append a single element to the end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Extend with elements from an iterable
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Insert at a specific position
fruits.insert(0, "apricot")
print(fruits)  # ['apricot', 'apple', 'banana', 'cherry', 'date', 'elderberry']
```

**Key difference:** `append(x)` adds `x` as a single element. `extend(iterable)` adds each element of the iterable individually:

```python
a = [1, 2, 3]
a.append([4, 5])
print(a)  # [1, 2, 3, [4, 5]]   — nested list!

b = [1, 2, 3]
b.extend([4, 5])
print(b)  # [1, 2, 3, 4, 5]     — flat list
```

#### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# Remove the first occurrence of a value
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana', 'date']

# Remove and return an element by index (default: last)
last = fruits.pop()
print(last)     # date
print(fruits)   # ['apple', 'cherry', 'banana']

first = fruits.pop(0)
print(first)    # apple
print(fruits)   # ['cherry', 'banana']

# Remove all elements
fruits.clear()
print(fruits)  # []
```

**`remove` vs `pop`:**
- `remove(value)` removes the first match by **value** — raises `ValueError` if not found
- `pop(index)` removes and returns by **index** — raises `IndexError` if index out of range

#### Finding Elements

```python
nums = [10, 20, 30, 20, 40, 20]

# Find the index of the first occurrence
print(nums.index(20))      # 1
print(nums.index(20, 2))   # 3  (search starting at index 2)

# Count occurrences
print(nums.count(20))      # 3
print(nums.count(99))      # 0
```

#### Reordering

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort in place (ascending)
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort in place (descending)
nums.sort(reverse=True)
print(nums)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Reverse in place
nums.reverse()
print(nums)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

#### Copying

```python
original = [1, 2, 3]

# Shallow copy with copy()
shallow = original.copy()

# Or with slice syntax
shallow2 = original[:]

# Modifying the copy doesn't affect the original
shallow.append(4)
print(original)  # [1, 2, 3]
print(shallow)   # [1, 2, 3, 4]
```

### Sorting with `key`

The `key` parameter lets you sort by a transformation of each element:

```python
words = ["banana", "cherry", "apple", "date"]
words.sort(key=len)
print(words)  # ['date', 'apple', 'banana', 'cherry']

# Sort by last character
words.sort(key=lambda word: word[-1])
print(words)  # ['banana', 'apple', 'date', 'cherry']
```

### List Comprehensions

A list comprehension creates a new list by applying an expression to each element:

**Syntax:** `[expression for item in iterable]`

```python
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Compare the loop version vs comprehension:

```python
# Loop version
squares = []
for x in range(10):
    squares.append(x ** 2)

# Comprehension version
squares = [x ** 2 for x in range(10)]
```

**Filtering with `if`:**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Transform and filter
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

**`if-else` in comprehensions (ternary):**

```python
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']
```

**Nested comprehensions (flattening a matrix):**

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

## Common Pitfalls

1. **Using `append` instead of `extend` (or vice versa)** — `append([4, 5])` adds a nested list; `extend([4, 5])` adds two elements. Know which one you need.

2. **Removing from a list while iterating** — This causes elements to be skipped. Create a new list with a comprehension instead:

```python
# DON'T:
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)  # Bug: skips elements

# DO:
nums = [n for n in nums if n % 2 != 0]
```

3. **Forgetting that `sort()` modifies in place and returns `None`** — `sorted_nums = nums.sort()` gives you `None`. Use `sorted(nums)` instead:

```python
nums = [3, 1, 2]
sorted_nums = nums.sort()   # ⚠️ sorted_nums is None
sorted_nums = sorted(nums)  # ✅ new sorted list
```

4. **Overly complex comprehensions** — If a comprehension spans multiple lines or has nested loops, a regular `for` loop is more readable.

5. **Confusing `copy()` with assignment** — `new = old` doesn't copy; it creates another reference to the same list. Use `copy()` or `[:]` for a true (shallow) copy.

## Hands-On Walkthrough

Let's process a list of temperatures:

```python
temps_c = [0, 15, 20, 25, 30, 35, 40]
temps_f = [c * 9/5 + 32 for c in temps_c]
print(f"°C: {temps_c}")
print(f"°F: {temps_f}")

# Filter temps above freezing (in °C)
above_freezing = [t for t in temps_c if t > 0]
print(f"Above freezing: {above_freezing}")

# Categorize
categories = ["Hot" if t >= 30 else "Warm" if t >= 20 else "Cool" for t in temps_c]
print(f"Categories: {categories}")
```

Now let's manage a shopping list:

```python
cart = ["milk", "eggs", "bread", "butter", "cheese"]
print(f"You have {len(cart)} items")

cart.append("apples")
cart.insert(0, "coffee")  # Add coffee to front

if "eggs" in cart:
    cart.remove("eggs")
    print("Removed eggs")

cart.sort()
print(f"Sorted cart: {cart}")

# Create uppercase version with comprehension
cart_upper = [item.upper() for item in cart]
print(f"Uppercase: {cart_upper}")
```

## Key Takeaways

- `append(x)` adds one element; `extend(iter)` adds multiple from an iterable
- `remove(x)` deletes by value; `pop(i)` deletes by index and returns the value
- `sort()` and `reverse()` modify the list in place and return `None`
- Use `sorted(list)` to get a new sorted list without modifying the original
- Use `copy()` or `list[:]` to create a shallow copy
- List comprehension syntax: `[expr for item in iterable if condition]`
- Comprehensions are more concise and often faster than manual `for` + `append` loops
- Keep comprehensions simple — if it's hard to read, use a regular loop

## Further Reading
- [Python docs: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python docs: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python: List Comprehensions](https://realpython.com/list-comprehension-python/)
- [Python docs: Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)

## Next Module
[Module 020: Milestone Project: To-Do List CLI App](../module-020-mini-project-todo-cli/README.md) — Build your first complete project: a command-line to-do list manager.
