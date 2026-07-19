# Module 063: Modules and Imports — Exercises

1. **Import styles**: Import the `math` module using three different styles: `import math`, `from math import sqrt`, and `import math as m`. Use each to compute the square root of 16.

2. **Module guard**: Create a file `greeter.py` that defines a function `greet(name)` and includes a `if __name__ == "__main__"` block that calls `greet("World")`. Run it directly, then import it from another script.

3. **sys.path**: Print `sys.path` and add a new directory (e.g., `"/tmp/my_modules"`) to the front of the list. Verify it appears first.

4. **Custom module**: Create a module `utils.py` with functions `add(a, b)` and `multiply(a, b)`. Create a second script that imports from `utils.py` and uses both functions.

5. **Circular import avoidance**: Create two files `a.py` and `b.py` that import each other. Observe the error. Then restructure to avoid the circular dependency by moving shared code to a third module.

6. **importlib.reload**: Create a module `messages.py` with a variable `greeting = "Hello"`. Import it in a script, modify the file, and use `importlib.reload` to see the change without restarting.
