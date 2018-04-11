import sqlite3

sql1 = '''
create table log_date(
	id integer primary key autoincrement,
	entry_date not null
);
'''
sql2='''
create table food(
	id integer primary key autoincrement,
	name text not null,
	protein integer not null,
	carbohydrates integer not null,
	fat integer not null,
	calories integer not null
);
'''

sql3 = '''
create table food_date(
	food_id integer not null,
	log_date_id integer not null,
	primary key(food_id, log_date_id)
);
'''

db = sqlite3.connect('food_track.db')
cur = db.cursor()
cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)

db.commit()



