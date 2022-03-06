from condominio import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_morador(user_id):
    return Morador.query.get(user_id)


class Morador(db.Model,UserMixin):
    __tablename__= "Morador"

    id = db.Column(db.Integer, primary_key=True)  
    nome = db.Column(db.String(45),unique=False)
    usuario = db.Column(db.String(45),unique=True)
    email = db.Column(db.String(45),unique=True)
    tel = db.Column(db.String(20),unique=False)
    bloco = db.Column(db.String(20),unique=False)  
    apto = db.Column(db.String(20),unique=False)  
    password = db.Column(db.String(250),unique=False)

    def __repr__(self):
        return '<Morador %r>' % self.name

db.create_all()        
