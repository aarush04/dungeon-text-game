import random
from Player import Player
from GameState import GameState

class Store:
    def __init__(self, game_instance : GameState, player_instance: Player):
        self.gamestate = game_instance
        self.player = player_instance
        self.name = self.player.get_player_name()
        
        
    def execute(self):
        print("You have entered a well-lit store with various items on display.")
        print("Welcome to the store! Here you can purchase items to aid you on your journey.\n")

        print("Available items:")
        print("1. Health Potion (100 coins) - Restores 100 health points.")
        print("2.5. Rusty Sword (500 coins) - Increases your attack points by 10")
        print("2. Magic Sword (1500 coins) - Increases your attack points by 30.")
        print("3. Light Armor (1000 coins) - Increases your health points by 400.")
        
        print("4. Leave the store")
        print("5. Check your player status")

        choice = input("Enter the number of the item you wish to buy (1/2/3), leave (4) or check your status (5): ")

        if choice == "1":
            # Deduct money and increase health
            print("You purchased a Health Potion.")
            current_health = self.player.health_points + 100
            if current_health >= self.player.max_health:
                self.player.health_points = self.player.max_health
            else:
                self.player.health_points += 100
            self.player.money -= 100
            print(self.player.money)
        elif choice == "2.5":
            if self.player.money < 500:
                print("Not enough money")
            elif self.player.rusty_sword == 0 and self.player.money >= 500:
                print("You purchased a Rusty Sword")
                self.player.rusty_sword = 1
                self.player.attack_points += 10
                self.player.money -= 500
                print("You equip the new Magic Sword. Your attack points increase to",
                      self.player.attack_points)
            elif self.player.rusty_sword == 1:
                print("You have already purchase the weapon.")                                
        elif choice == "2":
            if self.player.money < 1500:
                print("Not enough money.")
            # Deduct money and increase attack points
            elif self.player.weapon == 0 and self.player.money >= 1500:
                print("You purchased a Magic Sword.")
                self.player.weapon += 1
                self.player.attack_points += 30
                self.player.money -= 1500
                print("You equip the new Magic Sword. Your attack points increase to",
                      self.player.attack_points)
            elif self.player.weapon == 1:
                print("You have already purchase the weapon.")
        elif choice == "3":
            # Deduct money and reduce damage taken
            if self.player.money < 1000:
                print("Not enough money.")
            elif self.player.money >= 1000 and self.player.armor == 0:
                self.player.armor += 1
                self.player.health_points += 400
                self.player.max_health += 400
                self.player.money -= 1000
                print("You purchased Light Armor.")
                print("You equip the new Armor. Your health points increase to",
                      self.player.health_points)
                #Tru tien
            elif self.player.armor == 1:
                print("You have already purchased this weapon")
        elif choice == "4":
            print("You decide to leave the store.")
            self.gamestate.set_state("Castle")
        elif choice == "5":
            print("-----------------------------------------------------------------")
            print("Prince Edward Status")
            print("Attack Points: " + str(self.player.attack_points))
            print(f"Health Points: {self.player.health_points} / {self.player.max_health}" )
            
            print("Money: " + str(self.player.money))
        else:
            print("Invalid choice. Please select a valid option.")