class Album():

    def __init__(self, title, release_date, songs=None):
        self.title = title
        self.release_date = release_date
        if songs is None:
            self.songs = []
        else:
            self.songs = songs

    def count_songs(self):
        return len(self.songs)


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
        count = 0
        for a in self.albums:
            count += a.count_songs()
        return count


class Song():

    def __init__(self, name, duration, release_date):
        self.name = name
        self.duration = duration
        self.release_date = release_date

# testing
# TODO: Using your objects created in module 1, assign the songs to the album, and the album to the artist.
# TODO: Call the count_songs() method of your Artist object and print the output.
