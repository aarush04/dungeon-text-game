import random
from Player import Player
from GameState import GameState

class CastleState:
    #Store the current game instance and player instance
    def __init__(self, game_instance : GameState, player_instance: Player):
        self.gamestate = game_instance
        self.player = player_instance
        self.name = self.player.get_player_name()
        
    def execute(self):
        print("\n")
        print("After a treacherous journey, Prince Edward reaches the sorcerer's castle.")
        self.player.set_new_player(False)

        # List of riddles
        riddles = [
    {
        "riddle": "When writing code in Python, what keyword is used to indicate the start of a function?\n"
                  "(hint: def, func, define)",
        "answer": "def"
    },
    {"riddle": "In programming, a variable that is declared inside a function is known as a _______ variable. "
               "Fill in the blank (Hint: local, global, private) ",
     "answer": "local"},
    {"riddle": "What is the term for a piece of code that performs a specific task and can be reused in different parts of a program? "
               "(Hint: loop, module, branch)",
     "answer": "module"},
    {"riddle": "In coding, what do we call a function calling itself? (Hint: self-call, recursive, loop)",
     "answer": "recursive"},
    {"riddle": "A programming language that is known for its use in web development, especially for creating interactive and dynamic websites. "
               "(Hint: Java, Python, JavaScript)",
     "answer": "JavaScript"},
    {"riddle": "What does HTML stand for? (Hint: HyperText Markup Language, High-Level Text Language, HyperTransfer Markup Language)",
     "answer": "HyperText Markup Language"},
    {"riddle": "The process of finding and fixing errors in a computer program is known as _______. (Hint: debugging, compiling, testing)",
     "answer": "debugging"},
    {"riddle": "In version control systems like Git, what command is used to commit changes to the repository? "
               "(Hint: push, commit, save)",
     "answer": "commit"},
    {"riddle": "What do we call a collection of instructions that performs a specific task in a computer program? "
               "(Hint: algorithm, script, function)",
     "answer": "function"}

    # Add more coding riddles as needed
        ]

        print("He encounters a wise old hermit who challenges you with a riddle.")
        print("======================================================================================================")

        random_riddle = random.choice(riddles)  # Select a random riddle from the list
        answer = input(random_riddle["riddle"] + "\nYour answer: ").lower()
        #print(answer)
        if answer == random_riddle["answer"].lower():

            print("Correct! You solved the riddle.")
            self.player.attack_points += 2
            print("Your attack points increase to", self.player.attack_points)
        else:
            print("That's not the correct answer. Better luck next time.")

        val = input("Where do you want to go next: Buy Equipment, Fight Minion, Final Boss "
                    "(Store/Minion/Boss): ").lower()
        if val == "store":
            self.gamestate.set_state("Store")
        elif val == "minion":
            self.gamestate.set_state("Minion")
        elif val == "boss":
            print("pass")
            #game.set_state("FinalBoss")
        else:
            print("Invalid choice. Please select a valid option.")

        
        
        
        
        #TODO IMPLEMENT THIS 