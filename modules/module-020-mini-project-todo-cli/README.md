# Module 020: Milestone Project: To-Do List CLI App

> **Phase:** 2. Control Flow & Data | **Estimated time:** 3 hours | **Milestone Project:** **Yes**

## Prerequisites
- [Module 019: Lists: Methods & Comprehensions](../module-019-lists-methods-and-comprehensions/README.md)

## Learning Objectives
- Build a complete CLI application from scratch
- Design a menu-driven interface with a `while` loop
- Manage data using lists and related structures
- Implement CRUD operations (Create, Read, Update, Delete)
- Apply all concepts from Modules 001-019

## Why This Matters
This milestone project brings together everything you've learned so far: variables, conditionals, loops, lists, string formatting, and user input. Building a real tool — even a simple one — is the best way to solidify your skills. You'll also learn how to structure a program, handle edge cases, and think like a developer.

## Concept Explanation

### Project Overview

You'll build a **To-Do List CLI App** that runs in the terminal. The app will let users:

- View all tasks
- Add a new task
- Mark a task as complete
- Delete a task
- Quit the app

### Data Design

Since we haven't learned dictionaries yet (Module 023), we'll use two parallel lists:

```python
tasks = []           # list of task descriptions (strings)
completed = []       # list of booleans tracking completion
```

When the user adds "Buy milk", we append to both lists:
- `tasks` → `["Buy milk"]`
- `completed` → `[False]`

### Menu Structure

```python
while True:
    print("\n===== TO-DO LIST =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark complete")
    print("4. Delete task")
    print("5. Quit")
    choice = input("Choose (1-5): ")
    # handle choice...
```

### Displaying Tasks

```python
def show_tasks(tasks, completed):
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "[✓]" if completed[i] else "[ ]"
        print(f"{i + 1}. {status} {task}")
```

### Adding a Task

```python
def add_task(tasks, completed):
    description = input("Enter task description: ")
    if not description:
        print("Task cannot be empty!")
        return
    tasks.append(description)
    completed.append(False)
    print(f"Added: {description}")
```

### Marking a Task Complete

```python
def complete_task(tasks, completed):
    show_tasks(tasks, completed)
    if not tasks:
        return
    try:
        index = int(input("Task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            if completed[index]:
                print("That task is already complete!")
            else:
                completed[index] = True
                print(f"Marked complete: {tasks[index]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
```

### Deleting a Task

```python
def delete_task(tasks, completed):
    show_tasks(tasks, completed)
    if not tasks:
        return
    try:
        index = int(input("Task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            completed.pop(index)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")
```

## Common Pitfalls

1. **Not handling empty lists** — If the user chooses "Mark complete" with no tasks, the program should show a friendly message, not crash.

2. **Off-by-one in index display** — Show tasks starting at 1 for the user, but subtract 1 to access the list (0-indexed).

3. **Not validating input** — The user might enter a letter when asked for a number. Use `try/except` or `.isdigit()`.

4. **Allowing empty task descriptions** — A task with no description is meaningless. Check `if not description` before adding.

5. **Forgetting to update both parallel lists** — When deleting a task, you must `pop()` from both `tasks` and `completed`.

## Hands-On Walkthrough

Your starter code is in `project/starter_code.py`. It has a `main()` function with the menu loop and placeholder comments. Your job is to fill in each section.

Here's the full solution structure:

```python
def main():
    tasks = []
    completed = []

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark complete")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            if not tasks:
                print("\nNo tasks yet!")
            else:
                print()
                for i in range(len(tasks)):
                    status = "[✓]" if completed[i] else "[ ]"
                    print(f"{i + 1}. {status} {tasks[i]}")

        elif choice == "2":
            desc = input("Enter task description: ")
            if desc:
                tasks.append(desc)
                completed.append(False)
                print(f"Added: {desc}")
            else:
                print("Task cannot be empty!")

        elif choice == "3":
            if not tasks:
                print("\nNo tasks yet!")
                continue
            for i in range(len(tasks)):
                status = "[✓]" if completed[i] else "[ ]"
                print(f"{i + 1}. {status} {tasks[i]}")
            try:
                idx = int(input("Task number to mark complete: ")) - 1
                if 0 <= idx < len(tasks):
                    if completed[idx]:
                        print("Already complete!")
                    else:
                        completed[idx] = True
                        print(f"Completed: {tasks[idx]}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("\nNo tasks yet!")
                continue
            for i in range(len(tasks)):
                status = "[✓]" if completed[i] else "[ ]"
                print(f"{i + 1}. {status} {tasks[i]}")
            try:
                idx = int(input("Task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    completed.pop(idx)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
```

## Key Takeaways

- A menu-driven program uses a `while True` loop with `break` to exit
- Parallel lists are a simple way to store related data without dictionaries
- Always validate user input — both the format (number vs text) and the range
- Display indices starting from 1 for readability; convert internally to 0-based
- Empty collections (`[]`, `""`) are falsy — use `if not tasks:` to check
- `try/except ValueError` handles non-numeric input gracefully
- Keep your code organized: consider breaking it into functions

## Next Steps
- Check your solution against `project/solution/todo.py`
- Try extending the app: add due dates, priorities, or categories
- Next module: [Module 021: Tuples](../module-021-tuples/README.md) — Learn about dictionaries for key-value data

## Further Reading
- [Real Python: Building a CLI App](https://realpython.com/command-line-interfaces-python-argparse/)
- [Python docs: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
