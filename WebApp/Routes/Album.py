from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Album = Blueprint('Album', __name__)

@Album.route("/albums")
def albums():
    return redirect(url_for('Search.search', t='album'))


@Album.route("/album/<id>")
def album_lookup(id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM album WHERE id = {id}")

    album_data:models.Album = cursor.fetchone()
    conn.close()

    return render_template('album.html', album_data=album_data)