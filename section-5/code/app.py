from flask import Flask
from flask_restful import Resource, Api
from user import User, UserRegister

import sqlite3

app = Flask(__name__)
api = Api(app)


class User(Resource):
	def get(self, name):
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		sql = 'SELECT * FROM users WHERE username = "{}"'.format(name)
		#sql = 'SELECT * FROM items WHERE name = ?'
		result = cur.execute(sql)
		#result = cur.execute(query, (name,))
		get_result = result.fetchall()
		conn.close()

		if len(get_result) != 0:
			return {'result': 'User exists'},200
		else:
			return {'result': 'No such user'},200

class Item(Resource):
	
	@classmethod
	def sql_query(cls, sql_syntax):
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		sql = sql_syntax
		result = cur.execute(sql)
		get_result = result.fetchall()
		conn.close()
		return get_result

	def get(self, name):
		sql = 'SELECT * FROM item WHERE name = "{}" '.format(name)
		get_result = Item.sql_query(sql)
		return {"name": get_result[0][1], "price": get_result[0][2]}

	def post(self, name):
		pass

	def put(self, name):
		pass

	def delete(self, name):
		pass



if __name__ == "__main__":
	api.add_resource(UserRegister, '/register')
	api.add_resource(User, '/user/<string:name>')
	api.add_resource(Item, '/item/<string:name>')

	app.run(port=8080,debug=True)
