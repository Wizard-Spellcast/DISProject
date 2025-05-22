from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Track = Blueprint('Track', __name__)

@Track.route("/track")
def track_search():
    return render_template("search.html", table='track')


@Track.route("/track/<track_id>")
def track(track_id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM track WHERE id = {track_id}")

    track_data:models.Track = cursor.fetchone()
    conn.close()

    return render_template('track.html', track_data=track_data)