from abc import ABCMeta, abstractmethod

class Game(object, metaclass = ABCMeta):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start_play(self):
        pass
    
    @abstractmethod
    def end_play(self):
        pass
    
    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()