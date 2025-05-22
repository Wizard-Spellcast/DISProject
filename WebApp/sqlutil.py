import os

import psycopg2
from dotenv import load_dotenv


def get_connection():
    # Load .env file contents
    load_dotenv()

    # Get connection string from .env file
    cs = os.environ.get('CONNECTION_STRING')
    conn = psycopg2.connect(cs)
    conn.autocommit = True
    return conn