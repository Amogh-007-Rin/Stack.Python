# Solutions: Copying Objects

## Exercise 1
```python
original = [1, 2, 3]
ref = original
copy = original.copy()

ref[0] = 99

print("original:", original)  # [99, 2, 3] — changed!
print("ref:", ref)            # [99, 2, 3] — same object
print("copy:", copy)          # [1, 2, 3] — unchanged
```

## Exercise 2
```python
nums = [10, 20, 30]
nums_copy = nums.copy()
nums_copy[0] = 99
print(nums)       # [10, 20, 30]
print(nums_copy)  # [99, 20, 30]
```

## Exercise 3
```python
d = {"a": 1, "b": 2}
d_copy = d.copy()
d_copy["a"] = 99
print(d)       # {"a": 1, "b": 2}
print(d_copy)  # {"a": 99, "b": 2}
```

## Exercise 4
```python
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99
print(nested)  # [[99, 2], [3, 4]] — changed!
# Shallow copy copies references; inner lists are shared
```

## Exercise 5
```python
import copy
lst = [1, 2, 3]
shallow = copy.copy(lst)
shallow[0] = 99
print(lst)     # [1, 2, 3]
print(shallow) # [99, 2, 3]
```

## Exercise 6
```python
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0][0] = 99
print(nested)  # [[1, 2], [3, 4]] — unchanged
print(deep)    # [[99, 2], [3, 4]]
```

## Exercise 7
```python
data = {"items": [1, 2, {"nested": True}]}
deep = copy.deepcopy(data)
deep["items"][2]["nested"] = False
print(data)  # unchanged
print(deep)
```

## Exercise 8
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
p_copy = copy.copy(p)
p_deep = copy.deepcopy(p)
# For simple objects without nested mutable attrs, both behave the same
print(p_copy.x, p_copy.y)
```

## Exercise 9
```python
# Shallow copy: when the object has no nested mutable structures,
# or when sharing inner objects is desired/acceptable.
# Faster and uses less memory.

# Deep copy: when nested mutable structures must be fully independent.
# Needed for nested lists/dicts to avoid accidental mutation.
```

## Exercise 10
```python
def get_avg(nums):
    # Use copy to avoid mutating the original
    sorted_nums = sorted(nums)  # sorted() returns a new list
    return sum(sorted_nums) / len(sorted_nums)

scores = [3, 1, 4, 1, 5]
avg = get_avg(scores)
print(scores)  # unchanged
```
