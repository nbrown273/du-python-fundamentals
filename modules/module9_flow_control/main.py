"""
TODO: Write a function "listSongs" that loops through a passed in list of
      albums, and returns a list of songs, comprised of up to n songs from
      each album.
    * Function should take in a parameter "albums", whose value is a list of
      Album objects
        - There needs to be at least 1 Album object in the "albums" list
          parameter
    * Function should take in a parameter "n", where "n" in an int
        - Note that n > 0
    * Function should return a list of Songs objects
        - There can be up to "n" Song objects from any given Album
        - Should no Songs be found, an empty list should be returned
    * Function must use "continue"
"""

from album import Album
from artist import Artist
from song import Song
from datetime import timedelta, datetime
from csv import DictReader

def read_content(filename):
    try:
        with open(filename, newline='') as fp:
            reader = DictReader(fp)
            return list(reader)
    except FileNotFoundError e:
        print(f"Did not find file: {filename}")
        raise e

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
