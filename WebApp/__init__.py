import os

from flask import Flask
from WebApp import sqlutil

#from flask import session
#from flask_session import Session
app = Flask(__name__)


con = sqlutil.get_connection()
if con is None:
    app.logger.error("Could not connect to Wizard DB")
    con = sqlutil.get_connection('SQL_PGDB')
    if con is None:
        app.logger.fatal("Could not connect to PG DB")
        raise Exception("Could not connect to PG DB, check postgresql setup")
    else:
        app.logger.info("Connected to PG DB")
        cur = con.cursor()

        app.logger.info("Creating Wizard DB")
        cur.execute("CREATE DATABASE wizard")

        cur.close()
        con.close()

        # This does not work, use insert tab cause that for some reason works
        con = sqlutil.get_connection() # Connect to newly created DB
        app.logger.info("Connected to Wizard DB")
        cur = con.cursor()
        app.logger.info("Populating DB")

        sql_cmd = open(os.getcwd() + "/db/init.sql", "r").read()

        cur.execute(sql_cmd)

        data = [
            "Artist", "Album", "Track"
        ]
        links = [
            "ArtistAlbum", "AlbumTrack"
        ]

        for elm in data:
            cmd =  open(f"{os.getcwd()}/db/insert{elm}.sql").read()
            cur.execute(cmd)

        for elm in links:
            cmd =  open(f"{os.getcwd()}/db/insert{elm}Link.sql").read()
            cur.execute(cmd)

        app.logger.info("Finished populating DB")

else:
    app.logger.info("Connected to Wizard DB")

# Init database always, creates tables if not exist
with open(os.path.join(os.getcwd(), "db/init.sql")) as f:
    sql_commands = f.read().split(";")


cur = con.cursor()

for command in sql_commands:
    command = command.strip()
    if command:
        cur.execute(command)

con.close()



# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'

# TEMPLATE
# from WebApp.Routes.PAGE import PAGE
# app.register_blueprint(PAGE)
app.template_folder = "./Templates"

@app.context_processor
def handle_context():
    return dict(os=os)

def register_blueprints(_app, _blueprints):
    for bp in _blueprints:
        _app.register_blueprint(bp)

from WebApp.Routes import Home, Insert, Artist, Album, Track, Search, Linker
app.register_blueprint(Home.Home)
app.register_blueprint(Insert.Insert)
app.register_blueprint(Artist.Artist)
app.register_blueprint(Album.Album)
app.register_blueprint(Track.Track)
app.register_blueprint(Search.Search)
app.register_blueprint(Linker.Linker)