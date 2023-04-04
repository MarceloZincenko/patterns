import json
import xml.etree.ElementTree as et

class Song(object):
    """Creates a song instance"""
    def __init__(self, song_id: str, title: str, artist: str) -> None:
        self._song_id = song_id
        self._title = title
        self._artist = artist
    
    @property
    def song_id(self) -> None:
        return self._song_id
    
    @property
    def title(self) -> None:
        return self._title
    
    @property
    def artist(self) -> None:
        return self._artist

class SongSerializer(object):
    """The code converts a song object to its string representation using a different format in each logical path."""
    #Client method
    def serialize(self, song: Song, format: str) -> str:
        serializer = self._get_serializer(format)
        return serializer(song)
    
    #Creator method
    def _get_serializer(self, format: str) -> str:
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)
    
    #Product method
    def _serialize_to_json(self, song: Song) -> str:
        song_info = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(song_info)
    
    #Product method
    def _serialize_to_xml(self, song: Song) -> str:
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')

# main 
if __name__ == "__main__":
    #Intialize a song
    song = Song('1', 'Water of Love', 'Dire Straits')
    #intialize SongSerializer
    serializer = SongSerializer()
    #make json
    print(serializer.serialize(song, 'JSON'))