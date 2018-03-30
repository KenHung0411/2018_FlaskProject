import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()


user = [
	(2, 'alex', 'alex123'),
	(3,  'josh', 'josh456')
]

item = [
	(None,'soda', 25),
	(None,'juice', 45),
	(None,'water', 10),
	(None,'milk', 35),
	(None,'soup', 30)

]

insert_value_user = "insert into users values (?,?,?)"
insert_value_item = "insert into item values (?,?,?)"

cur.executemany(insert_value_user,user)
cur.executemany(insert_value_item,item)


conn.commit()

conn.close()

