# Module 017: Nested Loops and Pattern Printing — Solutions

## Exercise 1: Rectangle

```python
for i in range(4):
    for j in range(6):
        print("#", end="")
    print()
```

## Exercise 2: Right Triangle (Numbers)

```python
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()
```

## Exercise 3: Inverted Pyramid

```python
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

## Exercise 4: Multiplication Grid

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end=" ")
    print()
```

## Exercise 5: Hollow Rectangle

```python
rows = 4
cols = 8
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

## Exercise 6: Number Diamond

```python
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
```

## Exercise 7: Lower Triangular Multiplication Table

```python
for i in range(1, 13):
    for j in range(1, 13):
        if j <= i:
            print(f"{i}×{j}={i * j:2}", end="  ")
        else:
            print("        ", end="")
    print()
```
