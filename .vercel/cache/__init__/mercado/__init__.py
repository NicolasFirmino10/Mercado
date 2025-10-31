import os # Importe o 'os' para ler as variáveis
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)

db_uri = os.environ.get('POSTGRES_URL') 


if db_uri and db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')



db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = 'page_login'
login_manager.login_message = 'Por favor, realize o login.'
login_manager.login_message_category = 'info'

from mercado import routes
