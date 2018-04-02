from flask import Flask
from flask_restful import Resource, Api, reqparse
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

	TABLE_NAME = 'items'

	parser = reqparse.RequestParser()
	parser.add_argument('price',\
			type = float,
			required = True,
			help = 'this field cannot be left bank!!'
		)


	@classmethod
	def sql_query(cls, sql_syntax):
		conn = sqlite3.connect('data.db')
		cur = conn.cursor()
		sql = sql_syntax
		result = cur.execute(sql)
		get_result = result.fetchall()
		conn.commit()
		conn.close()
		return get_result

	def get(self, name):
		sql = 'SELECT * FROM item WHERE name = "{}" '.format(name)
		get_result = Item.sql_query(sql)
		return {"name": get_result[0][1], "price": get_result[0][2]}

	def post(self, name):
		sql_1= 'SELECT * FROM item WHERE name = "{}" '.format(name)
		
		check_if_exist = self.sql_query(sql_1)
		if check_if_exist: return {'message': 'This item is already exsists!!'},400

		data = Item.parser.parse_args()
		item = {'name':name, 'price':data['price']}
		
		try:
			sql_2= 'INSERT INTO item VALUES(NULL,"{}",{})'.format(item['name'], item['price']) #NULL is the autoincrement
			self.sql_query(sql_2)
			return item
		except:
			return {"message":"Data insert failed..."},500 #Internal server error

	# def put(self, name):
	# 	sql_1= 'SELECT * FROM item WHERE name = "{}" '.format(name)

	# 	data = Item.parser.parse_args()
	# 	item = {'name':name, 'price':data['price']}
	# 	updated_item = {'name':name,'price':data['price']}

	# 	sql_update = 'UPDATE item SET price={} WHERE name="{}" 'format(item['name'], item['price'])
	# 	sql_insert = 'INSERT INTO item VALUES(NULL,"{}",{})'.format(item['name'], item['price']) #NULL is the autoincrement

	# 	check_if_exist = self.sql_query(sql_1)

	# 	if check_if_exist:
	# 		try:
	# 			self.sql_query(sql_update)
	# 			return updated_item
	# 		except:
	# 			return {'Message':'Update Failed'}
	# 	else:
	# 		try:
	# 			self.sql_query(sql_insert)
	# 			return item
	# 		except:
	# 			return {'Message':'Insert Failed'}


	def delete(self, name):
		sql = 'DELETE FROM item WHERE name = "{}" '.format(name)
		get_result = Item.sql_query(sql)
		return {'message':'item deleted!!'}


class ItemList(Resource):
	def get(self):
		sql = "SELECT * FROM item"
		itemlist = Item.sql_query(sql)
		items = [{'name': i[1],'price':i[2]} for i in itemlist]
		return items



if __name__ == "__main__":
	api.add_resource(UserRegister, '/register')
	api.add_resource(User, '/user/<string:name>')
	api.add_resource(Item, '/item/<string:name>')
	api.add_resource(ItemList, '/items')
	app.run(port=8080,debug=True)
