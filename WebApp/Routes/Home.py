from flask import render_template, url_for, flash, redirect, request, Blueprint
from WebApp import models, sqlutil
import psycopg2

Home = Blueprint('Home', __name__)

@Home.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')