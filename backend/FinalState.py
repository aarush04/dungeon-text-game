import random
from Player import Player
from GameState import GameState
import time
class FinalBossStage:
    def __init__(self):
        self.states = {}
        self.current_state = None
    
    def execute(self):
        print("You have reached the lair of the wicked sorcerer, the final boss!")
        print("Prepare for the ultimate battle...\n")

        boss_health = 1000
        round_count = 1
        flag = 0
        flag1 = 0
        while self.player.health_points > 0 and boss_health > 0:
            print(f"---- Round {round_count} ----")
            print("You and the boss are both preparing for the next attack...\n")

            # Player's turn
            player_attack = int(random.uniform(0.8, 1.2) * self.player.attack_points)
            boss_health -= player_attack
            print(f"You dealt a powerful blow to the boss, causing {player_attack} damage!")

            if boss_health <= 0:
                # SUA LAI O DAY FOR ENGIDNG

                print("Congratulations! You have defeated the wicked sorcerer and saved Princess Emilia!")
                self.game.set_state("Ending")
                break

            print(f"Boss's health: {boss_health}")
            
            # Boss's turn
            boss_attack = int(random.uniform(1.0, 1.5) * 10)
            self.player.health_points -= boss_attack
            print(f"The boss unleashes a devastating spell, dealing {boss_attack} damage to you!")

            print(f"Your health: {self.player.health_points}")

            # Round ends, adjust health points
            self.player.health_points = max(self.player.health_points, 0)
            boss_health = max(boss_health, 0)

            round_count += 1
            time.sleep(1)

            print("\n------------------------------------------------------\n")
            if boss_health <= 200 and flag == 0:
                flag = 1
                print("The boss is weakened! You have a chance to land a critical blow.")
                print("If you think you deserve the princess, let's see how much you can understand her.")
                answer = input("What is the time complexity of a binary search algorithm? ").lower()

                if answer == "O(log n)":
                    print("It seems you remember something")
                    print("Critical hit! You dealt 100 damage to the boss!")
                    boss_health -= 100
                else:
                    print("Critical hit! You received 120 damage from the boss!")
                    print("\n")
                    self.player.health_points -= 120
            if boss_health < 100 and flag1 == 0 and self.player.health_points > 0:
                flag1 = 1
                print("n")
                print("The wicked sorcerer: Why do you have to try so hard to save her?")
                print("....")
                time.sleep(2)
                print("Edward: Dieeeeeeeeeeeeeeeeeee")
                input("Press Enter to continue...")

        if boss_health > 0:
            print("You have been defeated by the sorcerer. Princess Emilia remains captive...")
            print("Game Over. Try again to save the princess!")
