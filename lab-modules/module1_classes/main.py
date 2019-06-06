class Album():

    def __init__(self):
        pass
        # TODO: define init state
            # accepts:
                # Title: string
                # Release Date: date
                # songs: list of Song items

    # TODO: define a count_songs() function
        # accepts: None
        # returns: Number of songs in the album (integer)


class Artist():

    def __init__(self, name, genres, members, albums=None):
        self.name = name
        self.genres = genres
        self.members = members
        if albums is None:
            self.albums = []
        else:
            self.albums = albums

    # TODO: define count_songs() function
        # accepts: None
        # returns: total number of songs on all albums by this artist (integer)
            # HINT: reuse the function by the same name defined in our Album class. DRY design principles.


class Song():

    def __init__(self, name, duration, release_date):
        self.name = name
        self.duration = duration
        self.release_date = release_date


# testing
# TODO: Instantiate an Artist, Album, and three Songs.
