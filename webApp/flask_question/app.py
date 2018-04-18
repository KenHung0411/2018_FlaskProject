from flask import Flask, render_template, request, session, redirect, url_for

#Comment below line if wants to do migrate
#from models import Users

from flask_sqlalchemy import SQLAlchemy

#mask the password by hashing data
from werkzeug.security import generate_password_hash, check_password_hash

import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)
app.config['SECRET_KEY']  = os.urandom(24)

@app.route('/login', methods=['POST','GET'])
def login(): 

	if request.method == "POST":
		name = request.form['Name']
		password = request.form['Password']
		valid_password = Users.find_user_by_name(name).password

		if check_password_hash(valid_password, password):
			session['username'] = request.form['Name']
			return "<h1>Login!!</h1>"
		else:
			return "<h1>Login Failed!!</h1>"


	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('user', None)
	return redirect(url_for('home'))

@app.route('/register', methods=['POST','GET'])
def register():

	if request.method == "POST":
		name = request.form['Name']
		password =  generate_password_hash(request.form['Password'], method='sha256')
		add_user = Users(name=name, password=password).add_user()
		return "User_added!"

	return render_template('register.html')

@app.route('/users')
def users():
	return render_template('users.html')

@app.route('/home')
def home():
	user = None
	if 'username' in session:
		user = session['username']
	return render_template('home.html', user=user)


@app.route('/question')
def question():
	return render_template('question.html')

@app.route('/answer')
def answer():
	return render_template('answer.html')

@app.route('/ask')
def ask():
	return render_template('ask.html')

@app.route('/unanswered')
def unanswered():
	return render_template('unanswered.html')



if __name__ == "__main__":
	from models import db, Users#must to import here 
	db.init_app(app)
	app.run(debug=True, port=8080)

