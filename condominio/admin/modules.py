
from condominio import db




class Sindico(db.Model):

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


