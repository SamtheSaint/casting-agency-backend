from flask import Blueprint, jsonify, request, abort
from models import Movie
import datetime
from auth import requires_auth


movies = Blueprint('movies', __name__)


@movies.route('/')
@requires_auth('get:movies')
def get_movies():
    return jsonify({
        "movies": list(map(lambda movie: movie.format(), Movie.query.all())),
        "success": "true"
    }), 200


@movies.route('/', methods=['POST'])
@requires_auth('post:movies')
def post_movies():
    title = request.json.get("title")
    if title is None:
        abort(422)
    date = request.json.get("date")
    if date is None:
        abort(422)

    print(title, date)
    date = datetime.date.fromisoformat(date)
    movie = Movie(title=title, date=date)
    movie.insert()
    return jsonify({
        "movies": [movie.format()],
        "success": "true"
    }), 200


@movies.route('/<movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)

    movie.delete()
    return jsonify({
        "movies": [movie.format()],
        "success": "true"
    }), 200


@movies.route('/<movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def patch_movies(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)

    title = request.json.get("title")
    date = request.json.get("date")
    if date is not None:
        date = datetime.date.fromisoformat(date)

    movie.update(title, date)
    return jsonify({
        "movies": [movie.format()],
        "success": "true"
    }), 200
