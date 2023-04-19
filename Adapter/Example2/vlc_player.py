from advanced_media_player import AdvancedMediaPlayer

class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self, filename: str) -> None:
        print(f"Playing VLC filename:{filename}")
    
    def playMp4(self, filename: str) -> None:
       pass