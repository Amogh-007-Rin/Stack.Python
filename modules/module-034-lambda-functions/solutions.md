# Module 034: Solutions

## Exercise 1
```python
cube = lambda x: x ** 3
print(cube(3))  # 27
```

## Exercise 2
```python
power = lambda base, exp: base ** exp
print(power(2, 5))  # 32
```

## Exercise 3
```python
fruits = ["apple", "banana", "cherry", "date"]
fruits.sort(key=lambda s: s[-1])
print(fruits)  # ['banana', 'apple', 'date', 'cherry']
```

## Exercise 4
```python
data = [(1, 3), (2, 1), (3, 2)]
data.sort(key=lambda t: t[1])
print(data)  # [(2, 1), (3, 2), (1, 3)]
```

## Exercise 5
```python
nums = [5, 10, 15, 20]
result = list(map(lambda x: x + 10, nums))
print(result)  # [15, 20, 25, 30]
```

## Exercise 6
```python
words = ["hi", "hello", "hey", "greetings"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)  # ['hello', 'greetings']
```

## Exercise 7
```python
even_or_odd = lambda n: "even" if n % 2 == 0 else "odd"
print(even_or_odd(4))  # even
print(even_or_odd(7))  # odd
```

## Exercise 8
```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
people.sort(key=lambda p: p["age"])
print(people)  # [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
```

## Exercise 9
```python
print((lambda x: x * 10)(5))  # 50
```

## Exercise 10
```python
starts_with_a = lambda s: s.lower().startswith("a")
print(starts_with_a("apple"))  # True
print(starts_with_a("banana"))  # False
```
