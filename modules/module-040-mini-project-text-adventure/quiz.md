# Module 040: Quiz

## Question 1 (Multiple Choice)
What data structure is recommended for modeling the game world?
- A) A list of rooms
- B) A nested dictionary
- C) A set of tuples
- D) A string

## Question 2 (Multiple Choice)
What function handles the player moving between rooms?
- A) take_item()
- B) move_player()
- C) describe_room()
- D) show_inventory()

## Question 3 (True/False)
Items in a room should be stored in a set.
- True
- False

## Question 4 (Multiple Choice)
How should game state (current room, inventory, flags) be managed?
- A) Global variables
- B) Passed as arguments between functions
- C) Stored in a file at all times
- D) Hard-coded in every function

## Question 5 (Multiple Choice)
What does `WORLD.get(room_id)` return if the room doesn't exist?
- A) An empty dict
- B) None
- C) A KeyError
- D) False

## Question 6 (True/False)
A `for` loop is the best way to implement the main game loop.
- True
- False

## Question 7 (Multiple Choice)
What should happen when the player types "take" without specifying an item?
- A) Take a random item
- B) Print "Take what?"
- C) Do nothing silently
- D) Show inventory

## Question 8 (Multiple Choice)
How can you store whether a puzzle has been solved?
- A) In a local variable inside the function
- B) In a game_flags dictionary
- C) By deleting the room
- D) You can't

## Question 9 (Multiple Choice)
What command should display available commands to the player?
- A) look
- B) help
- C) commands
- D) hint

## Question 10 (Short Answer)
Name three essential functions any text adventure game should have.

---

## Answers

1. **B** — A nested dictionary
2. **B** — move_player()
3. **False** — A list is more appropriate (ordered, allows duplicates if needed)
4. **B** — Passed as arguments between functions
5. **B** — None
6. **False** — A `while` loop is best (runs until the player quits)
7. **B** — Print "Take what?"
8. **B** — In a game_flags dictionary
9. **B** — help
10. Any three: `get_room()`, `move_player()`, `describe_room()`, `take_item()`, `show_inventory()`, `parse_command()`, `game_loop()`
