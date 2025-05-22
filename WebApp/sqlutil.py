import os

import psycopg2
from dotenv import load_dotenv

def get_connection(conn_str:str = 'CONNECTION_STRING'):
    # Load .env file contents
    load_dotenv()

    # Get connection string from .env file
    cs = os.environ.get(conn_str)
    try:
        conn = psycopg2.connect(cs)
        conn.autocommit = True
        return conn
    except Exception as e:
        return None
