import sqlite3
from db import db


class ItemModel(db.Model): #extend modeldb for sqlalchemy

	__tablename__ = "items"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def json(self):
		return {"name": self.name, "price": self.price}

	@classmethod
	def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
        #     return cls(row[0], row[1])

        #return ItemModel.query.filter_by(name=name, id=1).first() 
		return ItemModel.query.filter_by(name=name).first() 

	def save_to_db(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # #query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        # query = "INSERT INTO items VALUES(?, ?)"
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()


        #we could just tell sqlalchemy what "object" we want to insert
        #Both insert and update (upsert)
	    db.session.add(self)
	    db.session.commit()



	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()




