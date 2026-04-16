# this file will contain about the code of items pickup and usage etc
# Each item has an name description and effect.

ITEMS = {
    "torch": {
        "name": "Torch",
        "description": "Lights up dark room. No Combat use.",
        "effect": "none"
    },
    "health_potion": {
        "name": "Health Potion",
        "description": "Heals and restores 40 HP to player when used.",
        "effect": "heal",
        "value" : 40
    },
    "rusty_sword": {
        "name": "RUSTY SWORD",
        "description": "An old sword which fuctions. +5 Attack",
        "effect": "attack_boost",
        "value" : 5
    },
    "steel_sword": {
        "name": "Steel Sword",
        "description": "A sharp, well-balanced blade. +12 attack",
        "effect": "attack_boost",
        "value" : 40
    },
    "gold_pouch": {
        "name": "Gold Pouch",
        "description": "A pouch filled with 30 gold coins.",
        "effect": "gold",
        "value" : 30
    }
}


def pick_up_item(player, room):
    pass


def show_inventory(player):
    pass


def use_item(player):
    pass