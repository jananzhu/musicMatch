'''
Created on Oct 10, 2015

@author: catzhangy1
'''
from contextlib import closing
import psycopg2

global db
  
def connect_db():
#     Need to refactor into app.config variable later
    db = psycopg2.connect(database='testdb', user='catzhangy1', port='5432', host='localhost') 
    return db

def close_db():
    db.close()
    return 

def init_db():
    cur = db.cursor()
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
def drop_db():
    cur = db.cursor()
    try:
        cur.execute("""DROP DATABASE foo_test""")
    except:
        print "I can't drop our test database!"
    cur.close()
    return 

# Returns rows of query result as list of tuples
def getAllSongs(userId):
    cur= db.cursor()
    try:
        cur.execute("SELECT DISTINCT Playlists.songId FROM Users, Playlists WHERE id = %s AND Users.playlistId = Playlists.playlistId", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return
        
def getSongInfo(songId):
    cur= db.cursor()
    try:
        cur.execute("SELECT * FROM Songs WHERE songId = %s", (songId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return

# Returns number of songs by genre for a given user
def getSongsByGenre(userId):
    cur= db.cursor()
    try:
        cur.execute(
    "SELECT V2.songGenre, COUNT(V2.songGenre) FROM (SELECT DISTINCT songId FROM Playlists, Users WHERE Playlists.playlistId = Users.playlistId AND Users.id = %s) AS V1, Songs as V2 WHERE V1.songId = Songs.songId GROUP BY V2.songGenre", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return

# Return number of songs by artist for a given user
def getSongsByArtist(userId):
    cur = db.cursor()
    try:
        cur.execute(
 "SELECT V2.songArtist, COUNT(V2.songArtist) FROM (SELECT DISTINCT songId FROM Playlists, Users WHERE Playlists.playlistId = Users.playlistId AND Users.id = %s) AS V1, Songs as V2 WHERE V1.songId = Songs.songId GROUP BY V2.songArtist", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return

def commit():
    return db.commit()
