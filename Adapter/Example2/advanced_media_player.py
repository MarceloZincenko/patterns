from abc import ABCMeta, abstractmethod

class AdvancedMediaPlayer(object, metaclass = ABCMeta):
    
    @abstractmethod
    def playVlc(self, filename: str) ->None:
        pass

    @abstractmethod
    def playMp4(self, filename: str) ->None:
        pass
