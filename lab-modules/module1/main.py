class Album():

    def __init__(self):
        pass
        # TODO: define init state

        # TODO: define a count_songs() function


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
        # HINT: reuse the function by the same name defined in our Album class. DRY design principles.


class Song():

    def __init__(self, name, duration, release_date):
        self.name = name
        self.duration = duration
        self.release_date = release_date
