class Artist():

    def __init__(self, name, genres, members, albums=None):
        self.name = name
        self.genres = genres
        self.members = members
        if albums is None:
            self.albums = []
        else:
            self.albums = albums

    def countSongs(self):
        cnt = sum([len(album.songs) for album in self.albums]) 
        return cnt
