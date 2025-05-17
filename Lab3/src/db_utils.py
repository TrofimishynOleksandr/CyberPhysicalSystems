import json
import psycopg2

def get_connection():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)["db"]

    conn = psycopg2.connect(
        dbname=config["name"],
        user=config["user"],
        password=config["password"],
        host=config["host"],
        port=config["port"]
    )
    return conn
