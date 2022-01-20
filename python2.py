import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()

req = "select * from velib2"
result = cur.execute(req)
for row in result:
     print(row[1])
