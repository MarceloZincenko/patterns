from abc import ABCMeta, abstractmethod

class MediaPlayer(object, metaclass = ABCMeta):
    
    @abstractmethod
    def play(self, audioType: str, filename: str) ->None:
        pass