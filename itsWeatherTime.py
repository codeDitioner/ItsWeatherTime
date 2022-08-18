# Posts

import os
import requests
import json
import datetime

def weather_today(city):
    """
    Returns a string with hourly weather forecast for the day.
    Location must be specified as "city,us".
    """
    # Grab API KEY from local environment
    api_key = os.getenv('OPENWEATHERMAP_API')

    # Url for forecast data in seattle
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city},us&units=imperial&appid={api_key}'
    r = requests.get(url)

    # Assign data in Python format using json
    data = json.loads(r.text)
    today = datetime.datetime.today().date()
    total_forecast = ''
    # Iterate through each item in key 'list'
    for d in data['list']:
        temp_dt = datetime.datetime.fromtimestamp(d['dt']) # converts date to YYYY-MM-DD HH:MM:SS format
        if temp_dt.date() <= today: # Checks if data is from today
            main_weather = d['weather'][0]['main'] # Extracts weather information
            temperature = int(d['main']['temp'])
            wind_speed = int(d['wind']['speed'])
            current_forecast = f"Forecast time is: {temp_dt}, and weather is {main_weather.lower()} in {city}. The temperature is"\
                               f" {temperature} degrees with winds of {wind_speed} mph."
            total_forecast += current_forecast + '\n\n'
    return total_forecast





