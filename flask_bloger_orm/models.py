from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime)
	content = db.Column(db.Text)

	def add_into(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_all_post(cls):
		return cls.query.all()

if __name__ == "__main__":

	db.create_all()
