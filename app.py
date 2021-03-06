import os
from flask import Flask, jsonify
from database import db
from actors import actors
from movies import movies
from flask_cors import CORS
from auth import AuthError

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(actors, url_prefix='/actors')
app.register_blueprint(movies, url_prefix='/movies')
db.init_app(app)


@app.route('/')
def health_check():
    return jsonify({
        "message": 'Healthy',
        "success": "true"
    }), 200


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "message": "bad request"
    }), 404


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "message": "unauthorized"
    }), 404


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "message": "forbidden"
    }), 404


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "message": "resource not found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "message": "method not allowed"
    }), 405


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "message": "unprocessable"
    }), 422


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "message": "internal server error (see logs)"
    }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "message": error.error
    }), error.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
