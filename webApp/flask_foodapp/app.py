from flask import Flask, render_template, request, redirect, url_for, g #Just store on this whatever you want. For example a database connection or the user that is currently logged in
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)
'''
good practice of database
'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_track.db'

db = SQLAlchemy(app)

class log_date(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	entry_date = db.Column(db.String(255))


	def __repr__(self):
		return 'logdate'

	def insert_data_row(self):
		db.session.add(self)
		db.session.commit()
		# a = log_date(id = 1, entry_date = '2018/04/11')

	def delete_data_row(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def query_data_row(cls, entry_date):
		result = cls.query.filter_by(entry_date=entry_date).first()
		return result

	@classmethod
	def show_all_rows(cls):
		results = cls.query.all()
		return results



class food(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	protein = db.Column(db.String(30))
	carbohydrates = db.Column(db.String(30))
	fat = db.Column(db.String(30))
	calories = db.Column(db.String(30))

	def __repr__(self):
		return 'food'

	def insert_data_row(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def show_all_rows(cls):
		results = cls.query.all()
		return results

	@classmethod
	def query_data_row(cls,food_name):
		result = cls.query.filter_by(name=food_name).first()
		return result


class food_date(db.Model):
	food_id = db.Column(db.Integer, primary_key=True)
	log_date_id = db.Column(db.Integer)

	def insert_data_row(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def select_food_in_date(cls, log_date_id):
		result = cls.query.filter_by()

	@classmethod
	def show_all_rows(cls):
		results = cls.query.all()
		return results

	def __repr__(self):
		return 'food_date'
'''
from app import db
db.create_all()
'''

'''
Bad practice of database
'''
def connect_db():
	sql = sqlite3.connect("D:\\016713\Desktop\\python pratice\\2018_FlaskProject\\webApp\\flask_foodapp\\food_track.db")
	sql.row_factory = sqlite3.Row
	return sql

def get_db():
	if not hasattr(g, 'sqlite3'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()



@app.route('/', methods=['GET','POST'])
def home():
	date_list = log_date.show_all_rows()
	if request.method == 'POST':
		date = request.form['entry_date']
		add_date = log_date(entry_date= date).insert_data_row()
		return  redirect(url_for('home'))

	return render_template('home.html', date_list=date_list)


@app.route('/addfood', methods=['GET','POST'])
def add_food():
	viewAllfood = food().show_all_rows()
	if request.method == 'POST':
		name = request.form['food_name']
		protein = request.form['protein']
		carbohydrates = request.form['carbohydrates']
		fat = request.form['fat']
		new_food = food(name=name,protein=protein,carbohydrates=carbohydrates,fat=fat)
		new_food.insert_data_row()	
		return redirect(url_for('add_food'))

	return render_template('add_food.html', foodlist=viewAllfood)


@app.route('/day/<dd>', methods=['GET','POST'])
def day(dd):
	
	query_date = log_date.query_data_row(dd)
	foodlist = food.show_all_rows()
	result =  food_date.show_all_rows()
	
	if query_date:
		return render_template('day.html',dd=query_date, foodlist=foodlist )
	else:
		return 'Bad request 404'

	if request.method == 'POST':
		food_name = request.form['food']
		food_id = food.query_data_row(food_name)

		new_food_date = food_date(food_id=food_id ,log_date_id=query_date.entry_date)
		new_food_date.insert_data_row()
		print('Test!!')
		return 'row has been added !'


if __name__ == '__main__':
	app.run(debug=True,port=8080)

