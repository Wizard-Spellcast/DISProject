import os

from flask import Flask
from WebApp import sqlutil

#from flask import session
#from flask_session import Session

def build_db():
    conn = sqlutil.get_connection("CONNECTION_STRING_PGDB")
    conn.cursor().execute("CREATE DATABASE wizard")
    conn.close()


app = Flask(__name__)

conn = sqlutil.get_connection()
if conn is None:
    conn = sqlutil.get_connection('CONNECTION_STRING_PGDB')
    if conn is None:
        print("Could not connect to PostgreSQL")
    else:
        print("Connected to PostgreSQL, but no database is set up")
        build_db()
else:
    print("Connected to PostgreSQL, database is set up")

cur = conn.cursor()

# Init database always, creates tables if not exist
with open(os.path.join(os.getcwd(), "db/init.sql")) as f:
    sql_commands = f.read().split(";")

for command in sql_commands:
    command = command.strip()
    if command:
        cur.execute(command)

conn.close()



# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'

# TEMPLATE
# from WebApp.Routes.PAGE import PAGE
# app.register_blueprint(PAGE)
app.template_folder = "./Templates"

from WebApp.Routes import Home, Insert, Artist, Album, Track
app.register_blueprint(Home.Home)
app.register_blueprint(Insert.Insert)
app.register_blueprint(Artist.Artist)
app.register_blueprint(Album.Album)
app.register_blueprint(Track.Track)