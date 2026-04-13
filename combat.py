import enemy as e
import player as p
import random



def run_combat(player, enemy):
    
    # this function will handle the combat between player and enemy

    print(f"\n A wild enemy {enemy["name"]} appears!")
    e.show_enemy_stats(enemy)

    while p.is_alive(player) and not e.is_dead(enemy):
        print("\n --------------------------------------")
        print(f" Your HP : {player["hp"]} / {player["max_hp"]}")
        print(f" Enemy HP : {enemy["hp"]}")
        print(" \nWhat is your plan? ")
        print("     [1] Attack the enemy.")
        print("     [2] Run away.")

        choice = input(" Enter your choice(1/2) :").strip()

        if  choice == "1":
            # player attacks the enemy

            dmg = p.player_attack(player)
            e.take_damage(enemy, dmg)
            print(f"\n ⚔️ You have dealt {dmg} damage to the enemy {enemy["name"]}!")

            if e.is_dead(enemy):
                print(f"\n 🎉 congratulations! You have defeated the enemy {enemy["name"]}")
                # player gets rewarded

                player["gold"] += enemy["gold"]
                player["kills"] += 1

                print(f" You have found {enemy["gold"]} gold! (Total gold : {player["gold"]})")

                if player["kills"] % 3 == 0:
                    p.level_up(player)

                return "win"
        
            #  enemy fights back if it is still alive
            enemy_dmg = e.enemy_attack(enemy)
            p.take_damage(player, enemy_dmg)
            print(f"\n 😈 {enemy["name"]} hits you for a damage {enemy_dmg}!")

            if not p.is_alive(player):
                print("\n 💀 You have been defeated by the enemy...")
                return "dead"
            


        elif choice == "2":
            # player tries to run away
            print("\n You  attempt to run away...")
            # 50% chance to successfully run away
            if random.random() < 0.5:
                print("\n You have successfully escaped from the enemy!")
                return "flee"
            else:
                print("\n You have failed to escape!")
                enemy_dmg = e.enemy_attack(enemy)
                p.take_damage(player, enemy_dmg)
                print(f"\n 😈 {enemy["name"]} hits you for a damage {enemy_dmg}! while fleeing")


                if not p.is_alive(player):
                    print("\n 💀 You have been defeated by the enemy while trying to flee...")
                    return "dead"


        else:
            print("\n Invalid choice. Please choose 1 or 2.")