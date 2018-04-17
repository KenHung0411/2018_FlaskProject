from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class log_date(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	entry_date = db.Column(db.String(255))

	food =  db.relationship('food', secondary='food_logdate', backref='logDate', lazy='dynamic')
	#food_date = db.relationship('food_date', backref='log_date', lazy='dynamic')

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

	
	#food_date = db.relationship('food_date', backref='log_date', lazy='dynamic')
	#log_date = db.relationship('log_date', secondary='food_logdate', backref='food', lazy='dynamic')

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

	@classmethod
	def query_data_row_id(cls,id):
		result = cls.query.filter_by(id=id).first()
		return result


association_table = db.Table('food_logdate',
		db.Column('food_id', db.Integer, db.ForeignKey('food.id')),
		db.Column('log_date_id', db.Integer, db.ForeignKey('log_date.id'))
		)