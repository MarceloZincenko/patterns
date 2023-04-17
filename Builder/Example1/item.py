import abc
from packing import Packing

class Item(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractclassmethod
    def name(self) -> str:
        return
    
    @abc.abstractclassmethod
    def packing(self) -> Packing:
        return
    
    @abc.abstractclassmethod
    def price(self) -> float:
        return