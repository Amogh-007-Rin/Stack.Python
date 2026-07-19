# Module 066: The Python Standard Library Tour — Exercises

1. **os.getcwd and os.listdir**: Print the current working directory and list all files/directories in it.

2. **os.path operations**: Given a path string `"data/config/settings.json"`, use `os.path` to extract: the directory name, the base filename, the extension, and whether the path exists.

3. **sys.argv**: Write a script that accepts two numbers as command-line arguments and prints their sum. Handle the case where arguments are missing.

4. **sys.version and sys.exit**: Print the Python version, then exit the script with status code 0 using `sys.exit`.

5. **datetime**: Get the current datetime, add 7 days using `timedelta`, and print both the original and future dates formatted as "YYYY-MM-DD".

6. **random sampler**: Given a list of 10 items, use `random.choice` to pick one, `random.sample` to pick 3 unique items, and `random.shuffle` to shuffle the list in place.
