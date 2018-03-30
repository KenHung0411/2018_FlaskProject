import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()

create_table_user = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY autoincrement , username text, password text)"
create_table_item  = "CREATE TABLE IF NOT EXISTS item (id INTEGER PRIMARY KEY autoincrement , name text, price INTEGER)"
cur.execute(create_table_user)
cur.execute(create_table_item)

conn.commit()

conn.close()

