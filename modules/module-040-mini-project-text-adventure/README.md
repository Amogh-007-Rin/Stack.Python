# Module 040: Milestone Project — Text-Based Adventure Game Engine

> **Phase:** 4. Functions  |  **Estimated time:** 3 hours  |  **Milestone Project:** Yes

## Prerequisites
- All modules 031-039 (Phase 4: Functions)

## Learning Objectives
By the end of this module, you will be able to:
- Build a complete text adventure game engine from scratch
- Model a game world using nested dictionaries
- Use functions to organize game logic (get_room, move_player, take_item, etc.)
- Implement inventory management
- Create simple puzzles with state-tracking
- Handle user input and game state

## Why This Matters
This milestone project ties together everything from Phase 4: functions, arguments, scope, lambdas, recursion, higher-order functions, decorators, generators, and iterators. You'll build a complete, playable game that demonstrates how functions organize complex logic.

## Project Overview

Build a text-based adventure game where the player explores rooms, finds items, and solves simple puzzles.

### Game World

The world is a collection of rooms, each with:
- A name and description
- Exits (N, S, E, W)
- Items that can be picked up
- Optional locked/puzzle state

```python
WORLD = {
    "entrance": {
        "name": "Dark Entrance",
        "description": "You stand at the entrance of a dark cave.",
        "exits": {"north": "hallway"},
        "items": ["torch"]
    },
    "hallway": {
        "name": "Stone Hallway",
        "description": "A long hallway with torches on the walls.",
        "exits": {"south": "entrance", "east": "treasure_room", "west": "storage"},
        "items": []
    },
    # ...
}
```

### Core Functions

- `get_room(room_id)` — look up room data
- `move_player(current_room, direction)` — handle movement
- `take_item(item, room, inventory)` — pick up items
- `show_inventory(inventory)` — display items
- `look(current_room)` — describe the room
- `handle_command(cmd, state)` — parse and execute commands

### Commands

- `look` / `l` — describe current room
- `move north/south/east/west` or `n/s/e/w` — move between rooms
- `take [item]` — pick up an item
- `inventory` / `i` — list items
- `help` — show available commands
- `quit` — exit the game

### Puzzles

Add at least one puzzle room:
- A locked door that requires a key
- A dark room that requires a torch
- A riddle that must be answered correctly

## Key Takeaways

- Functions organize complex game logic into manageable pieces.
- A nested dict structure models the game world naturally.
- Game state (current room, inventory, flags) is passed between functions.
- User input parsing is a real-world problem (handling synonyms, errors).
- State-tracking enables simple puzzles and conditional descriptions.

## Further Reading
- [Wikipedia: Interactive Fiction](https://en.wikipedia.org/wiki/Interactive_fiction)
- [Python docs: Building a game](https://docs.python.org/3/faq/library.html)

## Next Module
Continue to **Module 041** (Phase 5: Data Structures).
