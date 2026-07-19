# Module 020: Milestone Project: To-Do List CLI App — Exercises

## Exercise 1: Complete the App
Open `project/starter_code.py` and implement all the TODO sections to build a complete to-do list CLI app. Make sure your implementation:

1. **View tasks** — Shows `[✓]` for completed tasks and `[ ]` for pending tasks. Shows "No tasks yet!" if the list is empty.
2. **Add task** — Takes a description, validates it's not empty, and adds it.
3. **Mark complete** — Shows tasks, asks for a number, marks it complete (or warns if already done).
4. **Delete task** — Shows tasks, asks for a number, removes from both `tasks` and `completed`.
5. **Quit** — Exits the program with a goodbye message.
6. **Invalid choice** — Prints an error message for choices outside 1-5.

## Exercise 2: Add a "Clear All" Option
Extend your to-do list app with a 6th menu option: "Clear All Tasks". When selected, remove all tasks from both lists. Ask "Are you sure? (y/n)" before clearing.

## Exercise 3: Add Priority Levels
Add a priority level to each task. Create a third parallel list `priorities` that stores "High", "Medium", or "Low". When adding a task, ask for priority. When viewing, show `[High]` or `[Med]` or `[Low]` before each task.

## Exercise 4: Search Tasks
Add a search feature (option 6). Ask the user for a search term, then display only tasks that contain that term (case-insensitive). Show the same `[✓]`/`[ ]` format.

## Exercise 5: Statistics
Add a statistics option that shows:
- Total number of tasks
- Number of completed tasks
- Number of pending tasks
- Percentage complete
