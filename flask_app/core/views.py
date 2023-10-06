from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from core import app
from core.db_functions import (
    load_all_users_db,
    validate_json,
    add_user_db,
    find_user_db,
    authenication,
    update_user_db,
    delete_user_db,
    add_post,
    get_all_posts,
    edit_post_id,
)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    id = authenication(request.json)
    if id:
        access_token = create_access_token(identity=id)
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401


@app.route("/users", methods=["GET"])
@jwt_required()
def api_all():
    return load_all_users_db()


@app.route("/users", methods=["POST"])
# @jwt_required()
def post_user():
    if validate_json(request.json):
        return add_user_db(request.json)
    else:
        return "Bad request", 400


@app.route("/users/<int:id>", methods=["GET"])
# @jwt_required()
def get_user(id):
    user = find_user_db(id)
    if user:
        return user
    else:
        return "Error, non-correct id passed", 400


@app.route("/users/current", methods=["GET"])
@jwt_required()
def get_current_user():
    user = find_user_db(get_jwt_identity())
    if user:
        return user
    else:
        return "Error, non-correct id passed", 400


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    return delete_user_db(id)


@app.route("/users/<int:id>", methods=["PATCH"])
def update_user(id):
    return update_user_db(id, request.json)


@app.route("/posts", methods=["POST"])
@jwt_required()
def create_post():
    data = request.json
    return add_post(data, get_jwt_identity())


@app.route("/posts", methods=["GET"])
@jwt_required()
def get_posts():
    return get_all_posts()


@app.route("/posts/<int:id>", methods=["PATCH"])
@jwt_required()
def edit_post(id):
    data = request.json
    return edit_post_id(data, id, get_jwt_identity())


@app.route("/healtcheck", methods=["GET"])
def healtcheck():
    return "Is healty"


@app.route("/", methods=["GET"])
def index():
    return "Index"
