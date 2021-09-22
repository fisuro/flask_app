from flask import Flask, request, jsonify
import flask

app = Flask(__name__)
app.config["DEBUG"] = True

users = [
    { 
        "id":0,
        "name":"Filip",
        "surname":"Bjelic"
    },
    {
        "id":1,
        "name":"Aleksandar",
        "surname":"Vukovac"
    }
]

@app.route("/api/v1/resources/users/all", methods=['GET'])
def api_all():
    return jsonify(users)

@app.route("/api/v1/resources/users", methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id provided.", 400
    kita = []
    for i in users:
        if id == i["id"]:
            kita = i
    return kita

@app.route("/api/v1/resources/users", methods=['POST'])
def starting_url():
    json_data = flask.request.json
    users.append(json_data)
    return json_data

@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'