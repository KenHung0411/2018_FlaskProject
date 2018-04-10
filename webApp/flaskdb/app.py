from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#app.config['SQLALCHEMY_DAABASE_URI'] = 'mysql://username:password@server/db'
app.config.from_pyfile['config.cfg']

db = SQLAlchemy(app)

#To map the tables of database to python object we need to create a class
#what the table is and what columns in the table
class Example(db.Model):

	__tablenmae__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True)
	date = db.Column('data', db.Unicode)

	def __init__(self, id, data):
		self.id = id
		self.data = data

	
	#sqlalchemy will adds the row into database
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def update_db(self):
		self.query.filiter_by(id=3).first()

	def delete_db(self):
		db.session.delete(slef)
		db.session.commit()

'''
from app import Example
examples = Example.query.all()
print(examples) --> a list of full data objects
one = Example.query.filiter_by(id=3)
'''

#create a relation between database
class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	pets = db.relationship('Pet', backref='owner', lazy='dynamic') #bacref create a vitural column Pet class that references Person


class Pet(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))





if __name__ == '__main__':
	app.run(debug=True,port=8080)