from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_classy import FlaskView, route


app = Flask(__name__)

# app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://user:password@localhost/foo'
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# db = SQLAlchemy(app)

# Create a table
# Show limited rows
# class Comments(db.Models):
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(255))
# 	comment = db.Column(db.String(255))
'''
from app.templates import db
db.create_all()
'''


# @app.route('/')
# def index():
# 	return '<h1>Hi hello there</h1>'

# @app.route('/')
# def index():
# 	result = Comments.query.all()

# 	return render_template('index.html', result=result)

@app.route('/sign')
def sign():
	return render_template('sign.html')

# # Security issue
# @app.route('/process', methods=['POST'])
# def process():
# 	name = request.form['name']
# 	comment = request.form['comment']

# 	signature = Comments(name=nmae, comment=comment)
# 	db.session.add(signature)
# 	db.session.commit()

# 	#return render_template('index.html', name=name, comment=comment)
# 	return redirect(url_for('index'))


@app.route('/home',methods=['GET','POST'])
def home():
	links = ['www.yahoo.com.tw', 'www.google.com', 'www.youtube.com.tw']
	return render_template('example.html', myvar=None, links=links)

#Flask take everything before View create "Member" route 
#URL will convert to lower case
class MemberView(FlaskView):
	def index(self):
		return 'This is a member_index'
	def get(self, id):
		return 'This is ID' + str(id)

	@route('/userpage')
	def account(self):
		return 'This is account page!' + 'The URL is: ' + url_for('MemberView:account')

	def before_request(self, name):
		print 'This is happening before the request'
		
	def after_request(self, name, response):
		print 'This is happening before the request'
		return response

	#def post
	#def route

MemberView.register(app)


if __name__ == '__main__':
	app.run(debug=True)

