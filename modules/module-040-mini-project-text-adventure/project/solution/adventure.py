"""Text Adventure Game Engine — Complete Solution

A fully-featured text adventure with rooms, items, inventory,
locked doors, dark rooms, and a riddle puzzle.
"""

import json

WORLD = {
    "entrance": {
        "name": "Dark Entrance",
        "description": "You stand at the entrance of a dark cave. "
                       "A cold wind blows from within.",
        "exits": {"north": "hallway"},
        "items": ["torch"]
    },
    "hallway": {
        "name": "Stone Hallway",
        "description": "A long hallway with torches flickering on the walls. "
                       "You see doors to the east and west.",
        "exits": {"south": "entrance", "east": "locked_door", "west": "storage"},
        "items": []
    },
    "storage": {
        "name": "Storage Room",
        "description": "A dusty storage room filled with old crates and cobwebs.",
        "exits": {"east": "hallway"},
        "items": ["key"]
    },
    "locked_door": {
        "name": "Iron Door",
        "description": "A heavy iron door blocks your path. "
                       "It has a small keyhole.",
        "exits": {"west": "hallway", "north": "treasure_room"},
        "items": [],
        "locked": True,
        "lock_item": "key"
    },
    "treasure_room": {
        "name": "Treasure Chamber",
        "description": "A glittering chamber filled with gold coins, "
                       "jewels, and ancient artifacts!",
        "exits": {"south": "locked_door"},
        "items": ["treasure", "crown"]
    },
    "dark_cave": {
        "name": "Dark Cave",
        "description": "A pitch-black cave. You can barely see your hand "
                       "in front of your face.",
        "exits": {"east": "hallway"},
        "items": ["gem"],
        "needs_item": "torch"
    },
    "riddle_room": {
        "name": "Chamber of Questions",
        "description": "A strange room with words carved into the walls. "
                       "A pedestal stands in the center.",
        "exits": {"south": "hallway"},
        "items": [],
        "riddle": {
            "question": "What has keys but can't open locks?",
            "answer": "piano",
            "reward": "magic_amulet"
        },
        "riddle_solved": False
    }
}


def get_room(room_id):
    """Look up a room by ID.

    Args:
        room_id: String key for the room

    Returns:
        Room dict or None
    """
    return WORLD.get(room_id)


def move_player(current_room, direction):
    """Move the player in a direction.

    Args:
        current_room: Current room ID
        direction: Direction to move

    Returns:
        New room ID (or current if blocked)
    """
    room = get_room(current_room)
    exits = room["exits"]

    if direction not in exits:
        print("You can't go that way.")
        return current_room

    destination = exits[direction]
    dest_room = get_room(destination)

    if dest_room and dest_room.get("locked"):
        needed = dest_room.get("lock_item", "key")
        print(f"The {dest_room['name']} is locked! You need a {needed}.")
        return current_room

    return destination


def describe_room(room_id, inventory=None, visited=None):
    """Print the description of a room.

    Args:
        room_id: Room to describe
        inventory: Player's inventory (for dark room check)
        visited: Set of visited rooms
    """
    room = get_room(room_id)
    if not room:
        print("You are in a void. Something went wrong.")
        return

    needs_item = room.get("needs_item")
    if needs_item and (not inventory or needs_item not in inventory):
        print("\n=== Pitch Black ===")
        print(room["description"])
        print("Without light, you can't do anything here.")
        return

    visited_str = " (already visited)" if visited and room_id in visited else ""
    print(f"\n=== {room['name']}{visited_str} ===")
    print(room["description"])

    if room["items"]:
        print(f"You can see: {', '.join(room['items'])}")
    else:
        print("There is nothing notable here.")

    exits = list(room["exits"].keys())
    print(f"Exits: {', '.join(exits)}")


def take_item(item, room_id, inventory):
    """Take an item from a room.

    Args:
        item: Name of the item to take
        room_id: Current room ID
        inventory: Player's item list

    Returns:
        True if taken, False otherwise
    """
    room = get_room(room_id)

    needs_item = room.get("needs_item")
    if needs_item and (needs_item not in inventory):
        print("It's too dark to see anything clearly.")
        return False

    if item in room["items"]:
        room["items"].remove(item)
        inventory.append(item)
        print(f"You take the {item}.")
        return True

    print(f"There is no {item} here.")
    return False


def show_inventory(inventory):
    """Display the player's inventory.

    Args:
        inventory: List of items
    """
    if not inventory:
        print("You are carrying nothing.")
    else:
        print(f"Inventory: {', '.join(inventory)}")


def handle_riddle(room_id, inventory, game_flags):
    """Handle a riddle room interaction.

    Args:
        room_id: Current room ID
        inventory: Player's item list
        game_flags: Game state flags
    """
    room = get_room(room_id)
    riddle = room.get("riddle")
    if not riddle:
        return

    if room.get("riddle_solved"):
        print("The room is quiet. You've already solved the riddle.")
        return

    print(f"\nA voice echoes: '{riddle['question']}'")
    answer = input("Your answer: ").strip().lower()

    if answer == riddle["answer"]:
        print("Correct! The pedestal glows and a reward appears!")
        reward = riddle["reward"]
        inventory.append(reward)
        room["riddle_solved"] = True
        print(f"You receive: {reward}")
    else:
        print("Incorrect. The room rumbles and you stumble...")
        game_flags["sent_back"] = True


def parse_command(cmd, current_room, inventory, game_flags, visited):
    """Parse and execute a command.

    Args:
        cmd: Raw input string
        current_room: Current room ID
        inventory: Player's item list
        game_flags: Game state flags
        visited: Set of visited rooms

    Returns:
        Tuple of (new_room, continue_playing)
    """
    cmd = cmd.strip().lower()
    parts = cmd.split()
    if not parts:
        return current_room, True

    action = parts[0]

    if action in ("quit", "exit"):
        print("Thanks for playing!")
        return current_room, False

    if action in ("look", "l"):
        describe_room(current_room, inventory, visited)
        return current_room, True

    if action in ("north", "n"):
        new_room = move_player(current_room, "north")
        if new_room != current_room:
            visited.add(new_room)
        return new_room, True

    if action in ("south", "s"):
        new_room = move_player(current_room, "south")
        if new_room != current_room:
            visited.add(new_room)
        return new_room, True

    if action in ("east", "e"):
        new_room = move_player(current_room, "east")
        if new_room != current_room:
            visited.add(new_room)
        return new_room, True

    if action in ("west", "w"):
        new_room = move_player(current_room, "west")
        if new_room != current_room:
            visited.add(new_room)
        return new_room, True

    if action == "take":
        if len(parts) < 2:
            print("Take what?")
        else:
            take_item(parts[1], current_room, inventory)
        return current_room, True

    if action in ("inventory", "i"):
        show_inventory(inventory)
        return current_room, True

    if action == "help":
        print("Available commands:")
        print("  look (l)            — describe the current room")
        print("  north (n) / south (s) — move in a direction")
        print("  east (e) / west (w)   — move in a direction")
        print("  take [item]         — pick up an item")
        print("  inventory (i)       — list your items")
        print("  answer [text]       — answer a riddle")
        print("  help                — show this message")
        print("  quit                — exit the game")
        return current_room, True

    if action == "answer" and len(parts) > 1:
        game_flags["riddle_answer"] = parts[1]
        handle_riddle(current_room, inventory, game_flags)
        if game_flags.get("sent_back"):
            game_flags["sent_back"] = False
            return "hallway", True
        return current_room, True

    if action == "save":
        save_game(current_room, inventory, game_flags, visited)
        return current_room, True

    if action == "load":
        loaded = load_game()
        if loaded:
            return loaded, True
        return current_room, True

    print(f"Unknown command: {action}")
    return current_room, True


def save_game(current_room, inventory, game_flags, visited):
    """Save the game state to a JSON file.

    Args:
        current_room: Current room ID
        inventory: Player's item list
        game_flags: Game state flags
        visited: Set of visited rooms
    """
    state = {
        "room": current_room,
        "inventory": inventory,
        "flags": game_flags,
        "visited": list(visited),
        "world_rooms": {}
    }
    for room_id, room in WORLD.items():
        state["world_rooms"][room_id] = {
            "items": list(room.get("items", [])),
            "riddle_solved": room.get("riddle_solved", False),
        }

    with open("savegame.json", "w") as f:
        json.dump(state, f, indent=2)
    print("Game saved.")


def load_game():
    """Load the game state from a JSON file.

    Returns:
        Tuple of (current_room, inventory, game_flags, visited) or None
    """
    try:
        with open("savegame.json") as f:
            state = json.load(f)

        for room_id, saved in state.get("world_rooms", {}).items():
            if room_id in WORLD:
                WORLD[room_id]["items"] = list(saved.get("items", []))
                if "riddle_solved" in saved:
                    WORLD[room_id]["riddle_solved"] = saved["riddle_solved"]

        print("Game loaded.")
        return (
            state["room"],
            list(state["inventory"]),
            dict(state["flags"]),
            set(state["visited"])
        )
    except FileNotFoundError:
        print("No save file found.")
        return None


def game_loop():
    """Run the main game loop."""
    current_room = "entrance"
    inventory = []
    game_flags = {}
    visited = {"entrance"}

    print("=" * 50)
    print("        TEXT ADVENTURE GAME ENGINE")
    print("=" * 50)
    print("Type 'help' for a list of commands.")
    print("Type 'quit' to exit.\n")

    describe_room(current_room, inventory, visited)

    playing = True
    while playing:
        try:
            cmd = input("\n> ")
            result = parse_command(cmd, current_room, inventory,
                                   game_flags, visited)

            if isinstance(result, tuple) and len(result) == 2:
                current_room, playing = result
            elif isinstance(result, tuple) and len(result) == 4:
                current_room, inventory, game_flags, visited = result
            else:
                pass

        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing!")
            playing = False


if __name__ == "__main__":
    game_loop()
