from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)
app.config['SECRET_KEY']  = os.urandom(24)


db = SQLAlchemy(app)


from flask_question import routes
