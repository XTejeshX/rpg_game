### PHASE 1

APRIL 08, 2026
1. CREATED A SMALL ADVENTURE GAME WITH ENTRY BANNER, CREATED A PLAYER WITH VARIOUS STATS, ADDED HEAL OPTION, AND EXITING THE GAME OPTION.


APRIL 09, 2026
1. Created an enemy.py file where all the stuff about the enemy will be present like the type of enemy and their stats and whether if the enemy is defeated or not and spawning the enemy.
2. Created an combat.py file where all the stuff about the combat will be present as of right now nothing is added into it just created a small function where the player and enemy will run into combat.


APRIL 10 2026
1. Added combat feature between player and enemy which is present in combat.py file.
2. Added enemy stats, attack where how much damage it causes to player, whether it is still alive or not and how much damage it has taken in enemy.py file.
3. Added player atttack feature, how much damage player took, whether player is alive or not in player.py file. 


APRIL 13, 2026
1. Added player level up feature improving player attack and HP in player.py file.
2. Added feature where player decides to run away with a possibility of 50% in combat.py file.



### PHASE 2

April 14, 2026
1. Planned to add multiple rooms of different types containing different bosses and drop loot.
2. Future work will include a small map in the main.py file as a print statement.
3. currently added one entrance room for now.


April 15, 2026
1. Added a map to show the dungeon in a print statement, modified player choice and possible combat in current room in main.py file.
2. Added each room description, loot drop, enemy spawn probability, exits, and whether it has been visited or not. Also added move from one to another room possiblilty and whether all rooms are visted or not in rooms.py file.
3. Planned for inventory.py file where it will contain the code that will handle the players inventory.


April 16, 2026
1. Added new features to inventory and the items and their descriptions and the functions that will be used and defined later in inventory.py file.
2. Added some function calls, fixed some indentation bugs and naming mistakes from earlier versions in main.py and rooms.py files.


April 17, 2026
1. Added 3 new features in inventory.py file where player can pickup an item from the room and store it into his inventory, view his inventory and can use items from the inventory.
2. There are minor bugs that need fixing and will be fixed in the future.


April 24, 2026
1. Forgot to add a room in rooms.py file in the dictionary, that has been rectified since it was causing an error when visiting that room.




### PHASE 3

April 24, 2026
1. Added a new save_load.py file where it will manage the creation of the save file, checks if it exist, delete the save and peek into the save file, the functions need to be defined for the functions.
2. The main file has been updated so that choice has been rearranged into main() and added a feature where typing sl will save the file.
