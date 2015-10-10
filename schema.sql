DROP TABLE if EXISTS Users;
DROP TABLE if EXISTS Songs;
DROP TABLE if EXISTS Playlists;

CREATE TABLE Users
(id INTEGER NOT NULL,
 name VARCHAR(256) NOT NULL,
 api_token VARCHAR(256),
 playlistId INTEGER,
 UNIQUE(id, playlistId));

CREATE TABLE Songs
(songId INTEGER NOT NULL,
 songTitle VARCHAR(256),
 songArtist VARCHAR(256),
 songGenre VARCHAR(256));

CREATE TABLE Playlists
 (playlistId INTEGER NOT NULL,
 songId INTEGER NOT NULL);

