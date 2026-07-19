# Module 001: Setting Up Your Dev Environment (Python, VS Code, Terminal)

> **Phase:** 0. Orientation  |  **Estimated time:** 2 hours  |  **Milestone Project:** No

## Prerequisites
- [Module 000: Introduction to Python](../module-000-introduction-to-python/README.md) — basic context about the language

## Learning Objectives
By the end of this module, you will be able to:
- Verify Python 3.12 is installed on your system
- Navigate the filesystem using basic terminal commands (`pwd`, `ls`, `cd`)
- Open and use VS Code for editing Python files
- Run a Python script both from the terminal and from within VS Code
- Create your first `.py` file

## Why This Matters
You can't write Python without a working environment. A properly configured setup — terminal, editor, and Python interpreter — is the foundation every developer builds on. Spending time here saves hours of frustration later.

## Concept Explanation

### Installing Python 3.12

Python does not come pre-installed on all systems, or it may ship with Python 2 (macOS). You need Python 3.12 specifically.

#### Windows
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the Python 3.12 installer for Windows
3. **Important:** Check "Add Python to PATH" during installation
4. Open Command Prompt and type `python --version`

#### macOS
1. Install Homebrew from [brew.sh](https://brew.sh) if you don't have it
2. Run `brew install python@3.12`
3. Verify with `python3 --version`

#### Linux (Ubuntu/Debian)
1. Run `sudo apt update && sudo apt install python3.12`
2. Verify with `python3.12 --version`

### Terminal Basics

The terminal (also called shell or command line) is a text-based interface to your computer. You will use it constantly as a developer.

| Command | What it does | Example |
|---------|-------------|---------|
| `pwd` | Print Working Directory — shows where you are | `/home/student` |
| `ls` | List files in the current directory | `ls` |
| `cd` | Change Directory — move somewhere else | `cd Desktop` |
| `cd ..` | Go up one directory | `cd ..` |
| `mkdir` | Make a new directory | `mkdir myproject` |
| `clear` | Clear the terminal screen | `clear` |

### VS Code

VS Code is a free, lightweight code editor by Microsoft. It has excellent Python support through extensions.

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the **Python extension** by Microsoft (search Extensions panel)
3. Open a folder: File → Open Folder
4. Create a new file: File → New File → save as `hello.py`

### Running Python

There are two main ways to run Python:

**Interactive mode (REPL):**
```
$ python3
>>> print("Hello!")
Hello!
>>> exit()
```

**Script mode (run a .py file):**
```
$ python3 hello.py
Hello!
```

The REPL is great for experimenting. Script mode is for real programs.

### Your First .py File

Create a file called `hello.py` and add:

```python
print("Hello, World!")
```

Save it, then run:
```
$ python3 hello.py
Hello, World!
```

## Common Pitfalls

1. **"Python is not recognized" on Windows**: You forgot to check "Add Python to PATH". Re-run the installer and check the box.
2. **Using `python` instead of `python3` on macOS/Linux**: On these systems, `python` often points to Python 2. Always use `python3`.
3. **Typos in terminal commands**: `cd` requires a space between the command and the directory name.
4. **Forgetting to save before running**: If you edit your `.py` file but don't save, you will run the old version.
5. **Running from the wrong directory**: Use `pwd` and `ls` to confirm you are where you think you are.

## Hands-On Walkthrough

Follow along step by step:

1. Open your terminal.
2. Type `python3 --version` (or `python --version` on Windows). You should see something like `Python 3.12.x`.
3. Create a project folder:
   ```
   mkdir ~/python-intro
   cd ~/python-intro
   ```
4. Open VS Code from the terminal: `code .` (the dot means "current directory").
5. Create a new file called `hello.py` and write:
   ```python
   print("Welcome to Python 3.12!")
   ```
6. Save the file (Ctrl+S / Cmd+S).
7. Back in the terminal, run:
   ```
   python3 hello.py
   ```
8. You should see `Welcome to Python 3.12!` printed.

## Key Takeaways

- Always use Python 3 (check with `python3 --version` or `python --version`).
- `pwd` — where am I? `ls` — what's here? `cd` — take me somewhere else.
- VS Code with the Python extension is a great editor for beginners.
- Python runs in two modes: interactive REPL and script mode.
- A `.py` file is just a text file with Python code inside.
- Save your file before running it.
- Use `exit()` or Ctrl+D to leave the REPL.

## Further Reading
- [Python Beginners Guide / Download (python.org)](https://www.python.org/about/gettingstarted/)
- [VS Code Python Tutorial (code.visualstudio.com)](https://code.visualstudio.com/docs/languages/python)
- [Command Line Crash Course (learnpythonthehardway.org)](https://learnpythonthehardway.org/book/appendixa.html)

## Next Module
Let's write real code! [Module 002: Your First Python Program](../module-002-your-first-python-program/README.md) teaches the `print()` function and basic program structure.
