from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):

	_id = db.Column(db.Integer, primary_key=True) 
	name = db.Column()
	password = db.Column()
	expert = db.Column()
	admin = db.Column()
	test = db.Column()

	def __init__(self, name, password, expert, admin):
		self.name = name
		self.password = password
		self.expert = expert
		self.admin = admin


class Question(db.Model):

	_id =  db.Column(db.Integer, primary_key=True) 
	question = db.Column()
	answer = db.Column()
	asked_by_id = db.Column()
	answered_by_id = db.Column()
	expert_id = db.Column()

	def __init__(slef, question, answer, asked_by_id, answered_by_id, expert_id):
		self.question = question
		self.answer = answer 
		self.asked_by_id = asked_by_id
		self.expert_id = expert_id


