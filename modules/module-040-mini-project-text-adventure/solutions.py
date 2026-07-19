"""Module 040: Text Adventure Game Engine — Solutions

Solutions for standalone exercises (not the main game implementation,
which is in project/solution/adventure.py).
"""

# Exercise 1: Add a New Room
def add_garden_room():
    """Add a garden room to the WORLD (demonstration).

    Returns:
        The garden room dict
    """
    garden = {
        "name": "Enchanted Garden",
        "description": "A beautiful garden with glowing flowers "
                       "and a gentle stream.",
        "exits": {"west": "hallway"},
        "items": ["flower"]
    }
    return garden


# Exercise 2: Drop Command
def drop_item(item, room_id, inventory):
    """Drop an item from inventory into the current room.

    Args:
        item: Name of item to drop
        room_id: Current room ID
        inventory: Player's item list

    Returns:
        True if dropped, False otherwise
    """
    if item in inventory:
        inventory.remove(item)
        WORLD[room_id]["items"].append(item)
        print(f"You drop the {item}.")
        return True
    print(f"You don't have a {item}.")
    return False


# Exercise 3: Locked Door Puzzle
def try_enter_locked(room_id, direction, inventory):
    """Try to enter a locked room.

    Args:
        room_id: Current room ID
        direction: Direction of the locked door
        inventory: Player's items

    Returns:
        Destination room if unlocked, current room if locked
    """
    room = WORLD.get(room_id)
    if not room:
        return room_id
    dest_id = room["exits"].get(direction)
    if not dest_id:
        return room_id
    dest = WORLD.get(dest_id)
    if dest and dest.get("locked"):
        if "key" in inventory:
            dest["locked"] = False
            print("You use the key. The door unlocks!")
            return dest_id
        print("The door is locked. You need a key.")
        return room_id
    return dest_id


# Exercise 4: Dark Room Puzzle
def enter_dark_room(room_id, inventory):
    """Try to enter a dark room.

    Args:
        room_id: The dark room ID
        inventory: Player's items

    Returns:
        True if player can see, False otherwise
    """
    room = WORLD.get(room_id)
    if not room:
        return False
    needs = room.get("needs_item")
    if needs and needs not in inventory:
        print("It's too dark to see anything.")
        return False
    return True


# Exercise 5: Riddle Room
def solve_riddle(room_id, answer, inventory):
    """Try to solve a riddle in a room.

    Args:
        room_id: Room with the riddle
        answer: Player's answer
        inventory: Player's items

    Returns:
        True if solved, False otherwise
    """
    room = WORLD.get(room_id)
    if not room or "riddle" not in room:
        return False
    riddle = room["riddle"]
    if answer.lower().strip() == riddle["answer"].lower():
        if not room.get("riddle_solved"):
            reward = riddle["reward"]
            inventory.append(reward)
            room["riddle_solved"] = True
            print(f"Correct! You receive: {reward}")
        else:
            print("You already solved this riddle.")
        return True
    print("Incorrect answer.")
    return False


# Exercise 6: Score System
def calculate_score(visited, inventory, solved_riddles):
    """Calculate the player's score.

    Args:
        visited: Set of visited rooms
        inventory: Player's items
        solved_riddles: Number of riddles solved

    Returns:
        Total score
    """
    score = 0
    score += len(visited) * 10
    score += len(inventory) * 25
    score += solved_riddles * 50
    return score


# Exercise 7: Verbose Look (visited tracking)
def describe_with_visited(room_id, visited):
    """Describe a room, noting if already visited.

    Args:
        room_id: Room to describe
        visited: Set of visited room IDs
    """
    room = WORLD.get(room_id)
    if not room:
        return
    visited_tag = " (familiar)" if room_id in visited else ""
    print(f"\n=== {room['name']}{visited_tag} ===")
    print(room["description"])


# Exercise 8: Direction Aliases (handled in parse_command)
# Full word and single-letter aliases are already supported


# Exercise 9: Use Item
def use_item(item, room_id, inventory, game_flags):
    """Use an item in a specific room.

    Args:
        item: Item to use
        room_id: Current room
        inventory: Player's items
        game_flags: Game state flags

    Returns:
        True if item was used, False otherwise
    """
    if item not in inventory:
        print(f"You don't have {item}.")
        return False

    if item == "torch" and room_id == "dark_cave":
        game_flags["lit"] = True
        print("You light the torch. The cave illuminates!")
        return True

    if item == "key" and WORLD.get(room_id, {}).get("locked"):
        WORLD[room_id]["locked"] = False
        print("You unlock the door with the key.")
        return True

    print(f"Nothing happens when you use the {item} here.")
    return False


# Exercise 10: Save/Load Game
import json


def save_game_state(filename, current_room, inventory, game_flags, visited):
    """Save game state to a JSON file.

    Args:
        filename: Path to save file
        current_room: Current room
        inventory: Player's items
        game_flags: Game state dict
        visited: Set of visited rooms
    """
    state = {
        "room": current_room,
        "inventory": inventory,
        "flags": game_flags,
        "visited": list(visited),
        "world_state": {}
    }
    for rid, room in WORLD.items():
        state["world_state"][rid] = {
            "items": list(room.get("items", [])),
            "locked": room.get("locked", False),
            "riddle_solved": room.get("riddle_solved", False)
        }
    with open(filename, "w") as f:
        json.dump(state, f, indent=2)
    print(f"Game saved to {filename}.")


def load_game_state(filename):
    """Load game state from a JSON file.

    Args:
        filename: Path to save file

    Returns:
        Tuple of (current_room, inventory, game_flags, visited) or None
    """
    try:
        with open(filename) as f:
            state = json.load(f)

        for rid, saved in state.get("world_state", {}).items():
            if rid in WORLD:
                WORLD[rid]["items"] = list(saved.get("items", []))
                WORLD[rid]["locked"] = saved.get("locked", False)
                WORLD[rid]["riddle_solved"] = saved.get("riddle_solved", False)

        print(f"Game loaded from {filename}.")
        return (
            state["room"],
            list(state["inventory"]),
            dict(state["flags"]),
            set(state["visited"])
        )
    except FileNotFoundError:
        print(f"No save file found: {filename}")
        return None


# Reference for module-level WORLD access in exercises
WORLD = {
    "entrance": {
        "name": "Dark Entrance",
        "description": "Cave entrance.",
        "exits": {"north": "hallway"},
        "items": ["torch"]
    },
    "hallway": {
        "name": "Stone Hallway",
        "description": "A long hallway.",
        "exits": {"south": "entrance", "east": "locked_door"},
        "items": []
    },
    "locked_door": {
        "name": "Iron Door",
        "description": "A locked iron door.",
        "exits": {"west": "hallway"},
        "items": [],
        "locked": True
    },
    "dark_cave": {
        "name": "Dark Cave",
        "description": "A pitch-black cave.",
        "exits": {"east": "hallway"},
        "items": [],
        "needs_item": "torch"
    },
    "riddle_room": {
        "name": "Riddle Chamber",
        "description": "A room with a riddle.",
        "exits": {"south": "hallway"},
        "items": [],
        "riddle": {
            "question": "What has to be broken before you can use it?",
            "answer": "egg",
            "reward": "gold_coin"
        },
        "riddle_solved": False
    }
}
