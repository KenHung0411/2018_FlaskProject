from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_question import db


class Users(db.Model):

	_id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(30), nullable=False)
	password = db.Column(db.String(16), nullable=False)
	expert = db.Column(db.Boolean(),nullable=True)
	admin = db.Column(db.Boolean(),nullable=True)

	#question = db.relationship("Question", primaryjoin="User._id==Question._id")	
	
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.expert = False
		self.admin = False


	def add_user(self):
		db.session.add(self)
		db.session.commit()

	def delete_user(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def find_user_by_name(cls, name):
		return cls.query.filter_by(name=name).first()

	@classmethod
	def find_user_by_id(cls, id):
		return cls.query.filter_by(_id=id).first()

	@classmethod
	def fetch_all_users(cls):
		return cls.query.all()

	@classmethod
	def promote_to_expert(cls, name):
		promote_user = cls.find_user_by_name(name)
		promote_user.expert = True
		db.session.commit()

	@classmethod
	def fetch_all_expert(cls):
		return cls.query.filter_by(expert=True).all()


class Question(db.Model):

	_id =  db.Column(db.Integer, primary_key=True) 
	question = db.Column(db.Text(),nullable=True)
	answer = db.Column(db.Text(),nullable=True)

	asked_by_id = db.Column(db.Integer,nullable=True)
	#asked_by_id = db.Column(Integer, ForeignKey('user.id'))
	
	answered_by_id = db.Column(db.Integer,nullable=True)
	

	def __init__(self, question, asked_by_id, answered_by_id):
		self.question = question
		self.answer = ""
		self.asked_by_id = asked_by_id
		self.answered_by_id = answered_by_id

	def add_question(self):
		db.session.add(self)
		db.session.commit()	

	@classmethod
	def fetch_question_by_id(cls,id):
		return cls.query.filter_by(_id = id).first()

	@classmethod
	def fetch_all_questions(cls):
		return cls.query.all()

	@classmethod
	def join_id_with_ask_user(cls):
		return cls.query.join(Users, Question.asked_by_id ==Users._id).add_columns(Question.asked_by_id, Question.answered_by_id ,Users.name).all()

	@classmethod
	def join_id_with_unanswer_question(cls):
		return cls.query.join(Users, Question.asked_by_id ==Users._id).add_columns(Question.asked_by_id, Users.name).filter(Question.answer=="").all()



class Account(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='post', lazy=True)


class Post(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text(), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
	account = db.relationship('Account', backref='account', lazy=True)


'''
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
'''
