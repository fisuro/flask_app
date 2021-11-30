from os import read, write
from flask import Flask, request, jsonify, render_template
import flask
import json
from jsonschema import validate
import jsonschema
from flask_ngrok import run_with_ngrok



app = Flask(__name__)
app.config["DEBUG"] = True
# run_with_ngrok(app)

#Loading schema to a variable
def load_schema():
    with open('schema.json') as f:
        schema = json.load(f)
    return schema
#This function goes trough the keys(id's) inside users file and get's the last id, then parses it to int, adds a counter and returns the new ID as a string
def get_index():
    index = int((list(load_users().keys()))[-1]) + 1
    return str(index)
    
#Reading users data from json file and storing them as variable
def load_users():
    with open('users.json') as f:
        json_object = json.load(f)
    return json_object

#This helper function is writing the the whole dict to a file
def write_to_file(file, object):
    with open(file, 'w') as writefile:
        writefile.write(object)

def add_user(data):
    json_object = load_users()
    index = get_index()
    json_object[index] = data
    write_to_file('users.json', json.dumps(json_object))
    return json_object[index]

#Function for validation json data sent by POST request with catching exception
#And iretates trough the existing users comparing the emails returning only true if
#A the JSON schema is right and there is no user with the same ID
def validate_json(to_validate):
    schema = load_schema()
    try:
        validate(instance=to_validate, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return "Bad request", 400

    json_object = load_users()
    for user in json_object:
        if json_object[user]['email'] == to_validate['email']:
            return "Email already in use", 406
    return "Success"
 
#Defining route for reading and adding users 
@app.route("/users", methods=['GET'])
def api_all():
    return jsonify(load_users())

@app.route("/users", methods=['POST'])
def post_user():
    if(validate_json(request.json) == "Success"):
        return add_user(request.json)
    else: 
        return validate_json(request.json)

@app.route("/users/<string:id>", methods=['GET'])
def get_user(id):
    json_object = load_users()
    if id in json_object.keys():
        return render_template('user.html', data = json_object[id])
    else: 
        return 'Error, non-correct id passed', 400

@app.route("/users/<string:id>", methods=['DELETE'])
def delete_user(id):
    json_object = load_users()
    if id in json_object.keys():
        json_object.pop(id)
        write_to_file('users.json', json.dumps(json_object))
        return 'Success', 200
    else:
        return 'Error, non-correct id passed', 400

@app.route("/users/<string:id>", methods=['PUT'])
def update_user(id):
    json_object = load_users()
    if id in json_object.keys():
        json_object[id] = {
            "name":request.json['name'],
            "surname":request.json['surname'],
            "email": json_object[id]['email']
        }
        write_to_file('users.json', json.dumps(json_object))
        return json_object
    else:
        return 'Error, non-correct id passed', 400

@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()