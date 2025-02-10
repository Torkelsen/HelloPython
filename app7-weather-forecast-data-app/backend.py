import pandas as pd
import requests
from typing import List, Dict, Any, Tuple
import os
from datetime import date, timedelta

APIKEY = os.getenv("OPENWEATHERMAPAPIKEY")

def get_coordinates(city_name) -> Tuple[float, float]:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},NO&limit={1}&appid={APIKEY}"
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lon = response[0]["lon"]
    return lat, lon


def get_data(place: str, forecast_days: int) -> List[Dict[str, Any]]:
    lat, lon = get_coordinates(place)
    params = {
        "lat": lat,
        "lon": lon,
        "units": "metric",
        "appid": APIKEY,
    }
    url = f"http://api.openweathermap.org/data/2.5/forecast"
    response = requests.get(url, params=params).json()

    try:
        response = requests.get(url, params=params)
        # Raise an error for bad HTTP status codes
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        # Enable logging for prod
        raise err

    data = response.json()

    if "list" not in data:
        raise ValueError("Unexpected response format: missing 'list' key")

    # Using Pandas for proper filtering
    weather_df = pd.DataFrame(data['list'])
    weather_df['dt_txt'] = pd.to_datetime(weather_df['dt_txt'])

#    # List comprehension - nice for simple transformations
#    weather_data = [
#        {
#            "weather_icon": item["weather"][0]["icon"],
#            "temperature": item["main"]["temp"],
#            "date_time": item["dt_txt"]
#        }
#        for item in data["list"]
#    ]

    final_date = date.today() + timedelta(days=forecast_days)
    # Process each forecast item, building a list of desired weather information.
    weather_data: List[Dict[str, Any]] = []
    for _, item in weather_df[weather_df['dt_txt'].dt.date <= pd.to_datetime(final_date).date()].iterrows():
        try:
            weather_icon = item["weather"][0]["main"]
            temperature = item["main"]["temp"]
            date_time = item["dt_txt"]
        except (KeyError, IndexError) as err:
            # Optionally log this error and continue processing other items.
            continue

        weather_data.append({
            "weather_icon": weather_icon,
            "temperature": temperature,
            "date_time": date_time
        })

    return weather_data