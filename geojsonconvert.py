import json
import pandas as pd

# Ensure that the geojsonconvert function is defined correctly in geojsonconvert.py
def geojsonconvert(data):
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for item in data['items']:  # Adjust the key based on your JSON structure
        feature = {
            "type": "Feature",
            "properties": {
                "name": item['name'],  # Adjust the key based on your JSON structure
                # Add other properties as needed
            },
            "geometry": {
                "type": "Point",  # Adjust the geometry type if needed
                "coordinates": item['coordinates']  # Adjust the key based on your JSON structure
            }
        }
        geojson['features'].append(feature)
    return geojson

# Open the JSON file and read its content
with open('./field.json', 'r') as f:
    quads = json.load(f)

# Convert to GeoJSON
df_quads = geojsonconvert(quads)

# Optional: Convert the GeoJSON to a DataFrame and display its info
df_quads_df = pd.DataFrame(df_quads['features'])
df_quads_df.info()
