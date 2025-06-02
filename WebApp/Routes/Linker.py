import ast
import json
import os
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask.globals import app_ctx

from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

Linker = Blueprint('Linker', __name__)

@Linker.route("/linker_select", methods=['GET', 'POST'])
def linker():
    if request.method == 'POST':
        t1 = request.form.get('t1')
        t2 = request.form.get('t2')
        return redirect(url_for("Linker.linker_specific", t1=t1, t2=t2))
    else:
        return render_template("linker_select.html")

@Linker.route("/linker_specific", methods=['GET', 'POST'])
def linker_specific():
    if request.method == 'POST':
        t1 = request.args.get('t1')
        t2 = request.args.get('t2')

        t1_selection = None
        t2_selection = []

        items = request.form.items()
        for index, (k, v) in enumerate(items):
            if index == 0:
                data = ast.literal_eval(v)
                t1_selection = data[0]
            else:
                data = ast.literal_eval(k)
                t2_selection.append(data[0])

        con = sqlutil.get_connection()
        cur = con.cursor()

        for t2_id in t2_selection:
            # Ignore conflicts, user inserted already existing link
            update_string = f"INSERT INTO {t1}{t2}link VALUES({t1_selection}, {t2_id}) ON CONFLICT DO NOTHING"
            cur.execute(update_string)

        cur.close()
        con.close()
        return redirect(url_for('Linker.linker_specific', t1=t1, t2=t2))
    else:
        a_table1 = request.args.get('t1')
        a_table2 = request.args.get('t2')
        a_extra = request.args.get('ex')
        conn = sqlutil.get_connection()
        cur = conn.cursor()

        cur.execute(f"SELECT id, name FROM {a_table1}")
        t1_data = cur.fetchall()

        cur.execute(f"SELECT id, name FROM {a_table2}")
        t2_data = cur.fetchall()

        cur.close()
        conn.close()
        return render_template("linker_specific.html",
                               t1=a_table1, t2=a_table2, t1_data=t1_data, t2_data=t2_data)
