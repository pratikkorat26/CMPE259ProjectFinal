import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define time range for 1 year of daily sleep data
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
daily_timestamps = pd.date_range(start=start_date, end=end_date, freq='D')

# Simulate sleep_log data
np.random.seed(42)
sleep_data = {
    "timestamp": daily_timestamps,
    "duration": np.random.normal(loc=7.5, scale=1.0, size=len(daily_timestamps)).round(2),  # in hours
    "quality_score": np.random.randint(60, 100, size=len(daily_timestamps)),  # score out of 100
    "stage_deep": np.random.normal(loc=1.5, scale=0.3, size=len(daily_timestamps)).round(2),
    "stage_rem": np.random.normal(loc=2.0, scale=0.4, size=len(daily_timestamps)).round(2),
    "stage_light": np.random.normal(loc=4.0, scale=0.6, size=len(daily_timestamps)).round(2)
}

df_sleep_log = pd.DataFrame(sleep_data)

# Create time range for hourly heart-related metrics
hourly_timestamps = pd.date_range(start=start_date, end=end_date, freq='h')

# Simulate heart-related metrics
heart_metrics_data = {
    "timestamp": hourly_timestamps,
    "heart_rate": np.random.normal(loc=72, scale=8, size=len(hourly_timestamps)).astype(int),
    "systolic": np.random.normal(loc=120, scale=10, size=len(hourly_timestamps)).astype(int),
    "diastolic": np.random.normal(loc=80, scale=7, size=len(hourly_timestamps)).astype(int),
    "oxygen_level": np.random.normal(loc=98, scale=1.5, size=len(hourly_timestamps)).round(1)
}

df_heart_metrics = pd.DataFrame(heart_metrics_data)

# Save both tables into one SQLite database
combined_db_path = "./fitness_health_tracker.db"
with sqlite3.connect(combined_db_path) as conn:
    df_sleep_log.to_sql("sleep_log", conn, if_exists="replace", index=False)
    df_heart_metrics.to_sql("heart_metrics", conn, if_exists="replace", index=False)

print(combined_db_path)