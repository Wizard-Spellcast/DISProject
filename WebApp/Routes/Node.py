from flask import render_template, url_for, flash, redirect, request, Blueprint

Node = Blueprint('Node', __name__)

@Node.route("/create", methods=['GET', 'POST'])
def create():
    return