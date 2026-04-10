
import random

def create_player(name):
    player = {
        "name"  : name,
        "hp"    : 100,
        "max_hp": 100,
        "attack": 15,
        "gold"  : 0,
        "level" : 1,
        "kills" : 0    
    }

    return player

def player_attack(player):
    """
    Calculates player's damage with a small random variance.
    Returns the damage value.
    """
    damage = random.randint(
        max(1, player["attack"] - 3),
        player["attack"] + 3
    )
    return damage

def heal_player(player, amount):
    player["hp"] += amount
    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]

    print(f" Nice!! You healed {amount} HP! (HP: {player['hp']}/{player['max_hp']})")

def show_stats(player):
    print("===== CURRENT PLAYER STATS =====")
    print(f" Name    : {player['name']}")
    print(f" Level   : {player['level']}")
    print(f" HP      : {player['hp']} / {player['max_hp']}")
    print(f" Attack  : {player['attack']}")
    print(f" Gold    : {player['gold']}")
    print(f" Kills   : {player['kills']}")
    print("================================\n")


def is_alive(player):
    # returns a boolean value whether player is alive( return True ) or not( return False ).
    return player["hp"] > 0


def take_damage(player, damage):
    # player takes damage from enemy and reduces player HP
    player["hp"] -= damage
    
    # player HP cannot go into negative values so we do the below step
    if player["hp"] < 0:
        player["hp"] = 0


def level_up(player):
    # level up player and improve stats
    pass