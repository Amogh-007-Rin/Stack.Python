"""To-Do List CLI App — Solution"""


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

        # --- View tasks ---
        if choice == "1":
            if not tasks:
                print("\nNo tasks yet!")
            else:
                print()
                for i in range(len(tasks)):
                    status = "[✓]" if completed[i] else "[ ]"
                    print(f"{i + 1}. {status} {tasks[i]}")

        # --- Add task ---
        elif choice == "2":
            desc = input("Enter task description: ")
            if desc:
                tasks.append(desc)
                completed.append(False)
                print(f"Added: {desc}")
            else:
                print("Task cannot be empty!")

        # --- Mark complete ---
        elif choice == "3":
            if not tasks:
                print("\nNo tasks yet!")
                continue
            print()
            for i in range(len(tasks)):
                status = "[✓]" if completed[i] else "[ ]"
                print(f"{i + 1}. {status} {tasks[i]}")
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

        # --- Delete task ---
        elif choice == "4":
            if not tasks:
                print("\nNo tasks yet!")
                continue
            print()
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
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # --- Quit ---
        elif choice == "5":
            print("Goodbye!")
            break

        # --- Invalid choice ---
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
