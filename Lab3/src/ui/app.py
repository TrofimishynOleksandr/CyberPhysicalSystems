import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_utils import get_connection
from ml.predict import predict_next_day

conn = get_connection()
df = pd.read_sql("SELECT * FROM temperature_readings", conn)
conn.close()

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date

available_dates = sorted(df['date'].unique(), reverse=True)
selected_date = st.date_input("Оберіть дату для прогнозу погоди наступного дня", max(available_dates), min_value=min(available_dates), max_value=max(available_dates))

day_data = df[df['date'] == selected_date]['temperature'].tolist()

if not day_data:
    st.warning("Немає даних для вибраної дати.")
else:
    prediction = predict_next_day(day_data)

    st.title(f"Прогноз температури на {selected_date + pd.Timedelta(days=1)}")
    for i, temp in enumerate(prediction):
        st.write(f"{i}:00 -> {temp:.2f}°C")
