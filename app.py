from flask import Flask

app = Flask(__name__)

@app.route('/') # http://www.google.com/
def home():
	return 'hello world'


app.run(port=8080)
