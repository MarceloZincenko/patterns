from abc import ABCMeta, abstractmethod

class State(object, metaclass = ABCMeta):

    @abstractmethod
    def do_action(self) -> None:
        pass