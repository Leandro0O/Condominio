import email
from enum import unique
from main import db, login_sindico
from flask_login import UserMixin


@login_sindico.user_loader
def sindico_load(user_id):
    return Sindico.query.get(user_id)


class Sindico(db.Model, UserMixin):

    __tablename__ = "Sindico"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45),unique=False)
    usuario = db.Column(db.String(45),unique=True)
    email = db.Column(db.String(45),unique=False)
    tel = db.Column(db.String(20),unique=False)
    password = db.Column(db.String(250),unique=False)

    def __repr__(self):
        return '<Sindico %r>' % self.name

db.create_all()        


