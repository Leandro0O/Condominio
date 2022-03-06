from flask_wtf import FlaskForm
from wtforms import StringField, validators, Form

class Chamados(Form):
    nome = StringField('Nome do morador:', [validators.length(min=0, max=45),validators.DataRequired()])
    bloco = StringField('Bloco: ', [validators.length(min=0, max=20),validators.DataRequired()])
    apto = StringField('APTO:', [validators.length(min=0, max=20),validators.DataRequired()])
    descricao = StringField('Descrição:', [validators.length(min=0, max=2000),validators.DataRequired()])



class Sugestoes(Form):
    nome = StringField('Nome do morador:', [validators.length(min=0, max=45),validators.DataRequired()])
    bloco = StringField('Bloco: ', [validators.length(min=0, max=20),validators.DataRequired()])
    apto = StringField('APTO:', [validators.length(min=0, max=20),validators.DataRequired()])
    descricao = StringField('Descrição:', [validators.length(min=0, max=2000),validators.DataRequired()])



class Mensagem(Form):
    nome = StringField('Nome do morador:', [validators.length(min=0, max=45),validators.DataRequired()])
    bloco = StringField('Bloco: ', [validators.length(min=0, max=20),validators.DataRequired()])
    apto = StringField('APTO:', [validators.length(min=0, max=20),validators.DataRequired()])
    descricao = StringField('Descrição:', [validators.length(min=0, max=2000),validators.DataRequired()])    

