# Module 007: Solutions

## Exercise 1
```python
word = "Programming"
print(word[0])      # P
print(word[-1])     # g
print(word[5])      # a
print(word[-2])     # m (second-to-last)
```

## Exercise 2
```python
text = "Hello, World!"
print(text[0:5])       # Hello
print(text[7:12])      # World
print(text[::-1])      # !dlroW ,olleH
print(text[::2])       # Hlo ol!
```

## Exercise 3
```python
word = "radar"
print(word == word[::-1])  # True (it is a palindrome)
```

## Exercise 4
```python
data = "  python;PROGRAMMING;language  "
cleaned = data.strip().lower()
parts = cleaned.split(";")
print(parts[0].capitalize())  # Python
print(parts[1].capitalize())  # Programming
print(parts[2].capitalize())  # Language
```

## Exercise 5
```python
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.count("e"))  # 3
```

## Exercise 6
It prints `hello`. `text.upper()` returns a new string but does not modify `text`. Strings are immutable. To save the result, you must reassign: `text = text.upper()`.

## Exercise 7
```python
print("She said: \"Python's great!\"")
```
Or using escape for the apostrophe:
```python
print("She said: \"Python\\'s great!\"")
```

## Exercise 8
```python
url = "https://www.example.com/blog/post-title"
protocol = url[:5]                     # https
domain = url[8:26]                     # www.example.com
path = url[26:]                        # /blog/post-title
print(protocol, domain, path)
```
