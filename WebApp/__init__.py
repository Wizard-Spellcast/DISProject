from flask import Flask
import psycopg2

#from flask import session
#from flask_session import Session


app = Flask(__name__)

# app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
db = "dbname='nodeDB' user='postgres' host='127.0.0.1' password = 'admin'"
conn = psycopg2.connect(db)

# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'

# TEMPLATE
# from WebApp.Routes.PAGE import PAGE
# app.register_blueprint(PAGE)

from WebApp.Routes.Node import Node
app.register_blueprint(Node)