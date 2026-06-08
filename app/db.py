import os
import psycopg
from psycopg.rows import dict_row

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
else:
    conn = None


def get_db():
    if conn:
        return conn
    else:
        raise RuntimeError("Database not configured correctly")