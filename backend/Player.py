import time
import random
import os

'''
Player class, contains information about current player.
'''

class Player:
    def __init__(self):
        self.name = "Alpha"
        self.attack_points = 0
        self.health_points = 100
        self.max_health = 100
        self.money = 1000
        self.new_player = True
        self.weapon = 0
        self.rusty_sword = 0
        self.armor = 0
        

    '''
    Set get function for Player
    '''
    
    def set_new_player(self, new_player):
        self.new_player = new_player
    
    def get_new_player_status(self):
        return self.new_player
    
    def get_attack_points(self):
        return self.attack_points
    def set_play_attack_points(self, point):
        self.attack_points = point
    
    def set_player_name(self, name) :
        self.name = name
    def get_player_name(self):
        return self.name