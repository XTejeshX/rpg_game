
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