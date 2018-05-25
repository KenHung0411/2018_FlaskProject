from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

#Redis 
from redis import Redis


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)
app.config['SECRET_KEY']  = os.urandom(24)


db = SQLAlchemy(app)
redis = Redis()

from flask_question import routes

