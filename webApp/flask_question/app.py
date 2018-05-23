from flask import Flask, render_template, request, session, redirect, url_for, flash

#Comment below line if wants to do migrate
#from models import Users

from flask_sqlalchemy import SQLAlchemy

#mask the password by hashing data
from werkzeug.security import generate_password_hash, check_password_hash

from form import Login_form

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

	form = Login_form(request.form, csrf_enable=False)



	#if request.method == "POST":
	if form.validate_on_submit():
		
		username = request.form.get('username')
		password = request.form.get('password')
		'''
		valid_password = Users.find_user_by_name(name)
		if valid_password:
			if check_password_hash(valid_password.password, password):
				session['username'] = request.form['Name']
				return redirect(url_for('home'))
			else:
				return "<h1>Wrong Password!!</h1>"
		else:
			return "<h1>User not Existed!!</h1>"
		'''
		flash('login successed', 'success')
		
		return redirect(url_for('login'))
	
	#if form.errors:
	#	print(form.errors)
	#	return redirect(url_for('login'))

	return render_template('login.html' ,form=form)



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

		session['username'] =  name

		return redirect(url_for('home')) 

	return render_template('register.html', user=user)

@app.route('/users', methods=['POST','GET'])
def users():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)
	user_list = Users.fetch_all_users()

	if request.method == "POST":
		
		if "remove" in request.form['submit']:
			user = request.form['submit']
			user = user.split('-')[1]
			find_delete_user = Users.find_user_by_name(user)
			find_delete_user.delete_user()
			return redirect(url_for('users'))

		elif "promote" in request.form['submit'] :
			user = request.form['submit']
			user = user.split('-')[1]
			Users.promote_to_expert(user)
			return redirect(url_for('users'))

	return render_template('users.html',user=user,user_list= user_list)

@app.route('/home')
def home():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	all_questions = Question.join_id_with_ask_user()
	ask_by =  [ Users.find_user_by_id(i[2]).name for i in all_questions ]
	all_question_full = list(zip(ask_by, all_questions))
	print(all_question_full)
	
	return render_template('home.html', all_questions=all_question_full)


@app.route('/question/<string:question_id>')
def question(question_id):
	user = get_current_user()

	if not user:
		return render_template('login.html',user=user)
	question = Question.fetch_question_by_id(question_id)
	asked_by, answered_by = Users.find_user_by_id(question.asked_by_id).name ,Users.find_user_by_id(question.answered_by_id).name

	return render_template('question.html',user=user, question=question, asked_by= asked_by, answered_by= answered_by)

@app.route('/answer/<question_id>', methods=['POST', 'GET'])
def answer(question_id):
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	fetch_question = Question.fetch_question_by_id(question_id)

	if request.method == "POST":
		answer = request.form['answer']
		fetch_question.answer = answer
		fetch_question.add_question()
		return redirect(url_for('home'))


	return render_template('answer.html',user=user, question=fetch_question )

@app.route('/ask', methods=['POST','GET'])
def ask():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	fetch_experts =  Users.fetch_all_expert()

	if request.method == "POST":
		assign_to = request.form['expert_name']
		assign_to_id = Users.find_user_by_name(assign_to)._id
		question = request.form['question_content']
		new_question = Question(question=question, asked_by_id=user._id , answered_by_id= assign_to_id)
		new_question.add_question()

		return redirect(url_for('home'))
		

	return render_template('ask.html',user=user, expert_list=fetch_experts)

@app.route('/unanswered')
def unanswered():
	user = get_current_user()
	if not user:
		return render_template('login.html',user=user)

	question_list = Question.join_id_with_unanswer_question()
	print(question_list)

	return render_template('unanswered.html',user=user, question_list=question_list)

@app.route('/test')
def test():
	question_list = Question.join_id_with_ask_user()
	for i in question_list:
		print('Question is {}'.format(i[0].question))
		if not i[0].answer:
			print('This Question havnt have answer yet')
		else:
			print('The answer is {}'.format(i[0].answer)) 
		print('Who ask this question: {}'.format(i[2]))
	return 'test...'


if __name__ == "__main__":
	from models import db, Users, Question#must to import here 
	db.init_app(app)
	app.run(debug=True, port=8080)

