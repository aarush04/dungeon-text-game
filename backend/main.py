
import time
from Player import Player
from GameState import GameState
from IntroductionState import IntroductionState
from CastleState import CastleState
from Store import Store
from Minion import MinionStage

if __name__ == "__main__":

    player = Player()
    name = input("PLease enter your character name: ")
    player.set_player_name(name)
    game = GameState()
    
    
    
    #Add the Introduction State to our list of game state in the GameState object
    game.add_state("Introduction", IntroductionState(game, player))
    game.add_state("Castle", CastleState(game, player))
    game.add_state("Store", Store(game, player))
    game.add_state("Minion", MinionStage(game, player))
    
    #game.add_state("Castle", CastleState())
    
    #Set start game state or current game state = Introduction state.
    game.set_state("Introduction")
    
    #run the game
    #print(player.get_player_name())
    print("\n")
    print("--------------------------------------Welcome to Dungeon-------------------------------")
    time.sleep(2)
    game.run()
    