# rooms.py - Defines the dungeon map and room navigation

# The dungeon Map
# Each room has a name, description, exits, item, enemy chance, visited or not

DUNGEON = {
    "entrance": {
        "name": "Dungeon Entrance",
        "description" : " A dimly lit entrance with moss-covered walls. The air is damp and musty and smells of rot.",
        "exits": {"north": "hallway", "east": "guard_room"},
        "item": "torch",
        "enemy_chance" : 0.0,
        "visited": False
    }
}

def get_room(room_key):
    # returns the room data for the given key
    return DUNGEON.get(room_key)

def show_room(room)
    # displays the room description, exits, and any items
    print(f"\n 📍 {room['name']}")
    print(room['description'])

    # Show exits
    exits = list(room['exits'].keys())
    print(f"\n Exits: {','.join(exits)}")

    # Show item if present
    if room["item"]:
        item_name = room["item"].replace("_", " ").title()
        print(f"\n You see a {item_name} on the ground.")

    # Mark the room as visited
    if not room["visited"]:
        print("\n This is your first time here.")
        room["visited"] = True