'''
Created on Oct 10, 2015

@author: catzhangy1
'''
from flask import Flask
app = Flask(__name__)


#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

    
@app.route("/")
def hello():
    
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    except:
        print "I am unable to connect to the database"
    return "Hello World!jej "

if __name__ == "__main__":
    app.run()