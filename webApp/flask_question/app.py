from flask import Flask, render_template

from models import db
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/user')
def user():
	return render_template('user.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/question')
def question():
	return render_template('question.html')

@app.route('/answer')
def answer():
	return render_template('answer.html')

@app.route('/ask')
def ask():
	return render_template('ask.html')

@app.route('/unanswered')
def unanswered():
	return render_template('unanswered.html')


'''
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
'''

if __name__ == "__main__":
	from models import db #must to import here 
	manager.run()
	db.init_app(app)
	app.run(debug=True, port=8080)

