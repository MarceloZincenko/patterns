from knight import Knight
from archer import Archer

class Barracks(object):
    def __init__(self) -> None:
        self.units = {
        "knight": {
            1: Knight(1),
            2: Knight(2)
            },
        "archer": {
            1: Archer(1),
            2: Archer(2)
            }
        }
    
    def build_unit(self, unit_type: str, level: int) -> object:
        return self.units[unit_type][level].clone()