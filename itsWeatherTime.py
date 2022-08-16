import os
import requests
import json
import datetime

def rain_today(city):
    """
    Returns True if it is going to rain today.
    Location must be specified as "city,us".
    """
    rain = False
    # Grab api key from local environment
    api_key = os.getenv('OPENWEATHERMAP_API')

    # Url for forecast data in seattle
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city},us&units=imperial&appid={api_key}'
    r = requests.get(url)

    # Assign data in Python format using json
    data = json.loads(r.text)
    today = datetime.datetime.today().date()
    # data_readable = json.dumps(data['list'], indent=4) - internal use to check data in readable format
    # print(data_readable) - internal use to check data
    # Iterate through each item in key 'list'
    for d in data['list']:
        temp_dt = datetime.datetime.fromtimestamp(d['dt']) # converts date to YYYY-MM-DD HH:MM:SS format
        if temp_dt.date() <= today: # Checks if data is from today
            main_weather = d['weather'][0]['main'] # Extracts weather information
            if main_weather in ['Rain', 'rain']:
                rain = True
            print(f"time is: {temp_dt}, and weather is {main_weather} in {city}.")
    return rain

rain_today('Seattle')





