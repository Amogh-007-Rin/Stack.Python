# Module 007: Strings Deep Dive (Indexing, Slicing, Methods)

> **Phase:** 1. Fundamentals  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 006: Operators](../module-006-operators/README.md)

## Learning Objectives
By the end of this module, you will be able to:
- Access individual characters using positive and negative indices
- Extract substrings with the slicing syntax `[start:stop:step]`
- Use common string methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.count()`
- Measure string length with `len()`
- Explain why strings are immutable and what that means for your code
- Use escape sequences and multi-line strings

## Why This Matters
Text processing is one of the most common tasks in programming — parsing files, cleaning user input, generating reports, and working with APIs all rely on string manipulation. If you can wield slicing and string methods fluently, you can handle almost any text-based task.

## Concept Explanation

### String Indexing

Each character in a string has a position (index). Python uses **zero-based indexing**:

```
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
Neg:    -6 -5 -4 -3 -2 -1
```

```python
word = "Python"
print(word[0])   # P
print(word[3])   # h
print(word[5])   # n
print(word[-1])  # n (last character)
print(word[-3])  # h (third from end)
```

Attempting an index outside the range raises `IndexError`.

### Slicing

Slicing extracts a substring: `string[start:stop:step]`

- `start` — inclusive index to begin
- `stop` — exclusive index to end
- `step` — how many characters to skip (default 1)

```python
text = "Hello, World!"

print(text[0:5])     # Hello (indices 0-4)
print(text[7:12])    # World (indices 7-11)
print(text[:5])      # Hello (start defaults to 0)
print(text[7:])      # World! (stop defaults to end)
print(text[:])       # Hello, World! (full copy)
```

With step:
```python
print(text[::2])     # Hlo ol! (every 2nd char)
print(text[1:10:3])  # eoW  (indices 1,4,7)
print(text[::-1])    # !dlroW ,olleH (reverse)
```

Negative step reverses direction:
```python
print(text[5:0:-1])  # ,olle (from index 5 down to 1)
```

### len() Function

`len()` returns the number of characters in a string:

```python
print(len("Python"))    # 6
print(len(""))          # 0
print(len("Hello\n"))   # 6 (\n is one character)
```

### Common String Methods

Strings have many built-in methods. Methods are called with `.method_name()` syntax.

```python
text = "  Hello, Python World!  "
```

**Case conversion:**
```python
print(text.upper())       # "  HELLO, PYTHON WORLD!  "
print(text.lower())       # "  hello, python world!  "
print(text.capitalize())  # "  hello, python world!  " (first char uppercase)
print(text.title())       # "  Hello, Python World!  " (each word capitalized)
```

**Whitespace removal:**
```python
print(text.strip())       # "Hello, Python World!"
print(text.lstrip())      # "Hello, Python World!  "
print(text.rstrip())      # "  Hello, Python World!"
```

**Searching:**
```python
print(text.find("Python"))    # 10 (index where "Python" starts)
print(text.find("Java"))      # -1 (not found)
print(text.count("o"))        # 3 (how many times 'o' appears)
print("Python" in text)       # True
```

**Replacement:**
```python
print(text.replace("World", "Universe"))  # "  Hello, Python Universe!  "
```

**Splitting and joining:**
```python
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

joined = "-".join(fruits)
print(joined)  # "apple-banana-cherry"
```

### String Immutability

Strings are **immutable** — once created, they cannot be changed. Methods like `.upper()` return a *new* string; the original is unchanged:

```python
name = "alice"
name.upper()
print(name)   # "alice" (original unchanged!)

name = name.upper()
print(name)   # "ALICE" (must reassign to save)
```

You cannot modify a character directly:
```python
# name[0] = "A"  # TypeError: 'str' object does not support item assignment
```

Instead, create a new string via slicing or replacement.

### Escape Sequences

An escape sequence starts with `\` and represents a special character:

| Sequence | Meaning | Example |
|----------|---------|---------|
| `\n` | Newline | `"line1\nline2"` |
| `\t` | Tab | `"col1\tcol2"` |
| `\\` | Backslash | `"path\\to\\file"` |
| `\'` | Single quote | `'It\'s nice'` |
| `\"` | Double quote | `"He said \"Hi\""` |

```python
print("Hello\nWorld")
# Output:
# Hello
# World

print("Tab\tseparated")
# Output: Tab	separated
```

### Multi-line Strings

Use triple quotes (`"""` or `'''`) for multi-line strings:

```python
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you."""
print(poem)
```

## Common Pitfalls

1. **Off-by-one errors in slicing**: `s[0:5]` includes indices 0,1,2,3,4 — 5 characters total, not including index 5.
2. **Forgetting strings are immutable**: `text.upper()` doesn't change `text`; reassign with `text = text.upper()`.
3. **Using `.find()` and checking `if result:`**: `.find()` returns `-1` for not found (which is truthy). Check `if result >= 0` or use `in` instead.
4. **Confusing `.split()` default**: `.split()` (no argument) splits on any whitespace and removes empty strings; `.split(" ")` splits on single spaces only.
5. **Forgetting that `\` needs escaping**: `print("C:\new")` prints a newline. Use raw strings: `r"C:\new"` or double backslash.

## Hands-On Walkthrough

Let's build a data cleaner that processes a messy string:

```python
# Raw data as it might come from a user or file
raw = "  John;DOE;35;New York  "

# Clean it up
clean = raw.strip()
print("After strip:", clean)

# Split on semicolons
parts = clean.split(";")
print("Parts:", parts)

# Extract and clean individual fields
first_name = parts[0].capitalize()
last_name = parts[1].capitalize()
age = parts[2]
city = parts[3]

print("Name:", first_name, last_name)
print("Age:", age)
print("City:", city)

# Use slicing for initials
initials = first_name[0] + "." + last_name[0] + "."
print("Initials:", initials)

# Reconstruct a clean formatted version
formatted = f"{last_name}, {first_name} ({age}) — {city}"
print("Formatted:", formatted)

# Word count
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print("Word count:", len(words))
print("The appears", sentence.lower().count("the"), "times")
```

Expected output:
```
After strip: John;DOE;35;New York
Parts: ['John', 'DOE', '35', 'New York']
Name: John Doe
Age: 35
City: New York
Initials: J.D.
Formatted: Doe, John (35) — New York
Word count: 9
The appears 2 times
```

## Key Takeaways

- Indexing: `s[0]` first char, `s[-1]` last char.
- Slicing: `s[start:stop:step]` — stop is exclusive.
- Negative step reverses direction; `s[::-1]` reverses the whole string.
- `len(s)` returns character count.
- Common methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.count()`.
- Strings are immutable — methods return new strings.
- Escape sequences: `\n`, `\t`, `\\`, `\'`, `\"`.
- Triple quotes for multi-line strings.
- Use `in` to check substring membership.

## Further Reading
- [String Methods (docs.python.org)](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Lexical Analysis — Escape Sequences (docs.python.org)](https://docs.python.org/3/reference/lexical_analysis.html#literals)

## Next Module
Make your strings beautiful in [Module 008: String Formatting](../module-008-string-formatting/README.md).
