'''
Created on Oct 10, 2015

@author: catzhangy1
'''
from contextlib import closing
import psycopg2

def connect_db():
#     Need to refactor into app.config variable later
    db = psycopg2.connect(database='testdb', user='catzhangy1', port='5432', host='localhost') 
    return db

def init_db(db):
#     cur = db.cursor()
    with db:
        with db.cursor() as cur:
            try:
                cur.execute(open("schema.sql", "r").read())
            except:
                print "DB Initialization failed"
#     initializeSampleDatabase(db)
    return

#     with closing(connection) as db:
#         with db as cursor:
#             cursor.execute(open("schema.sql", "r").read())
#         db.commit()
def drop_db(db):
#     cur = db.cursor()
    with db:
        with db.cursor() as cur:
            try:
                cur.execute("""DROP DATABASE foo_test""")
            except:
                print "I can't drop our test database!"
    return 

# Returns rows of query result as list of tuples
def getAllSongs(db, userId):
    cur= db.cursor()
    try:
        cur.execute("SELECT DISTINCT Playlists.songId FROM Users, Playlists WHERE id = %d AND Users.playlistId = Playlists.playlistId;", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return
        
def getSongInfo(db, songId):
    cur= db.cursor()
    try:
        cur.execute("SELECT * FROM Songs WHERE songId = %s", (songId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    return

# Returns number of songs by genre for a given user
def getSongsByGenre(db, userId):
    cur= db.cursor()
    try:
        cur.execute(
    "SELECT V2.songGenre, COUNT(V2.songGenre) FROM (SELECT DISTINCT songId FROM Playlists, Users WHERE Playlists.playlistId = Users.playlistId AND Users.id = %d) AS V1, Songs as V2 WHERE V1.songId = Songs.songId GROUP BY V2.songGenre", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return

# Return number of songs by artist for a given user
def getSongsByArtist(db, userId):
    cur = db.cursor()
    try:
        cur.execute(
 "SELECT V2.songArtist, COUNT(V2.songArtist) FROM (SELECT DISTINCT songId FROM Playlists, Users WHERE Playlists.playlistId = Users.playlistId AND Users.id = %s) AS V1, Songs as V2 WHERE V1.songId = Songs.songId GROUP BY V2.songArtist;", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return

def insertUser(db, userId):
    cur = db.cursor()
    try:
        cur.execute( "SELECT V2.songArtist, COUNT(V2.songArtist) FROM (SELECT DISTINCT songId FROM Playlists, Users WHERE Playlists.playlistId = Users.playlistId AND Users.id = %d) AS V1, Songs as V2 WHERE V1.songId = Songs.songId GROUP BY V2.songArtist;", (userId,))
        return cur.fetchall()
    except:
        print "Query failed, or no result is returned"
        return []
    cur.close()
    return "success"

# def insertPlaylist():
#     
# def insertSong():
#     print 'nothing'
    
def initializeSampleDatabase(db):
    userdict = ({"id":"1", "name":"Janan", "playlistId":"1"},
                {"id":"1", "name":"Janan", "playlistId":"2"},
                {"id":"2", "name":"Cat", "playlistId":"1"},
                {"id":"2", "name":"Cat", "playlistId":"3"},
                {"id":"3", "name":"Jej", "playlistId":"2"},
                {"id":"3", "name":"Jej", "playlistId":"1"},
                {"id":"3", "name":"Jej", "playlistId":"3"})
    playlists = ({"playlistId":"1", "songId":"1"},
                 {"playlistId":"1", "songId":"2"},
                 {"playlistId":"1", "songId":"3"},
                 {"playlistId":"2", "songId":"2"},
                 {"playlistId":"2", "songId":"3"},
                 {"playlistId":"2", "songId":"4"},
                 {"playlistId":"3", "songId":"5"},
                 {"playlistId":"3", "songId":"1"},
                 {"playlistId":"3", "songId":"6"},
                 {"playlistId":"3", "songId":"7"},
                 {"playlistId":"3", "songId":"8"})
    songLists = ({"songId":"1", "songTitle":"Baby", "songArtist":"Justin Bieber", "songGenre":"Pop"},
                 {"songId":"2", "songTitle":"Boyfriend", "songArtist":"Justin Bieber", "songGenre":"Pop"},
                 {"songId":"3", "songTitle":"One More Time", "songArtist":"Justin Bieber", "songGenre":"Pop"},
                 {"songId":"4", "songTitle":"Blurred Lines", "songArtist":"Robin Thicke", "songGenre":"R&B"},
                 {"songId":"5", "songTitle":"Thinkin About You", "songArtist":"Frank Ocean", "songGenre":"R&B"},
                 {"songId":"6", "songTitle":"Get Her Back", "songArtist":"Robin Thicke", "songGenre":"R&B"},
                 {"songId":"7", "songTitle":"Mirrors", "songArtist":"Justin Timberlake", "songGenre":"Pop"},
                 {"songId":"8", "songTitle":"Niggas in Paris", "songArtist":"Jay Z", "songGenre":"Rap"})
#     cur = db.cursor()
    with db:
        with db.cursor() as cur:
            try:
                cur.executemany("INSERT INTO Users(id, name, playlistId) VALUES (%(id)d, %(name)s, %(playlistId)d);", userdict)
                cur.executemany("INSERT INTO Playlists(playlistId, songId) VALUES (%(playlistId)d, %(songId)d);", playlists)
                cur.executemany("INSERT INTO Songs(songId, songTitle, songArtist, songGenre) VALUES (%(songId)d, %(songTitle)s, %(songArtist)s, %(songGenre)s);", songLists)
            except:
                print "Insert failure"

def commit():
    db = psycopg2.connect(database='testdb', user='catzhangy1', port='5432', host='localhost') 
    return db.commit()
