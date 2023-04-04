from prototype import Prototype
from copy import deepcopy

class Knight(Prototype):
    def __init__(self, level: int) -> None:
        self.unit_type = "Knight"
        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 1
            self.weapon = "short sword"
        elif level == 2:
            self.life = 400
            self.speed = 5
            self.attack_power = 6
            self.attack_range = 2
            self.weapon = "long sword"
    
    def __str__(self) -> str:
        return f"Life: {self.life}\n" \
            f"Speed: {self.speed}\n" \
            f"Attack Power: {self.attack_power}\n" \
            f"Attack Range: {self.attack_range}\n" \
            f"Weapon: {self.weapon}\n" 
    
    def clone(self):
        return deepcopy(self)

