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

@app.route("/api/v1/resources/users/all", methods=['GET', 'POST'])
def api_all():
    if request.method == 'POST':
        json_data = flask.request.json
        users.append(json_data)
        return json_data
    else: 
        return jsonify(users)

@app.route("/api/v1/resources/users/<int:id>", methods=['GET'])
def api_id(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return 'Error, non-correct id passed', 400



@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'