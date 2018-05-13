from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/post')
def post():
	return render_template('post.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/add', methods=['GET','POST'])
def add():
	return render_template('add.html')

@app.route('/add_post', methods=['GET','POST'])
def add_form():
	title = request.form['title']
	subtitle = request.form['subtitle']
	author = request.form['author']
	content = request.form['content']

	add_post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now()).add_into()


	return redirect(url_for('add'))

if __name__ == '__main__':
	from models import db,Blogpost
	db.init_app(app)
	app.run(debug=True, port=8080)
