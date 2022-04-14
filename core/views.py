from flask import request, jsonify, render_template
from core import app
from core.db_functions import load_all_users_db, validate_json, add_user_db, find_user_db, delete_user_db, update_user_db

@app.route("/users", methods=['GET'])
def api_all():
    return jsonify(load_all_users_db())

@app.route("/users", methods=['POST'])
def post_user():
    if validate_json(request.json):
        return add_user_db(request.json)
    else:
        return "Bad request", 400

@app.route("/users/<int:id>", methods=['GET'])
def get_user(id):
    if find_user_db(id):
        return render_template('user.html', data = find_user_db(id))
    else:
        return 'Error, non-correct id passed', 400

@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    return delete_user_db(id)

@app.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    return update_user_db(id, request.json)

@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')