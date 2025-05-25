from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Track = Blueprint('Track', __name__)

@Track.route("/track")
def track_search():
    return redirect(url_for('Search.search', table='track'))


@Track.route("/track/<id>")
def track_lookup(id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM track WHERE id = {id}")

    track_data:models.Track = cursor.fetchone()
    conn.close()

    return render_template('track.html', track_data=track_data)