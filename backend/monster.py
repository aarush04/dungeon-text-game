import random

class Monster:
    def __init__(self, monster_type) -> None:
        self.monster_type = self.validate_monster_type(monster_type)
        
        if self.monster_type == "Big Bear":
            self.health = 50
            self.attack_damage = 10
            self.money = 100
        elif self.monster_type == "Goblin":
            self.health = 45
            self.attack_damage = 20
            self.money = 200
        elif self.monster_type == "Dragon":
            self.health = 100
            self.attack_damage = 35
            self.money = 350
            
    def validate_monster_type(self, monster_type):
        valid_types = ["Big Bear", "Goblin", "Dragon"]
        
        
        if monster_type in valid_types:
            return monster_type
        else:
            raise ValueError(f"Invalid monster type: {monster_type}. Valid types are: {', '.join(valid_types)}")
