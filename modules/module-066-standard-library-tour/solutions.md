# Module 066: The Python Standard Library Tour — Solutions

```python
import os
import sys
from datetime import datetime, timedelta
import random


# 1. os.getcwd and os.listdir
print("CWD:", os.getcwd())
print("Contents:", os.listdir("."))


# 2. os.path operations
path = "data/config/settings.json"
print("Dirname:", os.path.dirname(path))
print("Basename:", os.path.basename(path))
print("Extension:", os.path.splitext(path)[1])
print("Exists:", os.path.exists(path))


# 3. sys.argv
if len(sys.argv) < 3:
    print("Usage: python script.py <num1> <num2>")
    sys.exit(1)
result = float(sys.argv[1]) + float(sys.argv[2])
print(f"Sum: {result}")


# 4. sys.version and sys.exit
print("Python version:", sys.version)
sys.exit(0)


# 5. datetime
now = datetime.now()
future = now + timedelta(days=7)
print("Today:", now.strftime("%Y-%m-%d"))
print("Future:", future.strftime("%Y-%m-%d"))


# 6. random sampler
items = ["apple", "banana", "cherry", "date", "elderberry",
         "fig", "grape", "honeydew", "kiwi", "lemon"]
print("Random choice:", random.choice(items))
print("Random sample (3):", random.sample(items, 3))
random.shuffle(items)
print("Shuffled:", items)
```
