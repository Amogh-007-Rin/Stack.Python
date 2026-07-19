# Module 019: Lists: Methods & Comprehensions — Solutions

## Exercise 1: Append vs Extend

```python
a = [1, 2]
a.append([3, 4])
print(len(a))  # 3 → a = [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(len(b))  # 4 → b = [1, 2, 3, 4]
```

## Exercise 2: Shopping List Manager

```python
cart = []
while True:
    print("\n1. Add item  2. Remove item  3. View list  4. Sort  5. Quit")
    choice = input("Choose: ")
    if choice == "1":
        item = input("Item: ")
        if item:
            cart.append(item)
            print(f"Added: {item}")
    elif choice == "2":
        item = input("Item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"Removed: {item}")
        else:
            print("Not found")
    elif choice == "3":
        if not cart:
            print("Cart is empty")
        else:
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")
    elif choice == "4":
        cart.sort()
        print("Sorted!")
    elif choice == "5":
        print("Bye!")
        break
```

## Exercise 3: List Comprehension Squares

```python
squares = [x ** 2 for x in range(1, 21)]
print(f"Squares: {squares}")
even_squares = [s for s in squares if s % 2 == 0]
print(f"Even squares: {even_squares}")
```

## Exercise 4: Temperature Converter

```python
celsius = [0, 5, 10, 15, 20, 25, 30, 35, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(f"°C: {celsius}")
print(f"°F: {fahrenheit}")
```

## Exercise 5: Word Lengths

```python
words = ["python", "is", "awesome", "and", "fun"]
word_lengths = [(word, len(word)) for word in words]
print(word_lengths)
```

## Exercise 6: Unique Elements

```python
original = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []
for n in original:
    if n not in unique:
        unique.append(n)
print(f"Original: {original}")
print(f"Unique: {unique}")
```

## Exercise 7: Sort by Last Character

```python
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.sort(key=lambda name: name[-1])
print(names)
```

## Exercise 8: Flatten a Matrix

```python
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
```
