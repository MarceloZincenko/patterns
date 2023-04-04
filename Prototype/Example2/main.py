from concrete import ShapeCache 

def run():
    shapes = ShapeCache()
    circle = shapes.get_shape("circle", 3)
    rectangle = shapes.get_shape("rectangle", 2)
    square = shapes.get_shape("square", 1)
    circle.draw()
    rectangle.draw()
    square.draw()

if __name__ == '__main__':
    run()