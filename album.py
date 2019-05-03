from datetime import timedelta


class Album():

    def __init__(self, title, release_date, songs=None):
        self.title = title
        self.release_date = release_date
        if songs is None:
            self.songs = []
        else:
            self.songs = songs

    def __repr__(self):
        return self.title

    def count_songs(self):
        return len(self.songs)

    def totalDuration(self):
        time = sum([song.duration for song in self.songs], timedelta())
        return time
