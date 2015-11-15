import sqlite3

conn = sqlite3.connect("myDataBase.db")

c = conn.cursor()

q = "create table logins(username text, password text)"
c.execute(q)

conn.commit()
