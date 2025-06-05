import json
import os
from flask import render_template, url_for, flash, redirect, request, Blueprint, Flask
from flask.globals import app_ctx
import re

from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

app = Flask("WebApp")

# num predicate. Is regex
nump = re.compile("[0-9]+")


def isnum(s):
    bool(nump.fullmatch(s))


def artistToId(s, cur):
    if isnum(s):
        cur.execute(f"select * from artist where id = {s}")
        c = cur.fetchall()      # gets columns
        if c.length == 0:       # if no id corresponds to an artist; -1
            return -1
        return int(s)           # if s was valid id, then cast to int
    cur.execute(f"select distinct id from artist where name = '{s}'")
    c = cur.fetchall()          # gets columns
    if len(c) == 1:
        return int(c[0][0])
    return -1                   # if not exactly one artist; -1


Insert = Blueprint('Insert', __name__)


@Insert.route("/insert_select", methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        a_table = request.form.get('t')
        a_action = request.form.get('a')
        return redirect(url_for('Insert.insert_specific', t=a_table, a = a_action))
    else:
        return render_template("insert_select.html")

@Insert.route("/insert_specific", methods=['GET', 'POST'])
def insert_specific():
    if request.method == 'POST':
        a_table = request.args.get('t')
        a_action = request.args.get('a')

        con = sqlutil.get_connection()
        cur = con.cursor()

        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{a_table}'")
        columns = cur.fetchall()

        keys = []
        values = []

        items = dict(request.form.items())

        for column in columns:
            key = column[0]

            keys.append(key)
            value_data = items[key]

            match column[1]:
                case 'integer':
                    values.append(value_data)
                case 'character varying':
                    values.append(f"'{value_data}'")
                case _:
                    app_ctx.app.logger.error(f"Unknown column type parsed: {column[1]}")

        match a_action:
            case 'INSERT':
                match a_table:
                    case 'album':
                        ai = keys.index("artistowner")
                        ni = keys.index("name")
                        ii = keys.index("id")
                        id = artistToId(values[ai], cur)
                        app.logger.info(f"id: {id}")
                        if id != -1:
                            cur.execute(f"""
                                        insert into album values (
                                            {values[ii]}, {values[ni]}, {id}
                                        )""")
                    case _:
                        cur.execute(f"INSERT INTO {a_table} ({", ".join(keys)}) VALUES ({", ".join(values)})")
            case 'UPDATE':
                upd_string = f"UPDATE {a_table} SET {", ".join([f"{k}={v}" for k, v in zip(keys, values)])} WHERE id = {values[0]}"
                cur.execute(upd_string)
            case 'DELETE':
                # Could be done via just the id? but to ensure that the user does not delete the wrong entry we must confirm all data
                del_string = f"DELETE FROM {a_table} WHERE {" AND ".join([f"{k}={v}" for k,v in zip(keys, values)])}"
                cur.execute(del_string)

        return redirect(url_for('Insert.insert_specific', t=a_table, a = a_action))
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

"""
@Insert.route("/insert", methods=['GET', 'POST'])
def insert_data():
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
        """
