CREATE DATABASE wizard;

CREATE TABLE artist(
	id	 		SERIAL PRIMARY KEY,
	name 	VARCHAR NOT NULL
);

CREATE TABLE album(
	id  	    SERIAL PRIMARY KEY,
	name 	    VARCHAR NOT NULL,
	artistOwner INT,
    FOREIGN KEY (artistOwner) REFERENCES  artist
);

CREATE TABLE track(
	id      SERIAL PRIMARY KEY,
	name    VARCHAR NOT NULL,
    primaryArtist INT,
    FOREIGN KEY (primaryArtist) REFERENCES  artist
);

CREATE TABLE artistAlbumLink(
    artistID INT,
    albumID INT,
	PRIMARY KEY (artistid, albumid),
	FOREIGN KEY (artistID)  REFERENCES artist,
	FOREIGN KEY (albumID)   REFERENCES album
);

CREATE TABLE albumTackLink(
    albumID INT,
    trackID INT,
	PRIMARY KEY (albumID, trackID),
	FOREIGN KEY (albumID)   REFERENCES album,
	FOREIGN KEY (trackID)   REFERENCES track
);