"""Module 020: To-Do List CLI App — Solutions

Complete implementation plus extensions for exercises 1-5.
"""


def show_tasks(tasks, completed, priorities=None):
    """Display all tasks with status and optional priority."""
    if not tasks:
        print("\nNo tasks yet!")
        return False
    print()
    for i in range(len(tasks)):
        status = "[✓]" if completed[i] else "[ ]"
        if priorities:
            print(f"{i + 1}. {status} [{priorities[i]}] {tasks[i]}")
        else:
            print(f"{i + 1}. {status} {tasks[i]}")
    return True


def add_task(tasks, completed, priorities=None):
    """Add a new task with optional priority."""
    desc = input("Enter task description: ")
    if not desc:
        print("Task cannot be empty!")
        return
    tasks.append(desc)
    completed.append(False)
    if priorities is not None:
        while True:
            p = input("Priority (H/M/L): ").upper()
            if p in ("H", "M", "L"):
                priority_map = {"H": "High", "M": "Medium", "L": "Low"}
                priorities.append(priority_map[p])
                break
            print("Enter H, M, or L.")
    print(f"Added: {desc}")


def mark_complete(tasks, completed):
    """Mark a task as completed."""
    if not show_tasks(tasks, completed):
        return
    try:
        idx = int(input("Task number to mark complete: ")) - 1
        if 0 <= idx < len(tasks):
            if completed[idx]:
                print("That task is already complete!")
            else:
                completed[idx] = True
                print(f"Completed: {tasks[idx]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks, completed, priorities=None):
    """Delete a task and its associated data."""
    if not show_tasks(tasks, completed):
        return
    try:
        idx = int(input("Task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            completed.pop(idx)
            if priorities is not None:
                priorities.pop(idx)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def clear_all(tasks, completed, priorities=None):
    """Clear all tasks after confirmation."""
    if not tasks:
        print("No tasks to clear.")
        return
    confirm = input("Clear all tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        completed.clear()
        if priorities is not None:
            priorities.clear()
        print("All tasks cleared.")
    else:
        print("Cancelled.")


def search_tasks(tasks, completed, priorities=None):
    """Search tasks by keyword."""
    if not tasks:
        print("No tasks yet!")
        return
    term = input("Search for: ").lower()
    print()
    found = False
    for i in range(len(tasks)):
        if term in tasks[i].lower():
            status = "[✓]" if completed[i] else "[ ]"
            if priorities:
                print(f"{i + 1}. {status} [{priorities[i]}] {tasks[i]}")
            else:
                print(f"{i + 1}. {status} {tasks[i]}")
            found = True
    if not found:
        print(f"No tasks matching '{term}'.")


def show_stats(tasks, completed):
    """Display task statistics."""
    total = len(tasks)
    if total == 0:
        print("No tasks yet!")
        return
    done = sum(1 for c in completed if c)
    pending = total - done
    pct = (done / total) * 100
    print(f"\nTotal: {total}")
    print(f"Completed: {done}")
    print(f"Pending: {pending}")
    print(f"Progress: {pct:.1f}%")


def main():
    tasks = []
    completed = []
    priorities = None  # set to [] for Exercise 3

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark complete")
        print("4. Delete task")
        print("5. Quit")
        print("6. Clear all")
        print("7. Search")
        print("8. Statistics")

        choice = input("Choose (1-8): ")

        if choice == "1":
            show_tasks(tasks, completed, priorities)
        elif choice == "2":
            add_task(tasks, completed, priorities)
        elif choice == "3":
            mark_complete(tasks, completed)
        elif choice == "4":
            delete_task(tasks, completed, priorities)
        elif choice == "5":
            print("Goodbye!")
            break
        elif choice == "6":
            clear_all(tasks, completed, priorities)
        elif choice == "7":
            search_tasks(tasks, completed, priorities)
        elif choice == "8":
            show_stats(tasks, completed)
        else:
            print("Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()
