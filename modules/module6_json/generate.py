from faker import Faker
import json
from datetime import timedelta, datetime

# Complete the following five methods. Remember, DRY by using abstraction and
# encapsulation to your advantage.

def get_top_artist_names(limit):
    pass

def get_artist_genres(artist):
    pass

def get_album_names(artist):
    pass

def get_album_songs(artist, album):
    pass

def get_song_duration(artist, song_name):
    pass

# END OF METHODS TO COMPLETE
# Everything below here simply calls the above methods to make a file

def create_release_date():
    return Faker().date_time_between(start_date='-30y', end_date='now')

def get_song(artist_name, song_name):
    return {
        "name": song_name,
        "duration": get_song_duration(artist_name, song_name),
        "release_date": create_release_date()
    }

def get_album(artist_name, album_name):
    return {
        "title": album_name,
        "release_date": create_release_date(),
        "songs": [get_song(artist_name, n) for n in get_album_songs(artist_name, album_name)]
    }

def get_artist(artist_name):
    create_member = Faker().name
    return {
        "name": artist_name,
        "genres": get_artist_genres(artist_name),
        "members": [create_member() for _ in range(3)],
        "albums": [get_album(artist_name, n) for n in get_album_names(artist_name)]
    }

def get_store(artist_limit):
    return [get_artist(n) for n in get_top_artist_names(artist_limit)]

def main():
    store = get_store(10)
    def converter(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, timedelta):
            return str(obj)
    with open('store.json', 'w') as fp:
        json.dump(store, fp, default = converter, indent=2)

if __name__=="__main__":
    main()