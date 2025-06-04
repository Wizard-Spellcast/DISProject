CREATE TABLE IF NOT EXISTS artist(
	id	    INT PRIMARY KEY,
	name    VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS album(
	id  	    INT PRIMARY KEY,
	name 	    VARCHAR NOT NULL,
	artistOwner INT,
    FOREIGN KEY (artistOwner) REFERENCES artist
);

CREATE TABLE IF NOT EXISTS track(
	id      INT PRIMARY KEY,
	name    VARCHAR NOT NULL,
    artistOwner INT,
    albumOwner INT,
    FOREIGN KEY (artistOwner) REFERENCES artist,
    FOREIGN KEY (albumOwner) REFERENCES album
);



CREATE TABLE IF NOT EXISTS artistAlbumLink(
    artistID INT,
    albumID INT,
	PRIMARY KEY (artistid, albumid),
	FOREIGN KEY (artistID)  REFERENCES artist,
	FOREIGN KEY (albumID)   REFERENCES album
);

CREATE TABLE IF NOT EXISTS albumTrackLink(
    albumID INT,
    trackID INT,
	PRIMARY KEY (albumID, trackID),
	FOREIGN KEY (albumID)   REFERENCES album,
	FOREIGN KEY (trackID)   REFERENCES track
);
