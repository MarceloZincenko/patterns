from circle import Circle
from square import Square
from rectangle import Rectangle

class ShapeCache(object):
    def __init__(self) -> None:
        self.cache = {
        "circle": {
            1: Circle(1, "circle"),
            2: Circle(2, "circle"),
            3: Circle(3, "circle"),
            },
        "square": {
            1: Square(1, "square"),
            2: Square(2, "square"),
            3: Square(3, "square"),
            },
        "rectangle": {
            1: Rectangle(1, "rectangle"),
            2: Rectangle(2, "rectangle"),
            3: Rectangle(3, "rectangle"),
            }
        }
    
    def get_shape(self, tipo: str, id: int) -> object:
        return self.cache[tipo][id].clone()