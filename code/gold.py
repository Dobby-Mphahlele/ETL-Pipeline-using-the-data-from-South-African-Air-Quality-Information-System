import pandas as pd
from datetime import datetime

# Load the CSV into a DataFrame
file_path = './processed_data.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Ensure 'date' and 'time' are in the correct format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d').dt.date  # Convert date in YYYY-MM-dd format
df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour  # Extract hour from time (HH:00:00 format)
df['minute'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.minute  # Extract minute (always 00 in your format)

# Extract additional time components
df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek  # Extract day of the week (0=Monday, 6=Sunday)
df['month'] = pd.to_datetime(df['date']).dt.month  # Extract month (1=January, 12=December)
df['year'] = pd.to_datetime(df['date']).dt.year  # Extract year (e.g., 2025)

# Normalize the station dimension (unique station names and locations)
station_dim = df[['station_name', 'location']].drop_duplicates().reset_index(drop=True)
station_dim['station_id'] = station_dim.index + 1  # Create unique station_id

# Normalize the time dimension
time_dim = df[['date', 'hour', 'minute', 'day_of_week', 'month', 'year']].drop_duplicates().reset_index(drop=True)
time_dim['time_id'] = time_dim.index + 1  # Create unique time_id

# Merge the station_id and time_id into the fact table
df = df.merge(station_dim[['station_name', 'station_id']], on='station_name', how='left')
df = df.merge(time_dim[['date', 'hour', 'minute', 'time_id']], on=['date', 'hour', 'minute'], how='left')

# Create the fact table
fact_table = df[['station_id', 'time_id', 'aqi', 'dominentpol', 'dew', 'h', 'p', 'pm10', 'pm25', 'so2', 't', 'w', 'wg', 'no2', 'o3', 'r', 'co']]

# Save the dimensions and fact table to CSV files (or to your data warehouse)
station_dim.to_csv('station_dimension.csv', index=False)
time_dim.to_csv('time_dimension.csv', index=False)
fact_table.to_csv('fact_table.csv', index=False)

print("Data modeled and saved as station_dimension.csv, time_dimension.csv, and fact_table.csv.")
