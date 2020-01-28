from json import dumps

class Song():

    def __init__(self, name, duration, release_date):
        self.name = name
        self.duration = duration
        self.release_date = release_date

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return dumps({
            "name": self.name,
            "duration": str(self.duration),
            "release_data": str(self.release_date)
        }, indent=4)
