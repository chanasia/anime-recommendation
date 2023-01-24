from flask import Flask, abort, send_file
from models import AnimeModels
from infodb import AnimeList
import warnings

warnings.filterwarnings("ignore", message="specific warning message")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
model = AnimeModels()
infos = AnimeList()

@app.route('/partial_name/<string:name>')
def anime_name(name):
    if(name is None):
        abort(404)
    return {
        "datas": model.search_partial_name(name)
    }

@app.route('/similar_animes/<int:id>')
def similar_name(id):
    if(id is None):
        abort(404)
    return{
        "datas": model.similar_animes(id)
    }

@app.route('/image/<int:image_id>')
def image(image_id):
    try:
        return send_file(f"images/covers/{image_id}.jpg", mimetype='image/jpg')
    except FileNotFoundError:
        return 'Image not found', 404


@app.route('/get_info/<int:anime_id>')
def get_info(anime_id):
    return {
        "datas": infos.get_info(anime_id)
    }


if __name__ == "__main__":
    app.run(debug=True)