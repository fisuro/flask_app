from operator import itemgetter
from jsonschema import validate
import jsonschema
import json
from core.models import User

def load_schema():
    with open('schema.json') as f:
        schema = json.load(f)
    return schema

def add_user_db(data):
    if User.find_by_email(data['email']):
        return "Error: Email already exists"
    user = User(data['name'], data['surname'], data['email'])
    user.save_to_db()
    return data

def load_all_users_db():
    table = User.query.all()
    list = []
    for user in table:
        list.append(user.json())
    return sorted(list, key = itemgetter('id'))

def find_user_db(id):
    return User.find_by_id(id).json()

def delete_user_db(id):
    User.find_by_id(id).delete_from_db()
    return 'Success'

def update_user_db(id, data):
    user = User.find_by_id(id)
    user.name = data['name']
    user.surname = data['surname']
    user.commit_user()
    return user.json()

def validate_json(to_validate):
    schema = load_schema()
    try:
        validate(instance=to_validate, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True