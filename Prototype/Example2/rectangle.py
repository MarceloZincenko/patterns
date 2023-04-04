from interface import Shape
from copy import deepcopy

class Rectangle(Shape):

    def __init__(self, id: str, tipo: str) -> None:
        super().__init__(id, tipo)
    
    def draw(self) -> None:
        print("Inside rectangle draw method")
    
    def clone(self):
        return deepcopy(self)