CREATE TABLE IF NOT EXISTS artist(
	id	 		SERIAL PRIMARY KEY,
	name 	VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS  album(
	id  	    SERIAL PRIMARY KEY,
	name 	    VARCHAR NOT NULL,
	artistOwner INT,
    FOREIGN KEY (artistOwner) REFERENCES  artist
);

CREATE TABLE IF NOT EXISTS  track(
	id      SERIAL PRIMARY KEY,
	name    VARCHAR NOT NULL,
    primaryArtist INT,
    FOREIGN KEY (primaryArtist) REFERENCES  artist
);

CREATE TABLE IF NOT EXISTS  genre(
	id      SERIAL PRIMARY KEY,
	name    VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS  artistAlbumLink(
    artistID INT,
    albumID INT,
	PRIMARY KEY (artistid, albumid),
	FOREIGN KEY (artistID)  REFERENCES artist,
	FOREIGN KEY (albumID)   REFERENCES album
);

CREATE TABLE IF NOT EXISTS  albumTrackLink(
    albumID INT,
    trackID INT,
	PRIMARY KEY (albumID, trackID),
	FOREIGN KEY (albumID)   REFERENCES album,
	FOREIGN KEY (trackID)   REFERENCES track
);

CREATE TABLE IF NOT EXISTS  trackGenreLink(
    genreID INT,
    trackID INT,
	PRIMARY KEY (genreID, trackID),
	FOREIGN KEY (genreID)   REFERENCES genre,
	FOREIGN KEY (trackID)   REFERENCES track
);
