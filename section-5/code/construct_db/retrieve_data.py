import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()



insert_value = "select * from users"

result = cur.execute(insert_value)
result = result.fetchall()
print(result)

conn.commit()

conn.close()

