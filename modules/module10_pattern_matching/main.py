"""
TODO: Write a function "filterSongs" that loops through passed in albums and
      their songs, applies various filters, and returns a list of songs that
      pass all the applied filters:
    * Function should take in a parameter "albums", whose value is a list of
      Album objects
        - There needs to be at least 1 Album in the "albums" list parameter
    * Function should take in a parameter "name", that is used to filter based
      on the name of a song.
        - Should the value of "name" be None, the filter will not be applied
        - Should the value of "name" be a str, the filter will be passed if
          the value, case insensitive, of "name" is present in the song's name
    * Function should take in a parameter "minDuration", that is used to filter
      based on the duration of a song.
        - Should the value of "minDuration" be None, the filter will not be
          applied
        - Should the value of "minDuration" be an int, the filter will be
          passed if the value of "minduration" is less than or equal to the
          song's duration
    * Function should take in a parameter "maxDuration", that is used to filter
      based on the duration of a song.
        - Should the value of "maxDuration" be None, the filter will not be
          applied
        - Should the value of "maxDuration" be an int, the filter will be
          passed if the value of "maxDuration" is greater than or equal to the
          song's duration
    * Function should take in a parameter "minReleaseDate", that is used to
      filter based on the release_date of a song.
        - Should the value of "minReleaseDate" be None, the filter will not be
          applied
        - Should the value of "minReleaseDate" be an int, the filter will be
          passed if the value of "minReleaseDate" is less than or equal to the
          song's release_date
    * Function should take in a parameter "maxReleaseDate", that is used to
      filter
      based on the duration of a song.
        - Should the value of "maxReleaseDate" be None, the filter will not be
          applied
        - Should the value of "maxReleaseDate" be an int, the filter will be
          passed if the value of "maxReleaseDate" is greater than or equal to
          the song's release_date
    * Function should return a list of Song objects that pass all the filters
      applied
        - Should no songs pass all applied filters, an empty list should be
          returned
"""

from album import Album
from artist import Artist
from song import Song
from datetime import timedelta, datetime
from csv import DictReader

def read_content(filename):
    with open(filename, newline='') as fp:
        reader = DictReader(fp)
        return list(reader)

def create_object(record, constructor):
    if 'release_date' in record:
        record['release_date'] = datetime.fromisoformat(record['release_date'])
    if 'duration' in record:
        h, m, s = record['duration'].split(':')
        record['duration'] = timedelta(hours = int(h), minutes = int(m), seconds = int(s))
    if 'key' in record:
        record = {k:v for k,v in record.items() if k != "key"}
    return constructor(**record)

def init_objects(type_specs):
    database = {}
    for t, c in type_specs:
        data = read_content(f'../../data/faked/{t}.csv')
        lookup = {record['key']: create_object(record, c) for record in data}
        database[t] = lookup
    return database

def add_relationships(database, relationship_types):
    for parent_type, child_type in relationship_types:
        data = read_content(f'../../data/faked/{parent_type}_x_{child_type}.csv')
        for relationship in data:
            parent_key = relationship[parent_type]
            child_key = relationship[child_type]
            parent = database[parent_type][parent_key]
            parent.__getattribute__(child_type).append(child_key)

def load():
    def name_constructor(name):
        return name
    database = init_objects([
        ('artists', Artist), 
        ('albums', Album), 
        ('songs', Song), 
        ('genres', name_constructor),
        ('members', name_constructor)
    ])
    add_relationships(database, [
        ('artists', 'albums'), 
        ('artists', 'genres'), 
        ('artists', 'members'), 
        ('albums', 'songs')
    ])
    return database

# another possible abstraction: utility for compiling stats as a human readable string. 
# This example works for objects of type artist and album.
def get_stats(x, indent = 0):
    stats = '\t'*indent
    if isinstance(x, Artist):
        stats += 'Artist: {}, # of Albums: {}'.format(x.name, len(x.albums))
    elif isinstance(x, Album):
        stats += 'Album: "{}", # of Songs: {}'.format(x.title, x.countSongs())
    return stats

# second of two steps: accepts a list of artists and performs some analysis (for now, just prints object stats)
def analyze(database):
    for artist in database['artists'].values():
        print(get_stats(artist))
        for album in artist.albums:
            print(get_stats(database['albums'][album], indent = 1))

# main program: load then analyze the music collection
if __name__=="__main__":
    database = load()
    analyze(database)
