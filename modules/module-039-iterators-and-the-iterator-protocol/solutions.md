# Module 039: Solutions

## Exercise 1
```python
nums = [10, 20, 30, 40, 50]
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

## Exercise 2
```python
def manual_for(iterable, func):
    """Simulate a for loop.

    Args:
        iterable: Any iterable
        func: Function to call on each item
    """
    it = iter(iterable)
    while True:
        try:
            item = next(it)
        except StopIteration:
            break
        func(item)

manual_for([1, 2, 3], print)
```

## Exercise 3
```python
class MyRange:
    """Custom range iterator."""

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.current = 0
            self.stop = start
        else:
            self.current = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

print(list(MyRange(5)))       # [0, 1, 2, 3, 4]
print(list(MyRange(2, 7)))    # [2, 3, 4, 5, 6]
```

## Exercise 4
```python
class Counter:
    """Infinite counter starting from 0."""

    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.n
        self.n += 1
        return value

c = Counter()
print([next(c) for _ in range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Exercise 5
```python
class Squares:
    """Iterate through squares up to max_n."""

    def __init__(self, max_n):
        self.n = 1
        self.max_n = max_n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max_n:
            raise StopIteration
        value = self.n ** 2
        self.n += 1
        return value

print(list(Squares(5)))  # [1, 4, 9, 16, 25]
```

## Exercise 6
```python
t = (1, 2, 3)
print(f"Tuple has __iter__: {hasattr(t, '__iter__')}")
print(f"Tuple has __next__: {hasattr(t, '__next__')}")

it = iter(t)
print(f"Iterator has __next__: {hasattr(it, '__next__')}")
```

## Exercise 7
```python
class ReusableRange:
    """A reusable iterable range."""

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return MyRange(self.n)  # returns new iterator

print(list(ReusableRange(3)))  # [0, 1, 2]
print(list(ReusableRange(3)))  # [0, 1, 2] (works again!)
```

## Exercise 8
```python
class Fibonacci:
    """Iterate through first n Fibonacci numbers."""

    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

print(list(Fibonacci(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Exercise 9
```python
class Reverse:
    """Iterate through a sequence in reverse."""

    def __init__(self, seq):
        self.seq = seq
        self.index = len(seq)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.seq[self.index]

print(list(Reverse("Python")))  # ['n', 'o', 'h', 't', 'y', 'P']
```

## Exercise 10
```python
# Using iter(callable, sentinel) pattern
with open("/tmp/test.txt", "w") as f:
    f.write("a\nb\nEND\nc\n")

with open("/tmp/test.txt") as f:
    for line in iter(lambda: f.readline().strip(), "END"):
        print(line)  # a, b
```
