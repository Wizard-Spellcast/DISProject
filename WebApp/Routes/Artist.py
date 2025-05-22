from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Artist = Blueprint('Artist', __name__)

@Artist.route("/artist")
def artist_search():
    return redirect(url_for('Search.search', table='artist'))

@Artist.route("/artist/<id>")
def artist_lookup(id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM artist WHERE id = {id}")

    artist_data:models.Artist = cursor.fetchone()

    cursor.execute(f"SELECT * FROM album WHERE id IN (SELECT albumID FROM ArtistAlbumLink WHERE artistID = {id})")
    artist_albums:models.Album = cursor.fetchall()
    conn.close()

    return render_template('artist.html', artist_data=artist_data, artist_albums=artist_albums)