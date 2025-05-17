import psycopg2
import psycopg2.extensions
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_utils import get_connection

import json

sys.stdout.reconfigure(encoding='utf-8')

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)["db"]

def create_database():
    try:
        config = load_config()
        DB_NAME = config["name"]

        conn = get_connection()
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cur.fetchone()

        if not exists:
            cur.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error creating database:", str(e))

if __name__ == "__main__":
    create_database()
