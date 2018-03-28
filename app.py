from flask import Flask

app = Flask(__name__)

# @app.route('/') # http://www.google.com/
# def home():
# 	return 'hello world'

##############################################
# POST - used to receuve data
# GET - used to send data back only

# Think this file(app.py) as django's url.py 
###############################################

stores = [
{
	'name':'My Wonderful Store',
	items:[
		{
			'name':'My Item',
			'price': 15.99
		}]
}]


# POST /store data: {name:}
@app.route('/store', method=['POST'])
def create_store():
	pass


# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:8080/store/somw_name'
def get_store(name):
	pass


# GET /store
@app.route('/store')
def get_stores():
	pass

# POST /store/<string:name>/item {name:, price: }
@app.route('/store/<strng:name>/item', methods=['POST'])
def create_item_in_store(name):
	pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>') # 'http://127.0.0.1:8080/store/somw_name'
def get_item_in_store(name):
	pass



app.run(port=8080)


