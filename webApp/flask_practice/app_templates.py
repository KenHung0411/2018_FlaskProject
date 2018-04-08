from flask import Flask , render_template, request

app = Flask(__name__)


# @app.route('/')
# def index():
# 	return '<h1>Hi hello there</h1>'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sign')
def sign():
	return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']
	return render_template('index.html', name=name, comment=comment)

@app.route('/home',methods=['GET','POST'])
def home():
	links = ['www.yahoo.com.tw', 'www.google.com', 'www.youtube.com.tw']
	return render_template('example.html', myvar=None, links=links)




if __name__ == '__main__':
	app.run(debug=True)

