from flask import Flask, request, jsonify

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

    results = []

    for user in users:
        if user['id'] == id:
            results.append(user)

    return jsonify(results)

@app.route("/healtcheck", methods=['GET'])
def healtcheck():
    return 'Is healty'