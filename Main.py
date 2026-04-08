import player as p

def show_banner():
    
    print(" This is a RPG Game, WELCOME TO THIS TEXT ADVENTURE RPG! ")


def main_menu():
    # player choice
    print(" [1] NEW GAME ")
    print(" [2] QUIT ")

    return input(" Enter your choice to continue :").strip()

def game_loop(player):
    print(f"\n welcome {player['name']}! your adventure awaits You.")
    print(" Survive as long as possible and defeat enemies to level up. ")

    while True:
        print("\n----------------------------------------")
        print("You are in a dungeon, What will you do?")
        print(" [1] Explore the dungeon and find enemy.")
        print(" [2] Rest (heal 20 HP, costs 10 gold)")
        print(" [3] Display Stats.")
        print(" [4] Quit to Menu.")

        choice = input("Enter your choice:").strip()

        if choice == "1":
            pass

        elif choice == "2":
            if player["gold"] >= 10:
                player["gold"] -= 10
                p.heal_player(player, 20)
            else:
                print("\n player does not have enough gold to rest (Need 10 gold)")

        elif choice == "3":
            p.show_stats(player)
        
        elif choice == "4":
            print("\n returning to main Menu...")
            break

        else:
            print("\n Invalid choice")


def main():
    # game entry point
    
    show_banner()

    while True:
        choice = main_menu()

        if choice == 1:
            name = input("Enter the player's name")

            if not name:
                name = "Hero"
            
            hero = p.create_player(name)
            game_loop(hero)
        
        elif choice == 2:
            print("\n Thanks for playing adventurer!! Visit again! \n")
            break

        else:
            print("\ninvlaid choice! please enter a valid choice [1] or [2]\n")


if __name__ == "__main__":
    main()