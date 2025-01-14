import asyncio
import aiohttp
import json
import csv

API_TOKEN = "5ab68ec5cb99eb89461c555b09a1c02c3f426fed"
FEED_URL = "https://api.waqi.info/feed/geo:{lat};{lon}/?token={token}"

async def fetch_air_quality_data(session, lat, lon):
    """Fetch air quality data for the given latitude and longitude."""
    url = FEED_URL.format(lat=lat, lon=lon, token=API_TOKEN)
    async with session.get(url) as response:
        data = await response.json()
        if data["status"] == "ok":
            return data["data"]
        else:
            raise Exception(f"Error fetching data for coordinates ({lat}, {lon}): {data['data']}")

def read_coordinates_from_csv(file_path):
    """Read latitude and longitude from a CSV file."""
    coordinates = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        print("CSV Headers:", csv_reader.fieldnames)
        
        for row in csv_reader:
            latitude = float(row['Latitude'])
            longitude = float(row['Longitude'])
            coordinates.append((latitude, longitude))
    return coordinates

async def main():
    try:
        
        file_path = 'south_africa_air_quality_stations.csv'  # Path to the CSV file
        
        # Reading coordinates from CSV
        coordinates = read_coordinates_from_csv(file_path)

        # Useing aiohttp's ClientSession for making asynchronous requests
        async with aiohttp.ClientSession() as session:
            tasks = []
            for lat, lon in coordinates:
                tasks.append(fetch_air_quality_data(session, lat, lon))
            
            # Wait for all tasks to complete
            all_air_quality_data = await asyncio.gather(*tasks)

            # Save the results to a JSON file
            output_file = "air_quality_data.json"
            with open(output_file, "w") as f:
                json.dump(all_air_quality_data, f, indent=4)
            
            print(f"Data successfully saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
