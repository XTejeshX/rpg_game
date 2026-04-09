# Handles everything about enemies

import random


ENEMY_TYPE = [
    {"name": "Goblin",      "hp": 30,   "attack": 8,    "gold": 5,  "xp": 1},
    {"name": "Orc",         "hp": 50,   "attack": 10,   "gold": 10, "xp": 2},
    {"name": "Skeleton",    "hp": 40,   "attack": 12,   "gold": 7,  "xp": 1},
    {"name": "Troll",       "hp": 80,   "attack": 18,   "gold": 20, "xp": 3},
    {"name": "Dark Mage",   "hp": 35,   "attack": 20,   "gold": 25, "xp": 3}
]

def spawn_enemy(player_level = 1):
    
    """
    Spawns a random enemy.
    Higher player level = chance of tougher enemies.
    Returns a copy so the original template is never modified.
    """

    # as level increases the difficulty of the enemy also increases
    max_index = min(player_level + 1, len(ENEMY_TYPE))
    template = random.choice(ENEMY_TYPE[:max_index])

    # make a fresh copy so that HP changes do not effect the template
    enemy = template.copy()
    return enemy


def is_dead(enemy):
    return enemy["hp"] <= 0