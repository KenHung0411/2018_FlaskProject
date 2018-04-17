from flask import Flask, render_template, request, redirect, url_for, g #Just store on this whatever you want. For example a database connection or the user that is currently logged in

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from model import log_date,food


app = Flask(__name__)
'''
good practice of database
'''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #tracking every modification (turn off)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_track.db'


# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)



'''
from app import db
db.create_all()
db.session.commit()
'''

'''
Bad practice of database

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

'''

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
	food_list = food.show_all_rows()

	print(food_list)
	if request.method == 'GET':
		list_food_day = query_date.food.all()

		if list_food_day:		

			return render_template('day.html',dd=query_date, today_food = list_food_day , food_list=food_list )
		else:
			return render_template('day.html',dd=query_date, today_food = [], food_list=food_list )
	

	if request.method == 'POST':
		food_name = request.form['food']
		new_food = food.query_data_row(food_name)
		put_in_date = log_date.query_data_row(dd)

		put_in_date.food.append(new_food)
		db.session.commit()

		return 'food added'




if __name__ == '__main__':
	#manager.run()
	
	from db import db
	db.init_app(app)
	app.run(debug=True,port=8080)
	'''
	python app.py db init
    python app.py db migrate
    python app.py db upgrade
	'''

