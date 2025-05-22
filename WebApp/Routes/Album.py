from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Album = Blueprint('Album', __name__)

@Album.route("/album")
def album_search():
    return render_template("search.html", table='album')


@Album.route("/album/<album_id>")
def album(album_id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM album WHERE id = {album_id}")

    album_data:models.Album = cursor.fetchone()
    conn.close()

    return render_template('album.html', album_data=album_data)