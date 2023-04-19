from advanced_media_player import AdvancedMediaPlayer

class Mp4Player(AdvancedMediaPlayer):
    def playVlc(self, filename: str) -> None:
        pass
    
    def playMp4(self, filename: str) -> None:
        print(f"Playing Mp4 filename:{filename}")