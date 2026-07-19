# Module 067: Regular Expressions — Solutions

```python
import re


# 1. re.search
match = re.search(r"Python", "I love Python programming")
if match:
    print("Match found:", match.group())


# 2. re.findall
emails = re.findall(r"\w+@\w+\.\w+",
                    "Contact: alice@example.com and bob@test.org")
print("Emails:", emails)


# 3. re.sub
result = re.sub(r"cat", "dog",
                "The cat sat on the mat, and another cat joined")
print("Replaced:", result)


# 4. re.split
parts = re.split(r"[,;|]", "apple,banana;orange|grape")
print("Split:", parts)


# 5. Named groups
log_line = "2025-06-15 14:30:00 ERROR Something went wrong"
pattern = r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<level>[A-Z]+)\s+(?P<message>.+)"
m = re.match(pattern, log_line)
if m:
    print("Date:", m.group("date"))
    print("Time:", m.group("time"))
    print("Level:", m.group("level"))
    print("Message:", m.group("message"))


# 6. Compiled patterns
phone_pattern = re.compile(r"\((\d{3})\)\s\d{3}-\d{4}")
texts = ["Call (555) 123-4567 now", "Reach (555) 987-6543"]
for text in texts:
    m = phone_pattern.search(text)
    if m:
        print("Area code:", m.group(1))
```
