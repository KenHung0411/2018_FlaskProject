from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'ken'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth

#Create a in-memory database
items = []


#Define our resource
class Item(Resource):
	#@app.route('/item/<string:name>')
	@jwt_required()
	def get(self, name):
		# for item in items:
		# 	if item['name'] == name:
		# 		return item
		# 	else: 
		# 		return { 'item':'' }, 404
		item = next(filter(lambda x: x['name'] == name, items),None)
		return {'item': item}, 200 if item else 404


	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None) is not None:
			return {'message': 'The item is already esists.'} , 400

		data = request.get_json(force=True) #if not proper header content type will cause error or if it's not json format
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item , 201

	def delete(self, name):
		pass

class ItemList(Resource):
	def get(self):
		return {'items':items}


api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:8080/item/something ,compare this line with line 10
api.add_resource(ItemList, '/items')


app.run(port=8080, debug=True)
