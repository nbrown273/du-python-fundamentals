class Song():

    def __init__(self, name, duration, release_date):
        self.name = name
        self.duration = duration
        self.release_date = release_date

    def __repr__(self):
        return self.name
