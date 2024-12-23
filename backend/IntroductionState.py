import time
from GameState import GameState
from Player import Player
class IntroductionState:
    def __init__(self, game_instance : GameState, player_instance : Player):
        '''
        Store the current game instance and player instance
        '''
        self.gamestate = game_instance
        self.player = player_instance
        self.name = self.player.get_player_name()
    
    def execute(self):
        print(f"Once upon a time, in a faraway kingdom, there lived a brave prince named {self.name}.")
        print("The wicked sorcerer has captured the beautiful princess Emilia in his dark castle.")
        print(f"Prince {self.name} embarks on a perilous journey to rescue the princess and bring her back to safety.")
        print(f"As Prince {self.name}, your choices will determine the outcome of this adventure...\n")
        time.sleep(2)
        
        # Set the next state to castle state
        self.gamestate.set_state("Castle")
        
    #def print_test_player(self):