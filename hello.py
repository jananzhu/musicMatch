'''
Created on Oct 10, 2015

@author: catzhangy1
'''
import db
from flask import Flask, render_template, flash, redirect, url_for, Blueprint


'''Configuring local Postgres Database on Shell
postgres -D /usr/local/var/postgres -- starts up postgrespo
createuser admin -- create admin user
createdb -U admin testdb'''

app = Flask(__name__)

# profile = Blueprint('profile', __name__,
#                     template_folder='templates',
#                     static_folder='static')
# app.register_blueprint(profile)
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
#     try:
#         connect = db.connect_db()
#         db.init_db(connect)
#         print 'Connected to database'
#     except:
#         print "Database not ready to be used"
#     connect.close()
    return render_template('index.html', name='hello')


if __name__ == "__main__":
    app.run()