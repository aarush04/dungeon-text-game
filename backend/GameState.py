
class GameState:
    def __init__(self):
        self.states = {}
        self.current_state = None

    
    def press_start(self, message="Press Enter to continue..."):
        '''
        This function is use to wait for player to hit Enter to move to the next stage
        '''
        input(message)


    def add_state(self, state_name, state):
        '''
        This function is use to add the state into the state list of GameState 
        '''
        self.states[state_name] = state

    def set_state(self, state_name):
        '''
        This function is use in each State to change the current stage to the next stage in the game
        
        '''
        if state_name in self.states:
            #print(state_name + "aaaaaaaaaaaaaaaaaa")
            self.current_state = self.states[state_name]
    def run(self):
        '''
        This function is use to run the current game instance.
        '''
        while self.current_state:
            self.current_state.execute()
            print("----------------------------------------------------------------------------------------")
            self.press_start()  # Wait for player to press Enter before continuing
            
    def print_state(self):
        print(self.states)