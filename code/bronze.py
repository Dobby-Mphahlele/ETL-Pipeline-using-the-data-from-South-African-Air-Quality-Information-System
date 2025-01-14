import json
import pandas as pd

# Loading the JSON data
with open('air_quality_data.json', 'r') as f:
    data = json.load(f)

# Normalizing the JSON to flatten the nested structure
df = pd.json_normalize(
    data,
    record_path=None,
    meta=[
        'city.name', 
        'aqi', 
        'time.s', 
        'dominentpol', 
        'iaqi.dew.v',
        'iaqi.h.v',
        'iaqi.p.v',
        'iaqi.pm10.v',
        'iaqi.pm25.v',
        'iaqi.r.v',
        'iaqi.so2.v',
        'iaqi.t.v',
        'iaqi.w.v',
        'iaqi.no2.v',       # Added 'no2'
        'iaqi.o3.v',        # Added 'o3'
        'iaqi.wg.v',        # Added 'wg'
        'iaqi.co.v'         # Added 'co'
    ],
    errors='ignore'
)

# Selecting and rename columns as per required fields
df = df.rename(columns={
    'idx' : 'id',
    'city.name': 'station',
    'aqi': 'aqi',
    'time.s': 'time',
    'dominentpol': 'dominentpol',
    'iaqi.dew.v': 'dew',
    'iaqi.h.v': 'h',
    'iaqi.p.v': 'p',
    'iaqi.pm10.v': 'pm10',
    'iaqi.pm25.v': 'pm25',
    'iaqi.r.v': 'r',
    'iaqi.so2.v': 'so2',
    'iaqi.t.v': 't',
    'iaqi.w.v': 'w',
    'iaqi.no2.v': 'no2',  # Renamed 'no2'
    'iaqi.o3.v': 'o3',    # Renamed 'o3'
    'iaqi.wg.v': 'wg',    # Renamed 'wg'
    'iaqi.co.v': 'co'     # Renamed 'co'
})

# Save to CSV
df.to_csv('raw_data.csv', index=False)

print("CSV file saved as 'raw_data.csv'")
