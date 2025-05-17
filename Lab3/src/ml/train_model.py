from sqlalchemy import create_engine
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_utils import get_connection

conn = get_connection()
engine = create_engine('postgresql://user:password@localhost:5432/weather_forecast')
df = pd.read_sql("SELECT * FROM temperature_readings", engine)
conn.close()

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour

data_by_day = df.groupby(['date'])['temperature'].apply(list)
data_by_day = data_by_day[data_by_day.apply(lambda x: len(x) == 24)]

X = []
y = []
dates = list(data_by_day.index)

for i in range(30, len(dates)-1):
    X.append(data_by_day[dates[i]])
    y.append(data_by_day[dates[i+1]])

model = RandomForestRegressor()
model.fit(X, y)
joblib.dump(model, 'src/ml/model.joblib')