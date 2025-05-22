from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

from WebApp.Routes.Home import Home

Insert = Blueprint('Insert', __name__)

@Insert.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'GET':
        return render_template("insert.html")
    else:
        return redirect("/")