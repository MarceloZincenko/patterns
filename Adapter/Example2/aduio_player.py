from media_player import MediaPlayer
from media_adapter import MediaAdapter

class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, filename: str) -> None:
        if audio_type == "mp3":
            print(f"playing {audio_type} {filename}")
        elif audio_type == "vlc" or audio_type == "mp4":
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, filename)
        else:
            print("Invalid media. " + audio_type + " format not supported")