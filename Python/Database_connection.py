#Standard process------------
# 1. connect to database
# 2. create a cursor object
# 3. write a sql query
# 4. commit changes
# 5. Close connection

#------------------using sqllite3-------------------
import sqlite3

con = sqlite3.connect(r'C:\Users\bisha\Desktop\Bob\Python\Database\lite.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES('wine glass',10,5)")
cur.execute("INSERT INTO store VALUES('small glass',2,0.5)")
con.commit()
con.close()

#----------- fetch records from db-------------------------
con = sqlite3.connect(r'C:\Users\bisha\Desktop\Bob\Python\Database\lite.db')
cur = con.cursor()
cur.execute("SELECT * FROM store")
rows = cur.fetchall()
con.close()

print(rows)