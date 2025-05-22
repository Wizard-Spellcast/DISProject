from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Artist = Blueprint('Artist', __name__)

@Artist.route("/artist/<artist_id>")
def artist(artist_id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM artist WHERE id = {artist_id}")

    artist_data:models.Artist = cursor.fetchone()
    conn.close()

    return render_template('artist.html', artist_data=artist_data)