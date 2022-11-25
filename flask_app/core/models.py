# from core import app
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.database import db_session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email
        }

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def find_by_email(cls, user_email):
        return cls.query.filter_by(email=user_email).first()

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()
    def delete_from_db(self):
        db_session.delete(self)
        db_session.commit()
    def commit_user(self):
        db_session.commit()