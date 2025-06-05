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
        q_table = request.args.get('t')
        return redirect(url_for("Search.search", t=q_table, q=query))

    query = request.args.get('q')
    q_table = request.args.get('t')
    if query is None:
        return redirect(url_for("Search.search", t=q_table, q=""))
    else: # if system search
        conn = sqlutil.get_connection()
        cur = conn.cursor()

        if q_table is None:
            tables = ["artist", "album", "track"]

            results = []

            for table in tables:
                cur.execute(f"SELECT * FROM {table} WHERE name ~ '{query}'")
                results.append(cur.fetchall())

            q_result = results
        else:
            cur.execute(f"SELECT * FROM {q_table} WHERE name ~ '{query}'")

            # Cursed but works with the html page to show only the requested table
            if q_table == "artist":
                q_result = [cur.fetchall(), None, None]
            elif q_table == "album":
                q_result = [None, cur.fetchall(), None]
            else:
                q_result = [None, None, cur.fetchall()]


        app_ctx.app.logger.info(f"Found {len(q_result)} results in all tables by query: {query}")

        return render_template('search.html', t=q_table, q=query, q_result=q_result)