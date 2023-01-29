from flask import Flask, abort, send_file
from flask_cors import CORS
from infodb import AnimeList
import warnings

warnings.filterwarnings("ignore", message="specific warning message")

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

infos = AnimeList()

@app.route('/partial_name/<string:name>')
def anime_name(name):
    if(name is None):
        abort(404)
    return {
        "datas": infos.search_partial_name(name)
    }

@app.route('/similar_animes/<int:anime_id>')
def similar_name(anime_id):
    current_info = infos.get_info(anime_id)
    similar_animes = infos.similar_animes(anime_id)
    if((anime_id is None) | (current_info is None) | (similar_animes is None)):
        abort(404)
    return{
        "datas": {
            "current_info": current_info,
            "similar_animes": similar_animes
        }
    }

@app.route('/image/<int:anime_id>')
def image(anime_id):
    if(anime_id is None): abort(404)
    try:
        return send_file(f"images/covers/{anime_id}.jpg", mimetype='image/jpg')
    except FileNotFoundError:
        return 'Image not found', 404


@app.route('/get_info/<int:anime_id>')
def get_info(anime_id):
    getInfo = infos.get_info(anime_id)
    if((getInfo is None) | (anime_id is None)): abort(404)
    return {
        "datas": getInfo
    }


@app.route('/genre_lists/')
def genre_lists():
    return{
        "datas": infos.get_genre_list()
    }

@app.route('/get_anime_match_genre/<string:genre_selected>')
def get_anime_match_genre(genre_selected):
    anime_match_genre = infos.get_anime_match_genre(genre_selected)
    if(anime_match_genre is None): abort(404)
    return{
        "datas": anime_match_genre
    }

if __name__ == "__main__":
    # print(infos.get_genre_list())
    app.run(debug=True)