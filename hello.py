'''
Created on Oct 10, 2015

@author: catzhangy1
'''
import db
from flask import Flask


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
        connect = db.connect_db()
        db.init_db(connect)
        print 'Connected to database'
    except:
        print "Database not ready to be used"
    print 'print success'
    connect.close()
    return "Hello World! "


if __name__ == "__main__":
    app.run()