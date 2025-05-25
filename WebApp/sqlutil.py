import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask


def get_connection(conn_str:str = 'CONNECTION_STRING'):
    # Load .env file contents
    load_dotenv()

    # Get connection string from .env file
    cs = os.environ.get(conn_str)
    try:
        conn = psycopg2.connect(cs)
        conn.autocommit = True
        return conn

    # Dumb but works for now, should be more specific
    except Exception as e:
        return None

def insert_all_query(table, data) -> str: return f"""
    INSERT INTO {table} VALUES {data};
    """

#
# eg. form = "artist(id, name)", csv_path = os.getcwd() + "/db/csv/artist.csv"
#
def copy_csv(form:str, csv_path:str) -> str: return f"""
    COPY {form}
    FROM '{csv_path}'
    DELIMITER ','
    CSV HEADER;
"""

