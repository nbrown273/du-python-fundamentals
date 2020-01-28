from json import dumps

class Artist():

    def __init__(self, name, genres=None, members=None, albums=None):
        self.name = name
        self.genres = [] if genres is None else genres
        self.members = [] if members is None else members
        if albums is None:
            self.albums = []
        else:
            self.albums = albums

    def countAlbums(self):
        return len(self.albums)
    
    def __str__(self):
        return dumps({
            "name": self.name,
            "genres": self.genres,
            "members": self.members,
            "albums": self.albums
        }, indent=2)