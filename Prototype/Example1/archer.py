from prototype import Prototype
from copy import deepcopy

class Archer(Prototype):
    def __init__(self, level: int) -> None:
        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "short bow"
        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 3
            self.attack_range = 10
            self.weapon = "long bow"
    
    def __str__(self) -> str:
        return f"Life: {self.life}\n" \
            f"Speed: {self.speed}\n" \
            f"Attack Power: {self.attack_power}\n" \
            f"Attack Range: {self.attack_range}\n" \
            f"Weapon: {self.weapon}\n" 
        
    def clone(self) -> object:
        return deepcopy(self)
