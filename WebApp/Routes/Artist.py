from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Artist = Blueprint('Artist', __name__)

@Artist.route("/artist")
def artist_search():
    return render_template("search.html", table='artist')

@Artist.route("/artist/<artist_id>")
def artist_lookup(artist_id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM artist WHERE id = {artist_id}")

    artist_data:models.Artist = cursor.fetchone()

    cursor.execute(f"SELECT * FROM album a WHERE id = (SELECT albumid FROM artistalbumlink WHERE artistID = {artist_id})")
    artist_albums:models.Album = cursor.fetchall()
    conn.close()

    return render_template('artist.html', artist_data=artist_data, artist_albums=artist_albums)