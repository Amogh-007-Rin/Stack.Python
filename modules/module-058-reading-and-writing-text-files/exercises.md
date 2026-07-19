# Module 058: Working with Files: Reading & Writing Text Files — Exercises

1. **Write a file**: Write a program that creates a file `greeting.txt` with the content "Hello, File!" and then reads it back.

2. **Line by line**: Read the file `sample.txt` line by line using a `for` loop. Strip newlines and print each line with its line number.

3. **Append mode**: Write a program that appends a timestamp to a log file `app.log` each time it runs. Read and print the full log.

4. **Context manager**: Write a function `copy_file(src, dst)` that copies a text file using `with` statements. Handle `FileNotFoundError`.

5. **Encoding**: Create a file with UTF-8 characters (e.g., "café", "résumé", "中文"). Read it back with the correct encoding. Try reading with `latin-1` and observe the difference.

6. **pathlib**: Use `pathlib.Path` to create a directory structure `data/2025/01/`, write a file `notes.txt` inside it, then recursively list all files.
