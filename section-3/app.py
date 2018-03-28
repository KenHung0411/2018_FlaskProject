from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

# @app.route('/') # http://www.google.com/
# def home():
# 	return 'hello world'

##############################################
# POST - used to receuve data
# GET - used to send data back only

# Think this file(app.py) as django's url.py also views.py
###############################################

stores = [
{
	'name':'My Wonderful Store',
	'items':[
		{
			'name':'My Item',
			'price': 15.99
		}]
}]


#Home Page
@app.route('/')
def home():
	return render_template('index.html')


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name' : request_data['name'],
		'items' : []
	}
	stores.append(new_store)
	return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:8080/store/somw_name'
def get_store(name):
	# Iterate over stores
	for store in stores:
		# if the store name matches, return it
		if name == store['name']:
			return jsonify(store)
		else:
			# if none match, return error message
			return  jsonify({'message':'store is not esists....'})


# GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item_list') # 'http://127.0.0.1:8080/store/somw_name'
def get_item_in_store(name):
	# Iterate over items in a store
	for store in stores:
		# if the store name matches, return items
		if store['name'] == name:
			return jsonify(store['items'])
		else:
			# if none match, return error message
			return jsonify({'message': 'Store is not exists'})


# POST /store/<string:name>/item  data: {name:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name' : request_data['name'],
				'price' : request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)
		else:
			 jsonify({'message':'store is not esists....'})



app.run(port=8080)


