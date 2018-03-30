from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'ken'
api = Api(app)

# JWT creates a new endpoint, that endpoint is /auth , when we call /auth we send a username & password, and JWT send to authenticate fuction 
# we can send it to the next request when we send JWT token what JWT does is calls the identity function, and it use JWT token to get user ID 

jwt = JWT(app, authenticate, identity) # /auth  (object of a secret, authenticate, payload)

#Create a in-memory database
items = []


#Define our resource
class Item(Resource):

	#be aware of these aren't instance variabe instead these are class variable
	parser = reqparse.RequestParser()
	parser.add_argument('price',
				type=float,
				required = True,
				help = "This filed cannot be left blank!"
			)
	data = parser.parse_args()

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

		#data = request.get_json(force=True) #if not proper header content type will cause error or if it's not json format, force means  no need content type header
		# parser = reqparse.RequestParser()
		# parser.add_argument('price',
		# 		type=float,
		# 		required = True,
		# 		help = "This filed cannot be left blank!"
		# 	)
		# data = parser.parse_args()
		data = Item.parser.parse_args()
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item , 201

	def delete(self, name):
		#declare the item variable is the "items" out oh the class
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Item deleted'}

	def put(self, name):
		#data = request.get_json(force=True)
		# parser = reqparse.RequestParser()
		# parser.add_argument('price',
		# 		type=float,
		# 		required = True,
		# 		help = "This filed cannot be left blank!"
		# 	)
		# data = parser.parse_args()
		#print(data['another'])
		
		data = Item.parser.parse_args()
		item = next(filter(lambda x:x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else:
			#use entire payload, if payload had a name that will change entire row 
			#item.update(data)
		return item




class ItemList(Resource):
	def get(self):
		return {'items':items}


api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:8080/item/something ,compare this line with line 10
api.add_resource(ItemList, '/items')


app.run(port=8080, debug=True)
