

class Artist():

    def __init__(self, name, genres, members, albums=None):
        self.name = name
        self.genres = genres
        self.members = members
        if albums is None:
            self.albums = []
        else:
            self.albums = albums

    def count_songs(self):
        count = sum([len(album.songs) for album in self.albums])  # opportunity to demonstrate list comprehension AND/OR composition?
        return count
