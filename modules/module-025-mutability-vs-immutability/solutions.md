# Solutions: Mutability vs Immutability

## Exercise 1
```python
# Mutable: list, dict, set
# Immutable: int, float, str, tuple, frozenset
```

## Exercise 2
```python
a = "hello"
# a[0] = "H"  # TypeError: 'str' object does not support item assignment
a = "Hello"  # Reassignment is fine — creates a new string
print(a)
```

## Exercise 3
```python
lst = [1, 2, 3]
lst[0] = 99
print(lst)  # [99, 2, 3]
```

## Exercise 4
```python
def try_to_modify_int(x):
    x += 1
    print("Inside:", x)

n = 5
try_to_modify_int(n)
print("Outside:", n)  # 5 — unchanged
```

## Exercise 5
```python
def add_element(lst, item):
    lst.append(item)

my_list = [1, 2]
add_element(my_list, 3)
print(my_list)  # [1, 2, 3] — changed!
```

## Exercise 6
```python
d = {(1, 2): "works"}  # tuple is hashable
try:
    d[[1, 2]] = "fails"  # list is unhashable
except TypeError as e:
    print(f"Error: {e}")
```

## Exercise 7
```python
s = set()
try:
    s.add([1, 2])
except TypeError as e:
    print(f"Error: {e}")
s.add((1, 2))  # works
print(s)
```

## Exercise 8
```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)  # [99, 2, 3] — a changed because b is a reference to the same list
```

## Exercise 9
```python
def safe_append(lst, item):
    return lst + [item]

original = [1, 2, 3]
new_list = safe_append(original, 4)
print(original)  # [1, 2, 3] — unchanged
print(new_list)  # [1, 2, 3, 4]
```

## Exercise 10
```python
t = (1, [2, 3])
t[1].append(4)
print(t)  # (1, [2, 3, 4]) — works! The tuple itself is immutable,
# but the list it contains is mutable. The tuple still references
# the same list object.
```
