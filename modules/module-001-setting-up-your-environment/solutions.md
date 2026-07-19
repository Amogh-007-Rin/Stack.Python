# Module 001: Solutions

## Exercise 1
```python
import sys
print(sys.version)
```

## Exercise 2
```python
import subprocess
import os

# Simulating pwd
print("pwd output:", os.getcwd())

# Simulating ls
print("ls output:", os.listdir("."))

# Simulating cd ..
os.chdir("..")
print("After cd .., pwd:", os.getcwd())
```

## Exercise 3
```python
print("Alice")
print("Blue")
print("I want to learn data science with Python")
```

## Exercise 4
File `about_me.py`:
```python
print("My name is Bob.")
print("I love Python!")
```
Terminal command to run it:
```
python3 about_me.py
```

## Exercise 5
In the **REPL** (`python3`), you type commands one at a time and see results immediately. It's good for experimenting. In **script mode** (`python3 myfile.py`), the entire file is run as a program. Script mode is how you build real applications.

## Exercise 6
```bash
cd ..
ls
cd python_course
```

## Exercise 7
The **Python extension** by Microsoft.
