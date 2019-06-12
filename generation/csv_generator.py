from random_utils import *
import csv

def get_album(words, songs_table):
    songs = random.sample(songs_table.keys(), random.randint(1,20))
    return {
        "title": get_title(words),
        "release_date": get_date(before = min([songs_table[s]["release_date"] for s in songs])),
        "songs": songs
    }

def get_artist(words, genres_table, members_table, albums_table):
    return {
        "name": get_title(words),
        "genres": random.sample(genres_table.keys(), random.randint(3,5)),
        "members": random.sample(members_table.keys(), random.randint(1,5)),
        "albums": random.sample(albums_table.keys(), random.randint(1,10))
    }

def get_database(num_artists = 1000):
    words = load(common_words_url)
    genres_table = {i: {"name": genre} for i, genre in enumerate(load(genres_url))}
    members_table = {i: {"name": get_name()} for i in range(num_artists*3)}
    songs_table = {i: get_song(words) for i in range(num_artists*50)}
    albums_table = {i: get_album(words, songs_table) for i in range(num_artists*5)}
    artists_table = {i: get_artist(words, genres_table, members_table, albums_table) for i in range(num_artists)}
    return {
        "genres": genres_table,
        "members": members_table,
        "songs": songs_table,
        "albums": albums_table,
        "artists": artists_table
    }

def save_table_to_csv(table, key_field, non_key_fields, filepath):
    with open(filepath, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, [key_field] + non_key_fields, extrasaction='ignore')
        writer.writeheader()
        for key, row in table.items():
            writer.writerow(dict({key_field: key}, **row))

def save_relationship_table_to_csv(table, parent_field, child_field, filepath):
    with open(filepath, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, [parent_field, child_field], extrasaction='ignore')
        writer.writeheader()
        for parent in table:
            for child in table[parent][child_field]:
                writer.writerow({parent_field: parent, child_field: child})
    
def save_csv(database, root = ''):
    base_specs = [
        ("genres", ["name"]),
        ("members", ["name"]),
        ("songs", ["name", "duration", "release_date"]),
        ("albums", ["title", "release_date"]),
        ("artists", ["name"])
    ]
    for table_name, fields in base_specs:
        save_table_to_csv(database[table_name], "key", fields, f"{root}{table_name}.csv")
    
    relationship_specs = [
        ("albums", "songs"),
        ("artists", "genres"),
        ("artists", "members"),
        ("artists", "albums")
    ]
    for parent_name, child_name in relationship_specs:
        save_relationship_table_to_csv(database[parent_name], parent_name, child_name, f"{root}{parent_name}_x_{child_name}.csv")
    
if __name__=="__main__":
    database = get_database(int(input("Enter the number of artists to generate: ")))
    save_csv(database, input("Enter the path of the directory to store results in: "))

        
