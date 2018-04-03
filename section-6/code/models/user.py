import sqlite3

from db import db


class UserModel(db.Model): #extend modeldb for sqlalchemy
	
	__tablename__ = 'users'

	#sqlalchemy will automatically add "primary_key"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_username(cls, username):
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
		# result = cursor.execute(query, (username,))
		# row = result.fetchone()
		# if row:
		# 	user = cls(*row)
		# else:
		# 	user = None

		# connection.close()
		# return user
		return cls.query.filter_by(username=username).first()

	@classmethod
	def find_by_id(cls, _id):
		# connection = sqlite3.connect('data.db')
		# cursor = connection.cursor()

		# query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
		# result = cursor.execute(query, (_id,))
		# row = result.fetchone()
		# if row:
		# 	user = cls(*row)
		# else:
		# 	user = None
		# connection.close()
		# return user
		return cls.query.filter_by(id=id).first()

