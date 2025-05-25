import json
import os
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask.globals import app_ctx

from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

Insert = Blueprint('Insert', __name__)

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