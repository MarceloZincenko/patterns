from abc import ABCMeta, abstractmethod

class Shape(object, metaclass = ABCMeta):
    @abstractmethod
    def draw(self) -> None:
        pass
