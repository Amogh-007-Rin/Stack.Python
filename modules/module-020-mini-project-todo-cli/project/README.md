# Module 020 Milestone Project: To-Do List CLI

## Overview

Build a command-line to-do list manager. This is a milestone project that brings together everything you've learned in Modules 001-019.

## Requirements

Create a Python program that runs in the terminal and provides a menu-driven interface with the following features:

1. **View tasks** — Display all tasks with their status (completed or pending)
2. **Add task** — Add a new task to the list
3. **Mark complete** — Mark a task as completed
4. **Delete task** — Remove a task from the list
5. **Quit** — Exit the program

## Data Design

Use two parallel lists:

```python
tasks = []       # list of task descriptions (strings)
completed = []   # list of booleans (True = done, False = pending)
```

When you add a task, append to both lists. When you delete a task, pop from both lists.

## Specifications

- Display tasks numbered starting from **1** (not 0)
- Show `[✓]` for completed tasks and `[ ]` for pending tasks
- Validate all user input (non-empty descriptions, valid numbers for selection)
- Handle the case where the task list is empty
- Prevent marking an already-completed task as complete again
- The program should keep running until the user chooses to quit

## Example Session

```
===== TO-DO LIST =====
1. View tasks
2. Add task
3. Mark complete
4. Delete task
5. Quit
Choose (1-5): 2
Enter task description: Buy milk
Added: Buy milk

===== TO-DO LIST =====
1. View tasks
2. Add task
3. Mark complete
4. Delete task
5. Quit
Choose (1-5): 1

1. [ ] Buy milk

===== TO-DO LIST =====
1. View tasks
2. Add task
3. Mark complete
4. Delete task
5. Quit
Choose (1-5): 3
1. [ ] Buy milk
Task number to mark complete: 1
Completed: Buy milk

===== TO-DO LIST =====
1. View tasks
2. Add task
3. Mark complete
4. Delete task
5. Quit
Choose (1-5): 5
Goodbye!
```

## Getting Started

Open `starter_code.py` and fill in the TODO sections. The structure is already set up with a `main()` function and the menu loop.

## Solution

Check `solution/todo.py` after you've completed your implementation.
