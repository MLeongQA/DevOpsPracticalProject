from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config.update(
    #SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI"),
    SECRET_KEY=getenv("SECRET_KEY"),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

from . import routes