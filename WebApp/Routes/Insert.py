import json
import os
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask.globals import app_ctx

from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

Insert = Blueprint('Insert', __name__)

@Insert.route("/insert_select", methods=['GET', 'POST'])
def insert_select():
    if request.method == 'POST':
        a_table = request.form.get('t')
        a_action = request.form.get('a')
        return redirect(url_for('Insert.insert_specific', t=a_table, a = a_action))
    else:
        return render_template("insert_select.html")

@Insert.route("/insert_specific", methods=['GET', 'POST'])
def insert_specific():
    if request.method == 'POST':
        a_table = request.form.get('t')
        a_action = request.form.get('a')
        return redirect(url_for('Home.home'))
    else:
        a_table = request.args.get('t')
        a_action = request.args.get('a')
        conn = sqlutil.get_connection()
        cur = conn.cursor()
        cur.execute(f"select * from {a_table} LIMIT 0")

        column_names = [desc.name for desc in cur.description]
        cur.execute(f"SELECT COUNT(*) FROM {a_table}")
        base_values = cur.fetchall()[0][0]
        cur.close()
        conn.close()
        return render_template("insert_specific.html",
                               a_action=a_action,
                               a_table=a_table,
                               sql_fields = column_names,
                               base_values = base_values)


@Insert.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'GET':
        return render_template("insert.html")
    else:
        con = sqlutil.get_connection()
        cur = con.cursor()

        cur.execute(open(os.getcwd() + "/db/insertArtist.sql", "r").read())
        cur.execute(open(os.getcwd() + "/db/insertAlbum.sql", "r").read())
        cur.execute(open(os.getcwd() + "/db/insertTrack.sql", "r").read())
        cur.execute(open(os.getcwd() + "/db/insertGenre.sql", "r").read())

        cur.execute(open(os.getcwd() + "/db/insertArtistAlbumLink.sql", "r").read())
        cur.execute(open(os.getcwd() + "/db/insertAlbumTrackLink.sql", "r").read())
        cur.execute(open(os.getcwd() + "/db/insertTrackGenreLink.sql", "r").read())


        return redirect(url_for('Home.home'))