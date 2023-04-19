from media_player import MediaPlayer
from advanced_media_player import AdvancedMediaPlayer
from vlc_player import VlcPlayer
from mp4_player import Mp4Player

class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str) -> None:
        self.advancedMusicPlayer = self.media_adapter(audio_type)
    
    def media_adapter(self, audio_type: str) -> AdvancedMediaPlayer:
        if audio_type == "vlc":
            return VlcPlayer()
        elif audio_type == "mp4":
            return Mp4Player()

    def play(self, audio_type: str, filename: str) -> None:
        if audio_type == "vlc":
            self.advancedMusicPlayer.playVlc(filename) 
        elif audio_type == "mp4":
            self.advancedMusicPlayer.playMp4(filename)