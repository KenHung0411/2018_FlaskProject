from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


#Define our resource
class Student(Resource):
	#@app.route('/student/<string:name>')
	def get(self, name):
		return {'student': name}


api.add_resource(Student, '/student/<string:name>') #http://127.0.0.1:8080/student/Rolf ,compare this line with line 10

app.run(port=8080)