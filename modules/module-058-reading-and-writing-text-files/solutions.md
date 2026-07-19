# Module 058: Working with Files: Reading & Writing Text Files — Solutions

```python
import os
from pathlib import Path
from datetime import datetime


# 1. Write and read a file
with open("greeting.txt", "w", encoding="utf-8") as f:
    f.write("Hello, File!")

with open("greeting.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# 2. Line by line
with open("sample.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"{line_num}: {line.rstrip()}")

# 3. Append mode
with open("app.log", "a", encoding="utf-8") as f:
    f.write(f"Log entry at {datetime.now()}\n")

with open("app.log", "r", encoding="utf-8") as f:
    print(f.read())

# 4. Copy file with error handling
def copy_file(src: str, dst: str) -> str:
    try:
        with open(src, "r", encoding="utf-8") as f_in:
            content = f_in.read()
        with open(dst, "w", encoding="utf-8") as f_out:
            f_out.write(content)
        return f"Copied {src} to {dst}"
    except FileNotFoundError:
        return f"Source file {src} not found"


print(copy_file("greeting.txt", "greeting_copy.txt"))
print(copy_file("nonexistent.txt", "copy.txt"))

# 5. UTF-8 encoding
with open("unicode.txt", "w", encoding="utf-8") as f:
    f.write("café\nrésumé\n中文\n")

with open("unicode.txt", "r", encoding="utf-8") as f:
    print("UTF-8:", f.read())

try:
    with open("unicode.txt", "r", encoding="latin-1") as f:
        print("Latin-1:", f.read())
except UnicodeDecodeError as e:
    print(f"Latin-1 decode error: {e}")

# 6. pathlib directory creation
data_path = Path("data") / "2025" / "01"
data_path.mkdir(parents=True, exist_ok=True)
note_file = data_path / "notes.txt"
note_file.write_text("pathlib is powerful!", encoding="utf-8")

for p in Path("data").rglob("*"):
    print(p)

# Cleanup
os.remove("greeting.txt")
os.remove("greeting_copy.txt")
os.remove("app.log")
os.remove("unicode.txt")
import shutil
shutil.rmtree("data")
```
