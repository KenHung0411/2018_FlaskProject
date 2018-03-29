import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY autoincrement , username text, password text)"

cur.execute(create_table)

conn.commit()

conn.close()

