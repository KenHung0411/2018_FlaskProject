from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
#import sqlite3
from models.store import StoreModel

class Store(Resource):

	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json
		return {'message':'Store not found'}, 404

	def post(self,name):
		if StoreModel.find_by_name(name):
			return {"message":"store is already there"}, 400

		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			return {"message":"something went wrong"}

		return store.json(), 201

	def delete(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()
			return {"message":"store deleted"}
		else:
			return {"message":"store doesn't exists..."}

class StoreList(Resource):
	def get(self):
		return {'stores': [i.json for i in StoreModel.query.all()]}

