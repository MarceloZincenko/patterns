class Shape:
    def draw(self) -> None:
        pass

    def area(self) -> None:
        pass

class Rectangle(Shape):
    def __init__(self, h: int, w: int):
        self._h = h
        self._w = w
    
    @property
    def h(self, h: int):
        self._h = h 
    
    @property
    def w(self, w: int):
        self._w = w 

    def area(self) -> int:
        return self._h * self._w
    
    def draw(self) -> None:
        print("Draw Rectangle")

class Square (Shape):
    def __init__(self, h: int):
        self._h = h
        
    @property
    def h(self, h: int):
        self._h = h 

    def area(self) -> int:
        return self._h * self._h
    
    def draw(self) -> None:
        print("Draw Square ")

class Circle(Shape):
    def __init__(self, r: int):
        self._r = r
        
    @property
    def h(self, r: int):
        self._r = r 

    def area(self) -> int:
        return 3.14 * self._r * self._r
    
    def draw(self) -> None:
        print("Draw Circle")

class ShapeFactory(object):
    def getShape(self, format: str, *args) -> str:
        shape = self._getShape(format)
        return shape(args[0]) if len(args) == 1 else shape(args[0],args[1])

    def _getShape(self, shapeType: str):
        if shapeType == "Rectangle":
            return Rectangle
        elif shapeType == "Square":
            return Square
        elif shapeType == "Circle":
            return Circle
        else:
            raise ValueError(shapeType)

if __name__ == '__main__':
    #Initialize the factory
    shapeFactory = ShapeFactory()
    #create different shapes
    shape = shapeFactory.getShape("Circle", 5)
    print(shape.area())
    shape = shapeFactory.getShape("Rectangle", 2, 3)
    print(shape.area())
    shape = shapeFactory.getShape("Square", 1)
    print(shape.area())
