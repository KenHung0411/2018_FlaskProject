from flask_sqlalchemy import SQLAlchemy

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Users(db.Model):

	_id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(30), nullable=False)
	password = db.Column(db.String(16), nullable=False)
	expert = db.Column(db.Boolean(),nullable=True)
	admin = db.Column(db.Boolean(),nullable=True)
	
	
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.expert = False
		self.admin = False

	def add_user(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_user_by_name(cls, name):
		return cls.query.filter_by(name=name).first()


class Question(db.Model):

	_id =  db.Column(db.Integer, primary_key=True) 
	question = db.Column(db.Text())
	answer = db.Column(db.Text())
	asked_by_id = db.Column(db.Integer())
	answered_by_id = db.Column(db.Integer())
	expert_id = db.Column(db.Integer())

	def __init__(slef, question, answer, asked_by_id, answered_by_id, expert_id):
		self.question = question
		self.answer = answer 
		self.asked_by_id = asked_by_id
		self.expert_id = expert_id

	def add_question(self):
		db.session.add(self)
		db.session.commit()	


'''
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
'''

if __name__ == "__main__":
	manager.run()

