from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
def homepage():
	pass

@app.route('/author_list')
def author_page():
	conn = sqlite3.connect('library.db')
	cur = conn.cursor()
	author = cur.execute('''select id,name from author;''')
	authors = [dict(id=row[0], name=row[1]) for row in author.fetchall()]
	print(authors)
	return render_template('authors.html', authors=authors)





if __name__ == "__main__":
	app.run(port=8080)