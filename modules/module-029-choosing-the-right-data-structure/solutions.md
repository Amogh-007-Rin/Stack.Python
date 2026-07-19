# Solutions: Choosing the Right Data Structure

## Exercise 1
```python
# Tuple — it's immutable, so the point cannot be accidentally changed
point = (3, 4)
```

## Exercise 2
```python
# Set — automatically enforces uniqueness, O(1) membership check
visitors = set()
```

## Exercise 3
```python
# Dictionary — maps name to grade, O(1) lookup by name
grades = {"Alice": "A", "Bob": "B"}
```

## Exercise 4
```python
# List — ordered, supports adding/removing at ends and middle
shopping_list = ["milk", "eggs", "bread"]
```

## Exercise 5
```python
# Set gives O(1) membership check vs O(n) for list
nums = [1, 2, 3, 2, 4, 3, 5]
seen = set()
dupes = set()
for n in nums:
    if n in seen:
        dupes.add(n)
    seen.add(n)
print(dupes)  # {2, 3}
```

## Exercise 6
```python
# Dictionary — maps word -> count
def word_freq(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq
```

## Exercise 7
```python
# List used as a queue (or use collections.deque for efficiency)
from collections import deque
printer_queue = deque()
printer_queue.append("job1")
printer_queue.append("job2")
next_job = printer_queue.popleft()
```

## Exercise 8
```python
# List: O(n) — must scan each element
# Set:  O(1) — uses hash table for direct lookup
# For 1000 items, list may scan 500 on average; set goes directly to the bucket
```

## Exercise 9
```python
# Dictionary — natural for key-value configuration
config = {
    "debug": True,
    "max_users": 100,
    "theme": "dark"
}
```

## Exercise 10
```python
# Option 1: List of lists (mutable, easy to modify)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Option 2: Tuple of tuples (immutable, safe)
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Option 3: Dict with tuple keys for sparse matrix
matrix = {(0,0): 1, (0,1): 2, (1,0): 3}
```
