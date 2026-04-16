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
    },
    "hallway": {
        "name": "Dark Hallway",
        "description" : "A long corridor. Bones crunch underfoot. Shadows move at the far end.",
        "exits": {"south": "entrance", "north": "throne_room", "east": "armory", "west": "prison"},
        "item": "health_potion",
        "enemy_chance" : 0.4,
        "visited": False
    },
    "guard_room": {
        "name": "Guard Room",
        "description" : "An abandoned guard post. A rusty sword hangs ont the wall.",
        "exits": {"west": "entrance", "north": "armory"},
        "item": "rusty_sword",
        "enemy_chance": 0.6,
        "visited": False
    },
    "armory": {
        "name": "Armory",
        "description": " An old room filled with weapons racked along the walls. Most are broken, but a few are usable.",
        "exits": {"west": "hallway", "south": "guard_room"},
        "item" : "steel_sword",
        "enemy_chance" : 0.5,
        "visited" : False
    },
    "throne_room": {
        "name": " 💀 THRONE ROOM (BOSS)",
        "description": " A massive chamber. A rotting throne sits at the center. This is the final room",
        "exits": { "south": "hallway"},
        "item" : None,
        "enemy_chance" : 1.0,
        "visited" : False,
        "is_boss_room" : True
    }
}

def get_room(room_key):
    # returns the room data for the given key
    return DUNGEON.get(room_key)

def show_room(room):
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

def move(current_room_key, direction):
    # attempts to move in a direction from the current room and returns a new room key if valid or None if the room doesn't exist.
    room = DUNGEON.get(current_room_key)
    exits = room.get("exits", {})
    if  direction in exits:return exits[direction]
    else: return None

def all_rooms_visited():
    # Returns true if all rooms are visited
    return all(room["visited"] for room in DUNGEON.values())