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

INSERT INTO Users(id,name,playlistId) VALUES
	(1,'Janan',1),
	(2,'Janan',2),
	(2,'Cat',1),
	(2,'Cat',3),
	(3,'Jej',1),	
	(3,'Jej',2),
	(3,'Jej',3);

INSERT INTO Playlists(playlistId, songId) VALUES
	(1, 1),
	(1, 2),
	(1, 3),
	(2, 2),
	(2, 3),
	(2, 4),
	(3, 5),
	(3, 6),
	(3, 7),
	(3, 8);

INSERT INTO Songs(songId, songTitle, songArtist, songGenre) VALUES
(1, 'Baby', 'Justin Bieber', 'Pop'),
 (2, 'Boyfriend', 'Justin Bieber', 'Pop'),
 (3, 'One More Time', 'Justin Bieber', 'Pop'),
 (4, 'Blurred Lines', 'Robin Thicke', 'R&B'),
 (5, 'Thinkin About You', 'Frank Ocean', 'R&B'),
 (6, 'Get Her Back', 'Robin Thicke', 'R&B'),
 (7, 'Mirrors', 'Justin Timberlake', 'Pop'),
 (8, 'Niggas in Paris', 'Jay Z', 'Rap');