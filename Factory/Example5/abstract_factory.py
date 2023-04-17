import abc
import pygame

class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        raise NotImplementedError()
    
    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'left':
            self.x -= 4
        elif direction == 'right':
            self.x += 4

class Square(Shape):
    def draw(self):
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            pygame.Rect(self.x, self.y, 20, 20)
            )
        
class Circle(Shape):
    def draw(self):
        pygame.draw.circle(
            screen,
            (0, 255, 255),
            (self.x, self.y),
            10
            )
        
class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def make_object(self):
        return

class CircleFactory(AbstractFactory):
    def make_object(self):
        return Circle(100, 100)

class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square(100, 100)

def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()

def prepare_client():
    squareFactory = SquareFactory()
    draw_function(squareFactory)
    circleFactory = CircleFactory()
    draw_function(circleFactory)

if __name__ == '__main__':
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)
    prepare_client()
    pygame.display.flip()