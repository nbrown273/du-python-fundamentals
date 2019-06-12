from random_utils import *
import json

def get_album(words):
    songs = [get_song(words) for i in range(random.randint(1, 20))]
    return {
        "title": get_title(words),
        "release_date": get_date(before = min([s["release_date"] for s in songs])),
        "songs": songs 
    }

def get_artist(words, genres, name_lambda):
    return {
        "name": get_title(words),
        "genres": random.sample(genres, random.randint(3,5)),
        "members": [name_lambda() for x in range(random.randint(1, 5))],
        "albums": [get_album(words) for i in range(random.randint(1,10))]
    }

def get_artists(num_artists=1000):
    words = load(common_words_url)
    genres = load(genres_url)
    return [get_artist(words, genres, get_name) for i in range(num_artists)]

def save_json(artists, root = ''):
    def converter(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, timedelta):
            return str(obj)
    with open(root + 'store.json', 'w') as fp:
        json.dump(artists, fp, default=converter, indent=4)
    
if __name__=="__main__":
    artists = get_artists(int(input("Enter the number of artists to generate: ")))
    save_json(artists, input("Enter the path of the directory to store results in: "))

