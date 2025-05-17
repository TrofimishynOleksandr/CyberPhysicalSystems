import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_utils import get_connection

import json


def load_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM temperature_readings LIMIT 1)")
    exists = cur.fetchone()[0]

    if exists:
        print("Data already exists in the database. Skipping load.")
        cur.close()
        conn.close()
        return
    
    with open("config.json", "r", encoding="utf-8") as f:
        csv_path = json.load(f)["csv_path"]

    df = pd.read_csv(csv_path, skiprows=10)
    df.columns = ['timestamp', 'temperature']
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y%m%dT%H%M")

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO temperature_readings (timestamp, temperature) VALUES (%s, %s)",
            (row['timestamp'], row['temperature'])
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded successfully.")


if __name__ == "__main__":
    load_data()
