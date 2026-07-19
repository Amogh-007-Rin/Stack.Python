# Module 020: Milestone Project: To-Do List CLI App — Quiz

## Question 1
What data structure combination is recommended for storing tasks without using dictionaries?
- A) One list of tuples
- B) Two parallel lists (tasks and completed)
- C) Two separate variables
- D) A single string with newlines

## Question 2
When a user selects "Delete task", what must you do with both parallel lists?
- A) Only pop from `tasks`
- B) Only pop from `completed`
- C) Pop from both lists at the same index
- D) Clear both lists

## Question 3
What should happen if the user selects "View tasks" but the list is empty?
- A) The program crashes
- B) Print "No tasks yet!" or similar message
- C) Nothing
- D) Print an empty line

## Question 4
When displaying tasks to the user, what numbering convention should you use?
- A) Start from 0
- B) Start from 1
- C) Start from -1
- D) No numbers

## Question 5
How should you handle the user entering a letter when asked for a task number?
- A) Let the program crash — it's the user's fault
- B) Use `try/except ValueError` to catch the error and show a message
- C) Ignore it and continue
- D) Convert the letter to a number automatically

## Question 6
What does `if not tasks:` check for?
- A) If `tasks` contains the value `None`
- B) If the `tasks` list is empty
- C) If `tasks` is not defined
- D) If `tasks` has exactly one element

## Question 7
How do you exit the main menu loop in the to-do list app?
- A) `exit()`
- B) `break`
- C) `return`
- D) `quit()`

## Question 8
What is the purpose of the `main()` function in the starter code?
- A) It's called automatically by Python
- B) It organizes the code and runs when the script is executed directly
- C) It's the same as `__name__`
- D) It handles errors

## Answers
1. B — Two parallel lists: one for descriptions, one for completion booleans
2. C — Both lists must be updated at the same index to stay in sync
3. B — Check with `if not tasks:` and show a friendly message
4. B — Display starting from 1 for readability; convert to 0-based internally
5. B — Use `try/except ValueError` to catch and handle invalid input gracefully
6. B — An empty list is falsy, so `if not tasks:` checks for an empty list
7. B — `break` exits the `while True` loop
8. B — The `main()` function contains the program logic and runs when `__name__ == "__main__"`
