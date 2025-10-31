import os  
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)

db_url = os.environ.get("DATABASE_URL")

if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///mercado.db"

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "1afb86cf05c9bcf0de4be1de")



db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = 'page_login'
login_manager.login_message = 'Por favor, realize o login.'
login_manager.login_message_category = 'info'

from mercado import routes