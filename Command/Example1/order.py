from abc import ABCMeta, abstractmethod

class Order(object, metaclass = ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass