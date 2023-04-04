from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    """The interface. Here we declarate the pure virtual function clone() and draw()"""
    def __init__(self, id: str, tipo: str) -> None:
        self._id = id
        self._tipo = tipo

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def tipo(self)  -> str:
        return self._tipo
    
    @id.setter
    def id(self, id: str) -> None:
        self._id = id

    @tipo.setter
    def id(self, tipo: str) -> None:
        self._tipo = tipo
    
    @abstractmethod
    def draw(self) -> None:
        pass
    
    @abstractmethod
    def clone(self):
        pass