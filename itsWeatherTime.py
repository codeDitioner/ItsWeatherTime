import os
import requests
import json

# Grab api key from local environment
api_key = os.getenv('OPENWEATHERMAP_API')

# Url for forecast data in seattle
url = f'https://api.openweathermap.org/data/2.5/forecast?q=seattle,us&units=imperial&appid={api_key}'
r = requests.get(url)

# Assign data in Python format using json
data = json.loads(r.text)

len(data['list'])
print(data['list'])