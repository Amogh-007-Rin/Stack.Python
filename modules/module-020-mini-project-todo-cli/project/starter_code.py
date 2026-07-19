"""To-Do List CLI App — Starter Code

Fill in the TODO sections to complete the app.
"""


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
            # TODO: Display all tasks with [✓] or [ ] status
            # Hint: Check if tasks is empty first
            pass  # replace with your code

        # --- Add task ---
        elif choice == "2":
            # TODO: Get task description from user
            # TODO: Validate it's not empty
            # TODO: Append to tasks and completed lists
            pass  # replace with your code

        # --- Mark complete ---
        elif choice == "3":
            # TODO: Check if tasks is empty
            # TODO: Display tasks with numbers
            # TODO: Get task number from user
            # TODO: Validate the number
            # TODO: Mark as completed (or warn if already done)
            pass  # replace with your code

        # --- Delete task ---
        elif choice == "4":
            # TODO: Check if tasks is empty
            # TODO: Display tasks with numbers
            # TODO: Get task number from user
            # TODO: Validate the number
            # TODO: Remove from BOTH tasks and completed
            pass  # replace with your code

        # --- Quit ---
        elif choice == "5":
            print("Goodbye!")
            break

        # --- Invalid choice ---
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
