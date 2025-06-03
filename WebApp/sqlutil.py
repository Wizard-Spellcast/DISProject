import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask.globals import app_ctx
from psycopg2 import OperationalError


def get_connection(env_dbname:str = None):
    # Load .env file contents
    load_dotenv()

    if env_dbname is None:
        conn_str = f"dbname='{os.environ.get("SQL_WIDB")}' "
    else:
        conn_str = f"dbname='{os.environ.get(env_dbname)}' "

    conn_str += (f"user='{os.environ.get("SQL_USER")}' "
                 f"host='{os.environ.get("SQL_HOST")}' "
                 f"password='{os.environ.get("SQL_PASS")}'")


    try:
        conn = psycopg2.connect(conn_str)
        conn.autocommit = True
        return conn

    # Dumb but works for now, should be more specific
    except OperationalError as e:
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

