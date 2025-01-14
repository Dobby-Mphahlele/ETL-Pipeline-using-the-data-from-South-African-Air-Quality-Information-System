'''
import pandas as pd

file_path = './raw_data.csv'
df = pd.read_csv(file_path)

# Removing duplicates
df = df.drop_duplicates()

# Extracting station_name and location
df['station_name'] = df['station'].str.split(',').str[0]
df['location'] = df['station'].str.split(',').str[1]
df = df.drop(columns=['station'])

# Replacing NaN values with 0
df = df.fillna(0)

# Renaming the 'time' column to 'date_time'
df = df.rename(columns={'time': 'date_time'})

# Extract 'date' and 'time' from 'date_time'
df['date'] = pd.to_datetime(df['date_time']).dt.date
df['time'] = pd.to_datetime(df['date_time']).dt.time
df = df.drop(columns=['date_time'])

# Replace location with station_name if location is 'None' or 'South Africa'
df.loc[df['location'].isin(['None', 'South Africa']), 'location'] = df['station_name']


# Reordering columns to make station_name and location appear first
columns_order = ['station_name', 'location'] + [col for col in df.columns if col not in ['station_name', 'location']]
df = df[columns_order]

output_file = 'processed_data.csv'
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")
print(df.head())

'''

import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'raw_data.csv'

# Load the CSV into a DataFrame
df = pd.read_csv(file_path)

df = df.drop([
              'attributions', 
              'city.geo', 
              'city.url', 
              'city.location', 
              'time.tz', 
              'time.iso',
              'time.v',
              'forecast.daily.o3', 
              'forecast.daily.pm10', 
              'forecast.daily.pm25',
              'forecast.daily.uvi', 
              'debug.sync'],  axis=1)


# Extract station_name and location
df['station_name'] = df['station'].str.split(',').str[0]
df['location'] = df['station'].str.split(',').str[1]

# Drop the station column
df = df.drop(columns=['station'])

# Reorder columns to make station_name and location appear first
columns_order = ['id','station_name', 'location'] + [col for col in df.columns if col not in ['id', 'station_name', 'location']]
df = df[columns_order]

# Replace NaN values with 0
df = df.fillna(0)

# Rename the 'time' column to 'date_time'
df = df.rename(columns={'time': 'date_time'})

# Extract 'date' and 'time' from 'date_time'
df['date'] = pd.to_datetime(df['date_time']).dt.date
df['time'] = pd.to_datetime(df['date_time']).dt.time

# Drop the date_time column
df = df.drop(columns=['date_time'])

# Replace location with station_name if location is 'None' or 'South Africa'
df.loc[df['location'] == ' None', 'location'] = df['station_name']
df.loc[df['location'] == ' South Africa', 'location'] = df['station_name']

# Save the modified DataFrame to a new CSV file
output_file = 'processed_data.csv'
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")
