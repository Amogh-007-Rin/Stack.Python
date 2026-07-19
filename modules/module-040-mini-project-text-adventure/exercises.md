# Module 040: Exercises

## Exercise 1: Add a New Room
Add a "garden" room to the world with exits to "hallway" and items ["flower"].

## Exercise 2: Drop Command
Implement a `drop [item]` command that removes an item from inventory and places it in the current room.

## Exercise 3: Locked Door Puzzle
Create a puzzle room that requires a "key" to enter. If the player doesn't have the key, print "The door is locked."

## Exercise 4: Dark Room Puzzle
Create a "dark_cave" room that requires a "torch" to see. Without the torch, print "It's too dark to see anything."

## Exercise 5: Riddle Room
Add a room with a riddle. If the player answers correctly, they get a reward item. If wrong, they are sent back.

## Exercise 6: Score System
Add a score system that tracks points for finding rooms and collecting items.

## Exercise 7: Verbose Look
Modify `describe_room()` to show a different description if the player has already visited the room.

## Exercise 8: Direction Aliases
Add support for full word directions (`north`/`south`/`east`/`west`) in addition to single-letter ones.

## Exercise 9: Use Item
Implement a `use [item]` command that has different effects depending on the room and item.

## Exercise 10: Save/Load Game
Implement save and load functionality that writes the current game state to a JSON file.
