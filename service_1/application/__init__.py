from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config.update(
    SQLAlchemy_DATABASE_URI=getenv("DATABASE_URI"),
    SECRET_KEY=getenv("SECRET_KEY")
)

db = SQLAlchemy(app)

from application import routes