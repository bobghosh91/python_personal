#Standard process------------
# 1. connect to database
# 2. create a cursor object
# 3. write a sql query
# 4. commit changes
# 5. Close connection

#------------------using sqllite3-------------------
import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'databasepython' user='postgres' password='postgres' host='localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname = 'databasepython' user='postgres' password='postgres' host='localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def viewTable():
    conn = psycopg2.connect("dbname = 'databasepython' user='postgres' password='postgres' host='localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()

    return rows

print(viewTable())