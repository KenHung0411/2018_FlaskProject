import sqlite3
from  flask_restful import Resource, reqparse


class User:
	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username)
		conn = sqlite3.connection('data.db')
		cur = conn.cursor()

		query = "SELECT * FROM users WHERE username=?"
		result = cur.execute(query, (usernmae,)) 
		row = result.fetchone()
		if row:
			user = cls(row[0], row[1], row[2])
		else:
			user = None

		connection.close()
		return user

	@classmethod
	def find_by_id(cls, username)
		conn = sqlite3.connection('data.db')
		cur = conn.cursor()

		query = "SELECT * FROM users WHERE id=?"
		result = cur.execute(query, (usernmae,)) 
		row = result.fetchone()
		if row:
			user = cls(row[0], row[1], row[2])
		else:
			user = None

		connection.close()
		return user


class UserRegister(Resource):

	parser = reqparse.RequsetParser()
	parser.add_argument('username',
			type = str,
			required = True,
			help = "This field cannot be blank"
		)
	parser.add_argument('password',
			type = str,
			required = True,
			help = "This field cannot be blank"
		) 


	def post(self):

		data = UserRegister.parser.parse_args()
		print(data)

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query =  "INSERT INTO users VALUES (?, ?)"
		cursor.excute(query, (data['username'], data['password']))

		connection.commit()
		connection.close()


		return {'message': 'User created successfully'}, 201

		

