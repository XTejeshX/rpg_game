import player as p
import enemy as e
import combat as c
import rooms as r
import random

def show_banner():
    
    print(" This is a RPG Game, WELCOME TO THIS TEXT ADVENTURE RPG! ")

def show_map():
    # Prints a simple ASCII map showing visited rooms.
    print("""
  ┌─────────────────────────────────┐
  │          DUNGEON MAP            │
  │                                 │
  │         [THRONE ROOM]           │
  │             │                   │
  │ [PRISON]─[HALLWAY]─[ARMORY]     │
  │              │          │       │
  │          [ENTRANCE]─[GUARD RM]  │
  │                                 │
  │  ✅ = visited   ? = unknown     │
  └─────────────────────────────────┘
    """)


def main_menu():
    # player choice
    print(" [1] NEW GAME ")
    print(" [2] QUIT ")

    return input(" Enter your choice to continue :").strip()

def game_loop(player):

    # Main game loop with room navigation
    current_room_key = "Entrance"
    
    print(f"\n welcome {player['name']}! your adventure awaits You. Find the Throne room to win.")
    print("Or die trying!!")

    while True:

        room = r.get_room(current_room_key)
        r.show_room(room)

        # random  boss encounter chance
        if random.random() < room["enemy_chance"]:
            foe = e.spawn_enemy(player["level"])
        
        # Boss room: stronger enemy
        if room.get("is_boss_room"):
            foe = {"name" : "Dungeon Boss", "hp": 150, "attack": 25, "gold": 100, "xp": 50}
            print("\n 👑 The Dungeon Boss blocks your path!")

        result = c.run_combat(player, foe)


        if result == "dead":
            print("\n =================================================")
            print("                ☠️ Game Over ☠️                    ")
            print(f" Level reached: {player['level']} | Total kills: {player['kills']} | Gold collected: {player["gold"]}")
            print(" =================================================")
            return
        
        # Win condition: beating the boss
        if room.get("is_boss_room") and result == "win":
            print("\n =================================================")
            print("                🎉 You Win! 🎉                    ")
            print(f" Level reached: {player['level']} | Total kills: {player['kills']} | Gold collected: {player['gold']}")
            print(" =================================================")
            return




        # player action menu
        print("\n----------------------------------------")
        print("You are in a dungeon, What will you do?")
        print("     [n/s/e/w]   Move in a direction(north/south/east/west)")
        print("     [p]         Pick up item")
        print("     [u]         Use item")
        print("     [i]         Show inventory")
        print("     [m]         Show map")
        print("     [t]         Show stats")
        print("     [q]         Quit")
        print("----------------------------------------")
        

        choice = input("\n Enter your choice :").strip().lower()

        if choice in ("n","s","e","w"):
            direction_map = {"n": "north", "s": "south", "e": "east", "w": "west"}
            direction = direction_map[choice]
            new_room_key = r.move(current_room_key, direction)

            if new_room_key:
                current_room_key = new_room_key
            else:
                print(f"\n You can't go {direction} from here.")
        
        elif choice == "p":
            pass
        
        elif choice == "i":
            pass

        elif choice == "u":
            pass

        elif choice == "m":
            show_map()

        elif choice == "t":
            p.show_stats(player)

        elif choice == "q":
            print("\n Returning to main menu... \n")
            return

        else:
            print("\n Invalid choice")


def main():
    # game entry point
    
    show_banner()

    while True:
        choice = main_menu()

        if choice == "1":
            name = input("Enter the player's name :")

            if not name:
                name = "Hero"
            
            hero = p.create_player(name)

            hero["inventory"] = []      # Bag of consumables
            hero["weapon"] = "Fists"    # Equipped weapon
            hero["weapon_bonus"] = 0    # Bonus attack from weapon
            game_loop(hero)
        
        elif choice == "2":
            print("\n Thanks for playing adventurer!! Visit again! \n")
            break

        else:
            print("\ninvlaid choice! please enter a valid choice [1] or [2]\n")


if __name__ == "__main__":
    main()