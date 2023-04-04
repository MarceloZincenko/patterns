class Shape:
    def draw(self) -> None:
        pass

class Rectangle(Shape):
    def draw(self) -> None:
        print("Draw Rectangle")

class Square (Shape):
    def draw(self) -> None:
        print("Draw Square ")

class Circle(Shape):
    def draw(self) -> None:
        print("Draw Circle")

class ShapeFactory(object):
    def getShape(self, shapeType: str):
        if shapeType == "Rectangle":
            return Rectangle()
        elif shapeType == "Square":
            return Square()
        elif shapeType == "Circle":
            return Circle()
        else:
            return None

if __name__ == '__main__':
    #Initialize the factory
    shapeFactory = ShapeFactory()
    #create different shapes
    shape = shapeFactory.getShape("Circle")
    shape.draw()
    shape = shapeFactory.getShape("Rectangle")
    shape.draw()
    shape = shapeFactory.getShape("Square")
    shape.draw()
