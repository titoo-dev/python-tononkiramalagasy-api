from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import tononkira_api


# create the flask app
app = Flask(__name__)

# creating api object
api = Api(app)

class Artists(Resource):
    def get(self, page):
        artists = tononkira_api.get_artists(page)
        return {'artists': artists}

class ArtistSong(Resource):
    def get(self, index, page):
        songs = tononkira_api.get_artist_songs(index, page)
        return {'songs': songs}

class Lyrics(Resource):
    def get(self, artist, title):
        lyrics = tononkira_api.get_lyrics(title, artist)
        return {'lyrics': lyrics}


api.add_resource(Artists, '/artists/<int:page>')
api.add_resource(ArtistSong, '/artists/<int:index>/songs/<int:page>')
api.add_resource(Lyrics, '/lyrics/<string:artist>/<string:title>')

if __name__ == '__main__':
    app.run(debug=True)