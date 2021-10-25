from os import read, write
from flask import Flask, request, jsonify
import flask
import json
from jsonschema import validate
import jsonschema


app = Flask(__name__)
app.config["DEBUG"] = True

#Defining JSON Schema
schema = {
    "type" : "object",
    "additionalProperties": False,
    "properties" : {
        "id" : {"type" : "number"},
        "name" : {"type" : "string"},
        "surname" : {"type" : "string"},
    },
    "required":["id", "name", "surname"]
}

#Reading users data from json file and storing them as variable
json_object = json.load(open('users.json'))

#Function for validation json data sent by POST request with catching exception
#And iretates trough the existing users comparing the Id's returning only true if
#A the JSON schema is right and there is no user with the same ID
def validate_json(to_validate):
    try:
        validate(instance=to_validate, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    for user in json_object:
        if user['id'] == to_validate['id']:
            return False
    return True
 

 #Defining route for reading and adding users 
@app.route("/users", methods=['GET', 'POST'])
def api_all():
    if request.method == 'POST':
        json_data = request.json
        #Calling a function to validate JSON, if JSON follows schema
        #Then the data from request is stored in variable, and then saved to a file
        if validate_json(json_data):
            #If JSON form is valid, data from request is added to the list
            json_object.append(json_data)
            to_write = json.dumps(json_object)
            #Whole list is then written to the file
            with open('users.json', 'w') as writefile:
                writefile.write(to_write)
            return json_data
        else: return "Bad request", 400
    else: 
        return jsonify(json_object)

@app.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def api_id(id):
    for user in json_object:
        if user['id'] == id:
            if request.method == 'DELETE':
                json_object.remove(user)
                to_write = json.dumps(json_object)
                with open('users.json', 'w') as writefile:
                    writefile.write(to_write)
                return 'Sucess', 203
            elif request.method == 'PUT':
                json_data = request.json
                if user['id'] == id:
                    if json_data['name']:
                        user['name'] = json_data['name']
                    if json_data['surname']:
                        user['surname'] = json_data['surname']
                    to_write = json.dumps(json_object)
                    with open('users.json', 'w') as writefile:
                        writefile.write(to_write)
                    return jsonify(user)
            else:    
                return jsonify(user)
    return 'Error, non-correct id passed', 400

@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'
