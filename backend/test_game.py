class Monster:
    def __init__(self, monster_type):
        self.monster_type = self.validate_monster_type(monster_type)

        if self.monster_type == "Goblin":
            self.health = 50
            self.attack_damage = 10
        elif self.monster_type == "Dragon":
            self.health = 200
            self.attack_damage = 30
        # Add more conditions for other types of monsters

    def validate_monster_type(self, monster_type):
        valid_types = ["Goblin", "Dragon", "OtherMonsterType"]  # Add more valid types as needed

        if monster_type in valid_types:
            return monster_type
        else:
            raise ValueError(f"Invalid monster type: {monster_type}. Valid types are: {', '.join(valid_types)}")

    def __str__(self):
        return f"{self.name} ({self.monster_type}) - Health: {self.health}, Attack Damage: {self.attack_damage}"

# Example usage:
while True:
    try:
        monster_type_input = input("Enter monster type: ")
        monster = Monster(monster_type_input)
        break  # Break out of the loop if input is valid
    except ValueError as e:
        print(f"Error: {e}. Please try again.")