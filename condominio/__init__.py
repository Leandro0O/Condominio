import bcrypt
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret314159'

bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_condominio.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'loginmorador'
login_manager.needs_refresh_message_category = 'danger'
login_manager.login_message = u'Realize o login!'


from condominio.admin import  routes
from condominio.morador import routes
from condominio.chamados import routes




    