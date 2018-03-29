#-- sqlite3 library.db < library-schema.sql
import sqlite3





conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute(
	'''
	
	create table country(
		id INTEGER PRIMARY KEY autoincrement,
		name text not null);
	''')
conn.commit()
conn.close()


conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute(
	'''
	
	create table author(
		id INTEGER PRIMARY KEY autoincrement,
		country_id integer,
		name text not null
	);''')
conn.commit()
conn.close()


conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute(
	'''
	create table book(
		id INTEGER PRIMARY KEY autoincrement,
		author_id integer,
		title text not null,
		isbn text
	);''')

conn.commit()
conn.close()



