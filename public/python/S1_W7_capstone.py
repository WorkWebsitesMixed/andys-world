# ============================================================
#  SPRINT 1 · WEEK 7 — GAME CAPSTONE
#  Text Adventure Game — Project Scaffold
#
#  This is YOUR game. The structure is provided.
#  Fill in the rooms, write the descriptions, add items,
#  and create a win condition that makes sense for your story.
#
#  Minimum requirements:
#    [ ] At least 4 rooms connected by exits
#    [ ] At least 3 items to pick up
#    [ ] At least 1 locked door (requires an item to pass)
#    [ ] A win condition (player reaches a special room or finds an item)
#    [ ] A lose condition (player runs out of HP or makes a fatal choice)
# ============================================================


# ── WORLD DATA ───────────────────────────────────────────────
# Each room is a key in this dictionary.
# "exits" maps direction strings to other room names.
# "items" is a list of items in that room (empty = no items).
# "description" is printed when the player enters.

rooms = {
    "entrance": {
        "description": "You stand in a dusty entrance hall. Cobwebs hang from the ceiling.",
        "exits": {"north": "library", "east": "kitchen"},
        "items": ["rusty key"],
    },
    "library": {
        "description": "TODO: write a description for the library.",
        "exits": {"south": "entrance", "north": "tower"},
        "items": ["ancient map"],
    },
    "kitchen": {
        "description": "TODO: write a description for the kitchen.",
        "exits": {"west": "entrance"},
        "items": ["health potion"],
    },
    "tower": {
        "description": "TODO: write a description for the tower.",
        "exits": {"south": "library"},
        "items": [],
        "locked": True,          # requires "rusty key" to enter
        "key_required": "rusty key",
    },
    # TODO: add at least one more room of your own
}

WIN_ROOM  = "tower"    # reaching this room wins the game
START_ROOM = "entrance"


# ── PLAYER STATE ─────────────────────────────────────────────
player = {
    "location":  START_ROOM,
    "inventory": [],
    "hp":        10,
}


# ── HELPER FUNCTIONS ─────────────────────────────────────────
def describe_room(rooms, player):
    """Prints the current room's description, exits and items."""
    room = rooms[player["location"]]
    print("\n" + "=" * 40)
    print(room["description"])
    print(f"Exits: {', '.join(room['exits'].keys())}")
    if room["items"]:
        print(f"You see: {', '.join(room['items'])}")
    print(f"HP: {player['hp']} | Inventory: {player['inventory'] or 'empty'}")


def pick_up(rooms, player, item_name):
    """Picks up an item from the current room into the player's inventory."""
    room = rooms[player["location"]]
    if item_name in room["items"]:
        room["items"].remove(item_name)
        player["inventory"].append(item_name)
        print(f"Picked up: {item_name}")
    else:
        print(f"There is no {item_name} here.")


def move(rooms, player, direction):
    """Moves the player in the given direction if an exit exists."""
    room = rooms[player["location"]]

    if direction not in room["exits"]:
        print("You can't go that way.")
        return

    next_room_name = room["exits"][direction]
    next_room      = rooms[next_room_name]

    # Check for a locked door
    if next_room.get("locked"):
        key = next_room.get("key_required")
        if key in player["inventory"]:
            print(f"You use the {key} to unlock the door.")
            next_room["locked"] = False
        else:
            print(f"The door is locked. You need: {key}")
            return

    player["location"] = next_room_name
    print(f"You move {direction}.")


# ── MAIN GAME LOOP ───────────────────────────────────────────
def main():
    print("=" * 40)
    print("  DUNGEON ESCAPE")
    print("  Type: go [direction] | take [item] | inventory | quit")
    print("=" * 40)

    describe_room(rooms, player)

    while True:
        # Check win condition
        if player["location"] == WIN_ROOM:
            print("\nYOU WIN! You escaped the dungeon!")
            break

        # Check lose condition
        if player["hp"] <= 0:
            print("\nYOU LOSE! You ran out of health.")
            break

        command = input("\n> ").strip().lower()

        if command.startswith("go "):
            direction = command[3:]
            move(rooms, player, direction)
            describe_room(rooms, player)

        elif command.startswith("take "):
            item = command[5:]
            pick_up(rooms, player, item)

        elif command == "inventory":
            print(f"Inventory: {player['inventory'] or 'empty'}")

        elif command == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Unknown command. Try: go [direction], take [item], inventory, quit")

        # TODO: add a "look" command that re-prints the room description
        # TODO: add a "drop [item]" command that puts an item back in the room
        # TODO: add random encounters: 20% chance of losing 1 HP per move


if __name__ == "__main__":
    main()
