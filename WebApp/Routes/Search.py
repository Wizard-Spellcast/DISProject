import os
from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

Search = Blueprint('Search', __name__)

@Search.route("/search?table=<table>", methods=['GET', 'POST'])
def search(table:str = None):
    if request.method == 'GET':
        return render_template('search.html', table=table)
    else: #
        table = request.form.get('table')
        term = request.form.get('query')

        conn = sqlutil.get_connection()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {table} WHERE name LIKE '{term}'")
        q_result = cur.fetchall()

        lt = None
        match table:
            case 'artist':  lt = 'Artist.artist_lookup'
            case 'album':   lt = 'Album.album_lookup'
            case 'track':   lt = 'Track.track_lookup'

        return render_template('search.html', table=table, q_result=q_result, lt=lt)