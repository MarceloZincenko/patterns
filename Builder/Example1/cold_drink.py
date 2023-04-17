import abc
from item import Item
from bottle import Bottle

class ColdDrink (Item):
    __metaclass__ = abc.ABCMeta
    
    def packing(self) -> str:
        return Bottle()
    
    @abc.abstractclassmethod
    def price(self) -> float:
        return
