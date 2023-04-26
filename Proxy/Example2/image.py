from abc import ABCMeta, abstractmethod

class Image(object, metaclass = ABCMeta):

    @abstractmethod
    def display(self) -> None:
        pass