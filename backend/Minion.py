import random
from Player import Player
from GameState import GameState
from monster import Monster


class MinionStage:
    def __init__(self, game_instance : GameState, player_instance: Player):
        self.gamestate = game_instance
        self.player = player_instance
        self.name = self.player.get_player_name()
        self.new_game = 1

    def execute(self):
        if (self.new_game):
            print("Monster type: \n" "* Big Bear: easy \n" "* Goblin: moderate \n" "* Dragon: hard \n")
            print("Each Turn, player will have a chance to attack the monster and the monster get to attack you")
        
            print("We will play rock paper scissor. If you win, double the damage, If you loose half the damage, If you draw \n "
              "base damage is calculated\n" "Same thing apply for when monster try to attack you, if you loose they double the damage and etc")
            self.new_game = 0
        while (True):
            try:
                monster_type_input = input("Enter monster type: ")
                monster = Monster(monster_type_input)
                break  # Break out of the loop if input is valid
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
        choice = monster
        round_count = 1
        while (self.player.health_points > 0 and monster.health > 0) :     
            print(f"---- -------Round {round_count}------- ----")
            print(f"You and {monster_type_input} are both preparing for the next attack...\n")
            print(f"{self.player.name} healthpoints: {self.player.health_points}")
            print(f"{monster_type_input} healthpoints: {monster.health}")
            round_count +=1
             
            #Player's turn
            m_roll = random.randint(1,3)
            
            # user input
            while (True):
                #! Input can cause error
                guess = (input("Pick rock: 1, paper: 2, scissor: 3: Enter your number of choice: "))
                if ( guess != "1" and guess != "2" and guess != "3" ):

                    print("Input error try again")
                else:
                    break; #TODO check later'
            #print("PASSS")
            guess = int(guess)
            if (m_roll == int(guess)): # draw
                print(f"You inflict {self.player.attack_points} damage to monster")
                monster.health -= self.player.attack_points
                
            elif (m_roll !=int( guess)): # different than draw
                if m_roll == 1:
                    if (guess == 2): # player paper, computer rock
                        damage = 2 * self.player.attack_points
                        print(f"You dealt a powerful blow to {monster_type_input}, causing {damage} damage!")
                        monster.health -= damage
                    elif (guess == 3): #player scicsor, computer rock
                        damage = self.player.attack_points / 2
                        print(f"{monster_type_input} block half of your attack , causing {damage} damage!")
                        monster.health -= damage 
                
                elif m_roll == 2: # monster paper
                    if (guess == 3): # player scissor
                        damage = 2 * self.player.attack_points
                        print(f"You dealt a powerful blow to {monster_type_input}, causing {damage} damage!")
                        monster.health -= damage
                    elif (guess == 1): #player rock
                        damage = self.player.attack_points / 2
                        print(f"{monster_type_input} block half of your attack , causing {damage} damage!")
                        monster.health -= damage 
                elif m_roll == 3: #monster scisor
                    if (guess == 1): # player rock
                        damage = 2 * self.player.attack_points
                        print(f"You dealt a powerful blow to {monster_type_input}, causing {damage} damage!")
                        monster.health -= damage
                    elif (guess == 2): #player paper                                 
                        damage = self.player.attack_points / 2
                        print(f"{monster_type_input} block half of your attack , causing {damage} damage!")
                        monster.health -= damage
                    
            #Monster's turn  
            #print("PASS2")
            m_roll = random.randint(1,3)
            #user input
            while (True):
                guess = (input("Pick rock: 1, paper: 2, scissor: 3: Enter your number of choice: "))
                if ( guess != "1" and guess != "2" and guess != "3" ):

                    print("Input error try again")
                else:
                    break; #TODO check later'
            #print("PASS")
            guess = int(guess)
            if (m_roll == int(guess)): # draw
                print(f"{monster_type_input} inflict {monster.attack_damage} to {self.player.name}")
                self.player.health_points -= monster.attack_damage
            
            elif (m_roll != int(guess)): # different than draw
                if m_roll == 1:
                    if (guess == 2): # player paper, computer rock
                        damage = monster.attack_damage / 2
                        print(f"{self.player.name} try to dodge {monster_type_input} attack , however he still received {damage} damage!")
                        self.player.health_points -= damage 
                    elif (guess == 3): #player scicsor, computer rock
                        damage = 2 * monster.attack_damage
                        print(f"{monster_type_input} dealt a powerful blow to {self.player.name}, causing {damage} damage!")
                        self.player.health_points -= damage
                elif m_roll == 2: # monster paper
                    if (guess == 3): # player scissor
                        damage = monster.attack_damage / 2
                        print(f"{self.player.name} try to dodge {monster_type_input} attack , however he still received {damage} damage!")
                        self.player.health_points -= damage 
                    elif (guess == 1): #player rock
                        damage = 2 * monster.attack_damage
                        print(f"{monster_type_input} dealt a powerful blow to {self.player.name}, causing {damage} damage!")
                        self.player.health_points -= damage
                elif m_roll == 3: #monster scisor
                    if (guess == 1): # player rock
                        damage = monster.attack_damage / 2
                        print(f"{self.player.name} try to dodge {monster_type_input} attack , however he still received {damage} damage!")
                        self.player.health_points -= damage 
                    elif (guess == 2): #player paper                                 
                        damage = 2 * monster.attack_damage
                        print(f"{monster_type_input} dealt a powerful blow to {self.player.name}, causing {damage} damage!")
                        self.player.health_points -= damage
                       
                                      
                     
        if monster.health <= 0:
            print(f"Congratulations! You have defeated {monster_type_input}! You earned {monster.money} coins")
            self.player.money += (int)(monster.money * random.uniform(0.8, 1.2))
                # move to castle state after finish
            self.gamestate.set_state("Castle")    
        elif self.player.health_points <= 0:
            print("You are dead, you will be response with half of you money")
            self.player.money /= 2
            self.gamestate.set_state("Castle")
            
        
        
        # print("You have entered a dense jungle and encountered a fearsome minion!")
        # print("Prepare for battle...\n")
        # if self.player.attack_points >= 15:
        #     damage = random.randint(10, 19)
        #     self.player.health_points -= damage
        #     if self.player.health_points < 0:
        #         print("You died")
        #         self.player.health_points += 50
                
        #         self.gamestate.set_state("Castle")

        #     self.player.money += 200
        #     print(f"You defeated the minion with a strong attack! You took {damage} damage.")
        # elif self.player.attack_points >= 10:

        #     damage = random.randint(20, 29)
        #     self.player.health_points -= damage
        #     if self.player.health_points < 0:
        #         print("You died")
        #         self.player.health_points += 50
        #         self.game.set_state("Castle") #todo need to fix this.
        #     self.player.money += 200
        #     print(f"You defeated the minion, but took a good hit! You took {damage} damage.")
        # else:
        #     damage = random.randint(30, 50)
        #     self.player.health_points -= damage
        #     if self.player.health_points < 0:
        #         print("You died")
        #         self.player.health_points += 50
        #         self.gamestate.set_state("Castle")
        #     self.player.money += 200
        #     print(f"You struggled against the minion and suffered a heavy blow! You took {damage} damage.")

        # print(f"Your health: {self.player.health_points}")
        # print(f"Your money: {self.player.money}")
        # print("You've gained 200 coins from the battle.")
        # #add press to continue tomorow

        # print("Minh return to the castle after a long fight...")
        # # WHERE DO WANT TO GO? KEEP FIGHTING OR STOPFIGHTING.
        # # IF STOP GO TO CASTLE, IF KEEP FIGHTING REHIT THIS CLASS
        
    
