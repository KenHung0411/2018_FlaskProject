from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/addfood')
def add_food():
	return render_template('add_food.html')

@app.route('/day')
def day():
	return render_template('day.html')



if __name__ == '__main__':
	app.run(debug=True,port=8080)

