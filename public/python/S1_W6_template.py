# ============================================================
#  SPRINT 1 · WEEK 6 — Lists & Dictionaries
#  Game Inventory System
#
#  Fill in every TODO. Run after each step.
#  Run:  python S1_W6_template.py
# ============================================================


# ── STEP 1: Lists ────────────────────────────────────────────
# A list holds multiple values in order, separated by commas.
# Index starts at 0: inventory[0] is the first item.

inventory = ["sword", "potion", "torch"]

print("Your inventory:")
print(inventory)
print(f"First item: {inventory[0]}")
print(f"Number of items: {len(inventory)}")

# TODO: print the last item using index -1 (Python counts backwards too)
# TODO: print all items using a for loop: for item in inventory:


# ── STEP 2: Modifying lists ──────────────────────────────────
# .append() adds to the end  |  .remove() deletes by value
# in checks if a value is in the list

inventory.append("magic key")
print(f"\nAfter picking up the magic key: {inventory}")

inventory.remove("torch")
print(f"After dropping the torch: {inventory}")

# TODO: check if "potion" is in inventory using  if "potion" in inventory:
#       print "You have a potion!" or "No potion found."


# ── STEP 3: Dictionaries ─────────────────────────────────────
# A dictionary stores key: value pairs.
# Access values with  dict["key"]  or  dict.get("key")

player = {
    "name":  "Hero",
    "hp":    10,
    "level": 1,
    "gold":  50
}

print(f"\nPlayer: {player['name']}")
print(f"HP: {player['hp']} | Level: {player['level']} | Gold: {player['gold']}")

# TODO: update player["hp"] to 8 (the player took damage)
# TODO: add a new key "class" with value "Warrior" to the player dict
# TODO: print all keys and values using:  for key, value in player.items():


# ── STEP 4: List of dictionaries — the real power move ───────
# Combine both structures to represent multiple things with properties.

items = [
    {"name": "sword",    "damage": 5,  "value": 10},
    {"name": "potion",   "heal":   3,  "value": 5},
    {"name": "magic key","damage": 0,  "value": 20},
]

print("\nItem details:")
for item in items:
    # TODO: print each item's name and value using an f-string
    pass


# ── STEP 5: Inventory functions ──────────────────────────────
def pick_up(inventory, item_name):
    """Adds item_name to the inventory list."""
    inventory.append(item_name)
    print(f"Picked up: {item_name}")

def drop(inventory, item_name):
    """Removes item_name if it exists, otherwise prints a message."""
    if item_name in inventory:
        inventory.remove(item_name)
        print(f"Dropped: {item_name}")
    else:
        # TODO: print "You don't have {item_name}."
        pass

def show_inventory(inventory):
    """Prints the inventory neatly."""
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("\n--- INVENTORY ---")
        for i, item in enumerate(inventory):
            # enumerate gives index i AND value item at the same time
            print(f"  {i+1}. {item}")

# Test the functions:
show_inventory(inventory)
pick_up(inventory, "shield")
drop(inventory, "potion")
drop(inventory, "dragon")   # this one doesn't exist
show_inventory(inventory)


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a  sort_inventory(inventory)  function that returns the list sorted A-Z.
# Hint: sorted(list) returns a new sorted list.
# Add a  most_valuable(items)  function that returns the item dict
# with the highest "value" key. Hint: max(items, key=lambda x: x["value"])
