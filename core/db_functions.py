from operator import itemgetter
from sqlalchemy import exc
from jsonschema import validate
import jsonschema
import json
from core.models import db, User

def load_schema():
    with open('schema.json') as f:
        schema = json.load(f)
    return schema

def add_user_db(data):
    try:
        user = User(name=data['name'], surname=data['surname'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return data
    except exc.IntegrityError:
        db.session.rollback()
        return "Error: Email already exists"

def load_all_users_db():
    table = User.query.all()
    list = []
    for row in table:
        list.append({column: str(getattr(row, column)) for column in row.__table__.c.keys()})
    return sorted(list, key = itemgetter('id'))

def find_user_db(id):
    user = User.query.filter(User.id == id).one()
    return {column: str(getattr(user, column)) for column in user.__table__.c.keys()}

def delete_user_db(id):
    User.query.filter(User.id == id).delete()
    db.session.commit()
    return 'Success'

def update_user_db(id, data):
    user = User.query.filter(User.id == id).one()
    user.name = data['name']
    user.surname = data['surname']
    db.session.commit()
    return {column: str(getattr(user, column)) for column in user.__table__.c.keys()}

def validate_json(to_validate):
    schema = load_schema()
    try:
        validate(instance=to_validate, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True