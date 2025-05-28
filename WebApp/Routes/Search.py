import os
from re import search

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask.globals import app_ctx

from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

Search = Blueprint('Search', __name__)

@Search.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('q')
        table = request.args.get('t')
        return redirect(url_for("Search.search", t=table, q=query))

    query = request.args.get('q')
    table = request.args.get('t')
    if query is None:
        return render_template('search.html', t=table)
    else: # if system search
        conn = sqlutil.get_connection()
        cur = conn.cursor()

        q_result = []

        if table is None:
            cur.execute(f"SELECT * FROM artist WHERE name ~ '{query}'")
            q_result_artist = cur.fetchall()
            cur.execute(f"SELECT * FROM album WHERE name ~ '{query}'")
            q_result_album = cur.fetchall()
            cur.execute(f"SELECT * FROM track WHERE name ~ '{query}'")
            q_result_track = cur.fetchall()
            q_result = [q_result_artist, q_result_album, q_result_track, q_result_track]
        else:
            cur.execute(f"SELECT * FROM {table} WHERE name ~ '{query}'")
            q_result = [cur.fetchall()]


        app_ctx.app.logger.info(f"Found {len(q_result)} results in all tables by query: {table}")

        return render_template('search.html', t=table, q=query, q_result=q_result)