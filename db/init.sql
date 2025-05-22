CREATE DATABASE wizard;

CREATE TABLE artist(
	id	 		SERIAL PRIMARY KEY,
	artistName 	VARCHAR NOT NULL,
	albumsLink 	INT
);

CREATE TABLE artistAlbumLink(
	artistAlbumLinkID SERIAL PRIMARY KEY,
	artistID 	INT,
	albumID 	INT
);

CREATE TABLE album(
	albumID 	SERIAL PRIMARY KEY,
	albumName 	VARCHAR NOT NULL,
	albumIcon	VARCHAR,
	trackLink 	INT
);

CREATE TABLE albumTackLink(
	albumTackLinkID SERIAL PRIMARY KEY,
	albumID VARCHAR NOT NULL,
	trackID INT
);

CREATE TABLE track(
	trackID SERIAL PRIMARY KEY,
	trackName VARCHAR NOT NULL,
	albumLink INT
);