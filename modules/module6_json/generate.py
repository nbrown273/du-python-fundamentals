import os
from requests import get
from faker import Faker
import json
from datetime import timedelta, datetime

def load(method, **params):
    params["api_key"] = os.environ.get("API_KEY")
    params["format"] = "json"
    params["method"] = method
    return get("http://ws.audioscrobbler.com/2.0/", params).json()

def get_top_artist_names(limit):
    response = load("chart.gettopartists", limit = limit)
    return [a["name"] for a in response["artists"]["artist"]]

def get_artist_genres(artist):
    response = load("artist.gettoptags", artist = artist)
    return [t["name"] for t in response["toptags"]["tag"]][:3]

def get_album_names(artist):
    response = load("artist.gettopalbums", limit = 3, artist = artist)
    return [a["name"] for a in response["topalbums"]["album"]]

def get_album_songs(artist, album):
    response = load("album.getinfo", artist = artist, album = album)
    return [t["name"] for t in response["album"]["tracks"]["track"]][:3]

def get_song_duration(artist, song_name):
    response = load("track.getinfo", artist = artist, track = song_name)
    return timedelta(milliseconds = int(response["track"]["duration"]))

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