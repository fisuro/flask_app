from core import app
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String
from typing import List
from flask_bcrypt import Bcrypt


# import uuid


# db = SQLAlchemy(app)
# class Base(DeclarativeBase):
#     pass


# db = SQLAlchemy(model_class=Base)

db = SQLAlchemy()
bcrypt = Bcrypt(app)


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    posts: Mapped[List["Posts"]] = relationship(
        back_populates="user", cascade="all, delete"
    )


class Posts(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    post: Mapped[str] = mapped_column(String)
    user: Mapped["User"] = relationship(back_populates="posts")

    # def __init__(self, first_name, last_name, email, password):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.password = password

    # def json(self):
    #     return {
    #         "id": self.id,
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "email": self.email,
    #         "password": self.password,
    #     }

    # def find_by_id(user_id):
    #     return db.session.execute(
    #         db.select(User.id, User.first_name, User.last_name, User.email).where(
    #             User.id == user_id
    #         )
    #     ).all()

    # @classmethod
    # def find_by_email(cls, user_email):
    #     return cls.query.filter_by(email=user_email).all()

    # def return_users():
    #     return db.session.execute(
    #         db.select(User.id, User.first_name, User.last_name, User.email)
    #     ).all()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # def commit_user(self):
    #     db.session.commit()
