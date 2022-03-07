from condominio import db
from sqlalchemy.orm import relationship



class Chamados(db.Model):
    __tablename__= "Chamados"

    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(45),unique=False)
    bloco = db.Column(db.String(20),unique=False)  
    apto = db.Column(db.String(20),unique=False)
    descricao = db.Column(db.String(2000),unique=False)
    morador_id = db.Column(db.Integer,unique=True)

    def __repr__(self):
        return '<Chamados %r>' % self.name

class Sugestoes(db.Model):
    __tablename__= "Sugestoes"

    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(45),unique=False)
    bloco = db.Column(db.String(20),unique=False)  
    apto = db.Column(db.String(20),unique=False)
    descricao = db.Column(db.String(2000),unique=False)
    morador_id = db.Column(db.Integer,unique=True)

    def __repr__(self):
        return '<Sugestoes %r>' % self.name     

class Mensagem(db.Model):
    __tablename__= "Mensagem"

    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(45),unique=False)
    bloco = db.Column(db.String(20),unique=False)  
    apto = db.Column(db.String(20),unique=False)
    descricao = db.Column(db.String(2000),unique=False)
    morador_id = db.Column(db.Integer,unique=True)

    def __repr__(self):
        return '<Mensagem %r>' % self.name

db.create_all()                   