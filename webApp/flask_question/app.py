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

def get_current_user():
	user_result= None
	if 'username' in session:
		user = session['username']
		#check if db have data 
		user_result = Users.find_user_by_name(user)
		return user_result
	
	return None
	

@app.route('/login', methods=['POST','GET'])
def login(): 

	if request.method == "POST":
		name = request.form['Name']
		password = request.form['Password']
		valid_password = Users.find_user_by_name(name).password

		if check_password_hash(valid_password, password):
			session['username'] = request.form['Name']
			return redirect(url_for('home'))
		else:
			return "<h1>Login Failed!!</h1>"
	
	return render_template('login.html')

@app.route('/logout')
def logout():
	user = session.pop('username', None)
	return redirect(url_for('home'))

@app.route('/register', methods=['POST','GET'])
def register():
	user = get_current_user()

	if request.method == "POST":
		name = request.form['Name']
		password =  generate_password_hash(request.form['Password'], method='sha256')
		add_user = Users(name=name, password=password).add_user()
		return "User_added!"

	return render_template('register.html', user=user)

@app.route('/users')
def users():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	return render_template('users.html',user=user)

@app.route('/home')
def home():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	return render_template('home.html',user=user)


@app.route('/question')
def question():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	return render_template('question.html',user=user)

@app.route('/answer')
def answer():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	return render_template('answer.html',user=user)

@app.route('/ask')
def ask():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	return render_template('ask.html',user=user)

@app.route('/unanswered')
def unanswered():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	return render_template('unanswered.html',user=user)



if __name__ == "__main__":
	from models import db, Users#must to import here 
	db.init_app(app)
	app.run(debug=True, port=8080)

