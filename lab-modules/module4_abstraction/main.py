from album import Album
from artist import Artist
from song import Song
from datetime import timedelta, date

# create an artist
rhcp = Artist('Red Hot Chili Peppers', ['Rock'], ['Flea', 'Anthony Kiedis', 'Chad Smith', 'Josh Klinghoffer'])
print('Artist:', rhcp.name)

# create an album and add it to rhcp
rhcp.albums.append(Album('Stadium Arcadium', date(2006, 5, 9)))
print('Album:', rhcp.albums)

# add songs to the album
t1 = Song('Dani California', timedelta(minutes=4, seconds=42), date(2006, 5, 9))
t2 = Song('Snow (Hey Oh)', timedelta(minutes=5, seconds=34), date(2006, 5, 9))
t3 = Song('Charlie', timedelta(minutes=4, seconds=37), date(2006, 5, 9))

# this is messy imo, but necessary if data is stored in lists
# and you want to access a specific element
for a in rhcp.albums:
    if a.title == 'Stadium Arcadium':
        a.songs += [t1, t2, t3]

# print the # of songs and total duration for each album
for a in rhcp.albums:
    print('Album: "{}", # of Songs: {}, Total Duration: {}'.format(a.title, a.countSongs(), a.totalDuration()))
