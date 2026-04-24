# This file will save the current game progress upto a point, it will handle saving and loading the game progress usnig JSON

import json
import os

SAVE_FILE = "savegame.json"

def save_game(player, current_room_key):
    # save the currnt game situation into a JSON file, writes the player data , current room in to savegame.json
    pass

def load_game():
    #loads game state from the JSON save file, returns (player, current_room_key) or (None, None) if no save exists.
    pass

def delete_save():
    # Deletes the save file, it is used afther a game is completed or upon request/call
    pass

def save_exists():
    # returns whether or not a save file exists
    pass

def show_save_info():
    # peeks into the save file and give basic info without fully loading
    pass