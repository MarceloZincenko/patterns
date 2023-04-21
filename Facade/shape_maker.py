from circle import Circle
from square import Square
from rectangle import Rectangle

class ShapeMaker(object):

    def __init__(self) -> None:
        self.circle = Circle()
        self.rectangle = Rectangle()
        self.square = Square()
    
    def draw_circle(self) -> None:
        self.circle.draw()
    
    def draw_rectangle(self) -> None:
        self.rectangle.draw()
    
    def draw_square(self) -> None:
        self.square.draw()