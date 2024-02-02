from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #referring user table(calling it by small first letter because db have lowecase representations of tables)

class User(db.Model ,UserMixin):

    #this is my simple schema

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    tasks = db.relationship('Task')
    #this is actually one to many relationship <a user can have many tasks>

