from flask import Flask, request, jsonify, render_template
import json
from jsonschema import validate
import jsonschema
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
# run_with_ngrok(app)

POSTGRESQL_URI = 'postgres://axnbpeci:rADWtHAG9X0UDVyrJyvenm8-uX4GjZmR@tyke.db.elephantsql.com/axnbpeci'
# POSTGRESQL_URI='postgres://postgres:mysecretpassword@postgres/postgres'
connection = psycopg2.connect(POSTGRESQL_URI)

try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE users (name VARCHAR(43), surname VARCHAR(43), email VARCHAR(43) UNIQUE NOT NULL, id SERIAL PRIMARY KEY);")
except psycopg2.errors.DuplicateTable:
    pass

#Loading schema to a variable
def load_schema():
    with open('schema.json') as f:
        schema = json.load(f)
    return schema

def add_user_db(data):
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO users (name, surname, email) VALUES ( %s, %s, %s)'
                val = (data['name'], data['surname'], data['email'])
                cursor.execute(sql, val)
        return data
    except psycopg2.errors.UniqueViolation:
        return "Error: Email already exists"

def load_all_users_db():
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM users ORDER BY id;")
            users = cursor.fetchall()
        return users

def find_user_db(id):
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute(f"SELECT * FROM users WHERE id = {id};")
            user = cursor.fetchall()
        return user

def delete_user_db(id):
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute(f"DELETE FROM users WHERE id = {id};")
        return 'Success'

def update_user_db(id, data):
    with connection:
        with connection.cursor() as cursor:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute(f"UPDATE users SET name='{data['name']}', surname='{data['surname']}' WHERE id = {id};")
            cursor.execute(f"SELECT * FROM users WHERE id = {id};")
            user = cursor.fetchall()
        return user

#Function for validation json data sent by POST request with catching exception
#And iretates trough the existing users comparing the emails returning only true if
#A the JSON schema is right and there is no user with the same ID
def validate_json(to_validate):
    schema = load_schema()
    try:
        validate(instance=to_validate, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return "Bad request", 400
    return "Success"
 
#Defining route for reading and adding users 
@app.route("/users", methods=['GET'])
def api_all():
    return jsonify(load_all_users_db())

@app.route("/users", methods=['POST'])
def post_user():
    validation_response = validate_json(request.json)
    if(validation_response == "Success"):
        return add_user_db(request.json)
    else: 
        return validation_response

@app.route("/users/<int:id>", methods=['GET'])
def get_user(id):
    if find_user_db(id):
        return render_template('user.html', data = find_user_db(id)[0])
    else:
        return 'Error, non-correct id passed', 400

@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    return delete_user_db(id)

@app.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    return jsonify(update_user_db(id, request.json)[0])

@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0', port=8080)