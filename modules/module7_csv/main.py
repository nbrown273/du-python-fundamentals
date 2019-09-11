from album import Album
from artist import Artist
from song import Song
from datetime import timedelta, datetime
import json

# used to map every dictionary in the store JSON to an instance of a music class
def hook(dct):
    # first step is to decide which class to decode the dictionary as,
    # here we use unique field names to identify the class
    if "duration" in dct:
        return decode_song(**dct)
    elif "release_date" in dct:
        return decode_album(**dct)
    else:
        return decode_artist(**dct)

# create a song object after decoding the duration and release date from string representations
def decode_song(name, duration, release_date):
    h, m, s = [int(x) for x in duration.split(":")]
    duration = timedelta(hours = h, minutes = m, seconds = s)
    release_date = datetime.fromisoformat(release_date)
    return Song(name, duration, release_date)

# create an album object after decoding the release date from the string ISO format
# NOTE: songs have already been decoded at this point
def decode_album(title, release_date, songs):
    release_date = datetime.fromisoformat(release_date)
    return Album(title, release_date, songs)

# create an artist object simply by passing in the (decoded) arguments as is.
def decode_artist(**kwargs):
    return Artist(**kwargs)

# first of two steps: load/construct all the music related objects and define their relationships.
def load(source):
    with open(source, 'r') as fp:
        # object hook gets called on each dictionary mapped from the JSON in fp.
        return json.load(fp, object_hook=hook)

# another possible abstraction: utility for compiling stats as a human readable string. 
# This example works for objects of type artist and album.
def get_stats(x, indent = 0):
    stats = '\t'*indent
    if isinstance(x, Artist):
        stats += 'Artist: {}, # of Songs: {}'.format(x.name, x.countSongs())
    elif isinstance(x, Album):
        stats += 'Album: "{}", # of Songs: {}, Total Duration: {}'.format(x.title, x.countSongs(), x.totalDuration())
    return stats

# second of two steps: accepts a list of artists and performs some analysis (for now, just prints object stats)
def analyze(artists):
    for artist in artists:
        print(get_stats(artist))
        for album in artist.albums:
            print(get_stats(album, indent = 1))

# main program: load then analyze the music collection
if __name__=="__main__":
    artists = load(input("Enter json file path:"))
    analyze(artists)
