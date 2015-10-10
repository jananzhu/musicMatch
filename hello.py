'''
Created on Oct 10, 2015

@author: catzhangy1
'''
from flask import Flask
from contextlib import closing
import psycopg2

'''Configuring local Postgres Database on Shell
postgres -D /usr/local/var/postgres -- starts up postgrespo
createuser admin -- create admin user
createdb -U admin testdb'''

app = Flask(__name__)
# app.config.from_object(__name__)
# # DATABASE = '/tmp/flaskr.db'
# DBNAME = 'testdb'
# DEBUG = True
# # SECRET_KEY = 'development key'
# USERNAME = 'admin'
# HOST = 'localhost'
# PASSWORD = 'default'

@app.route("/")
def main():
    try:
        connect = connect_db()
        init_db(connect)
        print 'Connected to database'
    except:
        print "Database not ready to be used"

    connect.close()
    return "Hello World! "

def connect_db():
#     Need to refactor into app.config variable later
    return psycopg2.connect(database='testdb', user='catzhangy1', port='5432', host='localhost') 

def init_db(dbConnection):
    cur = dbConnection.cursor()
    try:
        cur.execute(open("schema.sql", "r").read())
    except:
        print "DB Initialization failed"
    cur.close()
    return
#     with closing(connection) as db:
#         with db as cursor:
#             cursor.execute(open("schema.sql", "r").read())
#         db.commit()
  
def drop_db(dbConnection):
    cur = dbConnection.cursor()
    try:
        cur.execute("""DROP DATABASE foo_test""")
    except:
        print "I can't drop our test database!"
    cur.close()
    return 

if __name__ == "__main__":
    app.run()