CREATE TABLE artists(
	id	 		INT PRIMARY KEY,
	artistName 	VARCHAR,
	albumsLink 	INT,
)

CREATE TABLE artistAlbumLink(
	artistAlbumLinkID INT PRIMARY KEY,
	artistID 	INT,
	albumID 	INT,
)

CREATE TABLE albums(
	albumID 	INT PRIMARY KEY,
	albumName 	VARCHAR,
	albumIcon	VARCHAR,
	tracksLink 	INT,
)

CREATE TABLE albumTackLink(
	albumTackLinkID INT PRIMARY KEY,
	albumID VARCHAR,
	tracksID INT,
)

CREATE TABLE tracks(
	trackID INT PRIMARY KEY,
	trackName VARCHAR,
	albumLink INT,
)