from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = '@#4324234325efg4b35'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:phutv123@localhost/webflask?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)