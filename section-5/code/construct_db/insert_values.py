import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()


user = [
	(2, 'alex', 'alex123'),
	(3,  'josh', 'josh456')
]
insert_value = "insert into users values (?,?,?)"

cur.executemany(insert_value,user)

conn.commit()

conn.close()

