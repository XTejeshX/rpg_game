

def show_banner():
    
    print(" This is a RPG Game, WELCOME TO THIS TEXT ADVENTURE RPG! ")


def main_menu():
    # player choice
    print(" [1] NEW GAME ")
    print(" [2] QUIT ")

    return input(" Enter your choice to continue :").strip()



def main():
    # game entry point
    
    show_banner()

    while True:
        choice = main_menu()

        if choice == 1:
            pass
        
        elif choice == 2:
            print("\n Thanks for playing adventurer!! Visit again! \n")

        else:
            print("\ninvlaid choice! please enter a valid choice [1] or [2]\n")


if __name__ == "__main__":
    main()