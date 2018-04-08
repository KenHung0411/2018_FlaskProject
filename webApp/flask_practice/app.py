from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> Hello there</h1>'

@app.route('/home', methods=['GET','POST'])
def home():
	return '<h1> You are in the  page </h1>'

@app.route('/home/<place>')
def home_1(place):
	return '<h1> You are in the '+ place + ' page </h1>'


if __name__ == '__main__':
	app.run(debug=True)
