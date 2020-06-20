from flask import Blueprint, jsonify, request, abort
from models import Actor
from auth import requires_auth

actors = Blueprint('actors', __name__)


@actors.route('/')
@requires_auth('get:actors')
def get_actors():
    return jsonify({
        "actors": list(map(lambda actor: actor.format(), Actor.query.all())),
        "success": "true"
    }), 200


@actors.route('/', methods=['POST'])
@requires_auth('post:actors')
def post_actors():
    name = request.json.get("name")
    if name is None:
        abort(422)
    age = request.json.get("age")
    if age is None:
        abort(422)
    gender = request.json.get("gender")
    if gender is None:
        abort(422)

    actor = Actor(name=name, age=age, gender=gender)
    actor.insert()
    return jsonify({
        "actors": [actor.format()],
        "success": "true"
    }), 200


@actors.route('/<actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        abort(404)

    actor.delete()
    return jsonify({
        "actors": [actor.format()],
        "success": "true"
    }), 200


@actors.route('/<actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def patch_actors(actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if actor is None:
        abort(404)

    name = request.json.get("name")
    age = request.json.get("age")
    gender = request.json.get("gender")

    actor.update(name, age, gender)
    return jsonify({
        "actors": [actor.format()],
        "success": "true"
    }), 200
