"""Text Adventure Game Engine — Starter Code

Fill in the TODO sections to complete the game.
"""

WORLD = {
    # TODO: Add at least 4 rooms
    # Each room needs: name, description, exits, items
    "entrance": {
        "name": "Dark Entrance",
        "description": "You stand at the entrance of a dark cave.",
        "exits": {"north": "hallway"},
        "items": ["torch"]
    },
}


def get_room(room_id):
    """Look up a room by ID.

    Args:
        room_id: String key for the room

    Returns:
        Room dict or None
    """
    # TODO: Return the room from WORLD
    pass


def move_player(current_room, direction):
    """Move the player in a direction.

    Args:
        current_room: Current room ID
        direction: Direction to move

    Returns:
        New room ID (or current if blocked)
    """
    # TODO: Check exits dict for the direction
    # TODO: If found, return the destination room ID
    # TODO: If not found, print error and return current room
    pass


def describe_room(room_id):
    """Print the description of a room.

    Args:
        room_id: Room to describe
    """
    # TODO: Print room name, description, items, and exits
    pass


def take_item(item, room_id, inventory):
    """Take an item from a room.

    Args:
        item: Name of the item to take
        room_id: Current room ID
        inventory: Player's item list

    Returns:
        True if taken, False otherwise
    """
    # TODO: Check if item is in the room's items list
    # TODO: Remove from room, add to inventory
    # TODO: Print appropriate messages
    pass


def show_inventory(inventory):
    """Display the player's inventory.

    Args:
        inventory: List of items
    """
    # TODO: Show items or "You are carrying nothing."
    pass


def parse_command(cmd, current_room, inventory, game_flags):
    """Parse and execute a command.

    Args:
        cmd: Raw input string
        current_room: Current room ID
        inventory: Player's item list
        game_flags: Dict of game state flags

    Returns:
        Tuple of (new_room, continue_playing)
    """
    # TODO: Parse the command and call appropriate functions
    # TODO: Handle: look, north/south/east/west, take, inventory, help, quit
    pass


def game_loop():
    """Run the main game loop."""
    # TODO: Initialize state, print welcome, run command loop
    pass


if __name__ == "__main__":
    game_loop()
