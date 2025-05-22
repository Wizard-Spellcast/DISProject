import os

from flask import Flask
from WebApp import sqlutil

#from flask import session
#from flask_session import Session

def build_db():
    conn = sqlutil.get_connection()
    curr = conn.cursor()

    with open(os.path.join(os.getcwd(), "db/init.sql")) as f:
        sql_commands = f.read().split(";")

    for command in sql_commands:
        command = command.strip()
        if command:
            curr.execute(command)

    curr.close()
    conn.close()

cur = sqlutil.get_connection().cursor()
cur.execute("SELECT datname FROM pg_database where datname = 'wizard'")
if len(cur.fetchall()) == 0:
    # Wizard DB must not exist
    build_db()


app = Flask(__name__)


# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'

# TEMPLATE
# from WebApp.Routes.PAGE import PAGE
# app.register_blueprint(PAGE)
app.template_folder = "./Templates"

from WebApp.Routes import Home, Insert
app.register_blueprint(Home.Home)
app.register_blueprint(Insert.Insert)