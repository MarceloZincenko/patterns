import abc
from item import Item
from wrapper import Wrapper

class Burger(Item):
    __metaclass__ = abc.ABCMeta
    
    def packing(self) -> str:
        return Wrapper()
    
    @abc.abstractclassmethod
    def price(self) -> float:
        return
