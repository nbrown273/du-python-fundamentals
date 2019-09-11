from album import Album
from artist import Artist
from song import Song
from datetime import timedelta, date

# one possible abstraction: utility for adding songs to album by title
# may be generalizing too early in practice...
def add_songs(artist, album_title, songs):
    for album in artist.albums:
        if album.title == album_title:
            album.songs += songs

# first of two steps: load/construct all the music related objects and define their relationships.
def load():
    # create an artist
    rhcp = Artist('Red Hot Chili Peppers', ['Rock'], ['Flea', 'Anthony Kiedis', 'Chad Smith', 'Josh Klinghoffer'])

    # create an album and add it to rhcp
    rhcp.albums.append(Album('Stadium Arcadium', date(2006, 5, 9)))

    # add songs to the album
    add_songs(rhcp, 'Stadium Arcadium', [
        Song('Dani California', timedelta(minutes=4, seconds=42), date(2006, 5, 9)),
        Song('Snow (Hey Oh)', timedelta(minutes=5, seconds=34), date(2006, 5, 9)),
        Song('Charlie', timedelta(minutes=4, seconds=37), date(2006, 5, 9))
    ])

    return [rhcp]

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
    artists = load()
    analyze(artists)
