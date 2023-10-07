from operator import itemgetter
from sre_constants import SUCCESS
from jsonschema import validate
from sqlalchemy import false
from core.models import User, Posts, bcrypt, db
import jsonschema
import json


def load_schema():
    with open("schema.json") as f:
        schema = json.load(f)
    return schema


def add_user_db(data):
    user = User.query.filter_by(email=data["email"]).first()
    if user:
        return "Error: Email already exists"
    else:
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=bcrypt.generate_password_hash(data["password"]).decode("utf-8"),
        )
    db.session.add(user)
    db.session.commit()
    return "success"


def load_all_users_db():
    list_of_users = []
    users = User.query.all()
    for user in users:
        list_of_users.append(
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "id": user.id,
            }
        )
    return list_of_users


def find_user_db(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "id": user.id,
        }
    return "User doesn't exist"


def delete_user_db(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return "Success"


def update_user_db(id, data):
    user = User.query.filter_by(id=id).first()
    if user:
        user.first_name, user.last_name = data["first_name"], data["last_name"]
        db.session.commit()
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "id": user.id,
        }
    return "user dosen't exist"


def validate_json(to_validate):
    schema = load_schema()
    try:
        validate(instance=to_validate, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def authenication(data):
    user = User.query.filter_by(email=data["email"]).first()
    if user:
        if bcrypt.check_password_hash(user.password, data["password"]):
            return user.id
    else:
        return False


def add_post(data, id):
    user = User.query.filter_by(id=id).first()
    post = Posts(post=data["post"], user=user)
    db.session.add(post)
    db.session.commit()
    return "success"


def get_all_posts():
    list_of_posts = []
    posts = Posts.query.all()
    for post in posts:
        list_of_posts.append(
            {
                "post_id": post.id,
                "poster": post.user.first_name,
                "post": post.post,
            }
        )
    return list_of_posts


def edit_post_id(data, id, user_id):
    post = Posts.query.filter_by(id=id).first()
    if post.user.id == user_id:
        post.post = data["post"]
        db.session.commit()
        return "success"
    return "error"
