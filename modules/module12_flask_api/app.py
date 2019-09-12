import main
from flask import request
from flask_api import FlaskAPI


# Initialize the Flask App
app = FlaskAPI(__name__)


# Load the database
db = main.load()


# Set up what to do at 'root' endpoint
@app.route("/", methods=["GET"])
def home():
    return {
        "routes": {
            "/": "Root, shows list of available routes",
            "/artist": "Return a randomly chosen Artist info",
            "/album": "Return a specified Album info",
            "/song": "Return a randomly chose Song info or Add a song to the database"
        }
    }


"""
# TODO: Write a route to return an artist
    Route will return a random artist from the database
        * Route should be '/artist'
        * If request method is GET:
            * A random artist should be chosen from the database
            * A JSON response should be returned that contains:
                - Artist's name, genres, members, and album's titles
"""


"""
# TODO: Write a route to return an album
    Route will return a specified album from the database
        * Route should be '/album/artist=<artistid>&album=<albumid>'
        * If request method is GET:
            * If artists <artistid> exists in the database:
                * If albums <albumid> exists in the artist object:
                    * A JSON response should be returned that contains:
                        - Artist's name who made album, album's title,
                        album's release data, and song's names
                * If albums <albumid> doesn't exist in the artist object:
                    * A JSON response should be returned with an error message
                    * Message should say:
                        - "Album <albumid> does not exist in Artist <artistid>"
            * If artists <artistid> doesn't exist in the database:
                * A JSON response should be returned with an error message
                * Message should say:
                    - "Artist <id> does not exist in database"

Hint: You can make use if the request.args.to_dict() method
"""


"""
# TODO: Write a route to return a Song
    Route will return a randomly chosen song from a randomly chosen album
    from a randomly chosen artist, or add a song to the database based on
    passed in data
    * Route should be '/song'
    * If request method is GET:
        * A random artist will be chosen from the database
        * A random album will be chosen from the artist
        * A random song will be chosen from the album
        * A JSON response should be returned that contains:
            - Artist's name, album's title, song's name, song's duration,
              and song's release data
    * If request method is POST:
        * Request's Data Format:
            {
                "artistID": <artistid>,
                "albumID": <albumid>,
                "name": <songname>,
                "duration": <songduration>,
                "releasedata": <songreleasedate>
            }
        * If <artistid> exists in database:
            * If <albumid> exists in artist object:
                * A new Song object should be created based on <songname>, <songduration>,
                  and <songreleasedate>
                * Song should be added to the Artist's <artistid> Album's <albumid> songs
                * A JSON response should be returned with a success message
                * Message should say:
                    - "Song added to Album <albumid> by Artist <artistid>
            * If <albumid> doesn't exist in artist object:
                * A JSON response should be returned with an error message
                * Message should say:
                    - "Album <albumid> does not exist in Artist <artistid>"
        * If <artistid> doesn't exist in database:
            * A JSON response should be returned with an error message
            * Message should say:
                - "Artist <artistid> does not exist in database"
"""


if __name__ == "__main__":
    app.run()