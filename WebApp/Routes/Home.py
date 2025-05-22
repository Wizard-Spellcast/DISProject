from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Home = Blueprint('Home', __name__)
Search = Blueprint('Search', __name__)

def wrap(html_text):
    return render_template("head_wrapper.html", html_text)

@Home.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        return redirect(url_for("search"))

@Home.route("/a/<artist_id>")
def artist(artist_id:str=None):
    conn = sqlutil.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM artist WHERE id = {artist_id}")

    artist_data:models.Artist = cursor.fetchone()

    return render_template('artist.html', artist_data=artist_data)

@Search.route("/search", methods=['GET', 'POST'])
def Search():
    return render_template("search.html")