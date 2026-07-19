# Module 040 Milestone Project: Text-Based Adventure Game Engine

## Overview

Build a text-based adventure game where the player explores rooms, collects items, and solves puzzles. This project brings together everything from Phase 4 (Modules 031-039).

## World Design

Your world is a dictionary of rooms. Each room has:

```python
"room_id": {
    "name": "Room Name",
    "description": "A description of the room.",
    "exits": {"north": "other_room", "south": "another_room"},
    "items": ["item1", "item2"]
}
```

## Minimum Requirements

1. At least **4 rooms** connected by exits
2. At least **2 items** that can be picked up
3. The commands: `look`, `north`/`south`/`east`/`west`, `take [item]`, `inventory`, `help`, `quit`
4. At least **one puzzle** (locked door, dark room, or riddle)
5. All functions must have **Google-style docstrings**

## Commands to Support

| Command | Aliases | Description |
|---------|---------|-------------|
| `look` | `l` | Describe the current room |
| `north` | `n` | Move north |
| `south` | `s` | Move south |
| `east` | `e` | Move east |
| `west` | `w` | Move west |
| `take [item]` | — | Pick up an item |
| `inventory` | `i` | Show carried items |
| `help` | — | Show available commands |
| `quit` | `exit` | Exit the game |

## Puzzle Ideas

- **Locked door**: A room requires a "key" item to enter.
- **Dark room**: A room requires a "torch" to reveal items and exits.
- **Riddle room**: The player must answer a question correctly.
- **Combination lock**: The player must enter the correct numbers.

## Getting Started

1. Open `starter_code.py`
2. Fill in the `WORLD` dictionary with your rooms
3. Implement each function marked with `TODO`
4. Test your game by running `python3 starter_code.py`

## Solution

Check `solution/adventure.py` after completing your implementation.
