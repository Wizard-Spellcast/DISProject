from datetime import date


class Artist(tuple):
    def __init__(self, artist_data):
        self.id:int = artist_data[0] # Primary key
        self.name:int = artist_data[1]
        self.albumsLink:int = artist_data[2]

class ArtistAlbumLink(tuple):
    def __init__(self, linkData):
        self.artistAlbumKey:int = linkData[0] # Primary key
        self.artistId:int = linkData[1]
        self.albumId:int = linkData[2]

class Genre(tuple):
    def __init__(self, genre_data):
        self.id:int = genre_data[0]
        self.name:int = genre_data[1]
        
class Album(tuple):
    def __init__(self, album_data):
        self.id:int = album_data[0] # Primary key
        self.name:str = album_data[1]
        self.artisLlink:int = album_data[2]
        self.genreLink:int = album_data[3]

class AlbumTrackLink(tuple):
    def __init__(self):
        self.albumTrackKey:int # Primary key
        self.albumId:int
        self.trackId:int

class Track(tuple):
    def __init__(self, track_data):
        self.id:int = track_data[0] # Primary key
        self.name:str = track_data[1]
        self.genre:str = track_data[2]
        self.genreLink:int = track_data[3]