# Solutions: Dictionaries: Basics

## Exercise 1
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
```

## Exercise 2
```python
print(person["name"])  # Alice
print(person.get("country", "Unknown"))  # Unknown
```

## Exercise 3
```python
inventory = {}
inventory["apples"] = 5
inventory["bananas"] = 3
inventory["apples"] = 10
print(inventory)  # {'apples': 10, 'bananas': 3}
```

## Exercise 4
```python
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name in scores:
    print(name)
```

## Exercise 5
```python
for score in scores.values():
    print(score)
```

## Exercise 6
```python
for name, score in scores.items():
    print(f"{name}: {score}")
```

## Exercise 7
```python
print("Alice" in scores)    # True
print("David" in scores)    # False
```

## Exercise 8
```python
print(len(scores))  # 3
```

## Exercise 9
```python
def word_lengths(words):
    return {word: len(word) for word in words}

print(word_lengths(["hi", "hello", "python"]))
# {'hi': 2, 'hello': 5, 'python': 6}
```

## Exercise 10
```python
def char_count(text):
    counts = {}
    for ch in text:
        if ch == " ":
            continue
        counts[ch] = counts.get(ch, 0) + 1
    return counts

print(char_count("hello world"))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```
