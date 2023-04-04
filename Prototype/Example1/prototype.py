from abc import ABCMeta, abstractmethod
    
class Prototype(metaclass=ABCMeta):
    """The interface. Here we declarate the pure virtual function clone()"""
    @abstractmethod
    def clone(self):
        pass