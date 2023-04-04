from interface import Shape
from copy import deepcopy

class Square(Shape):

    def __init__(self, id: str, tipo: str) -> None:
        super().__init__(id, tipo)
    
    def draw(self) -> None:
        print("Inside square draw method")
    
    def clone(self):
        return deepcopy(self)