import abc

class Packing(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def pack(self) -> str:
        return