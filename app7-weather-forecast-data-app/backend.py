import requests
from typing import List, Dict, Any, Tuple
import os

APIKEY = os.getenv("OPENWEATHERMAPAPIKEY")

def get_coordinates(city_name) -> Tuple[float, float]:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},NO&limit={1}&appid={APIKEY}"
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lon = response[0]["lon"]
    return lat, lon


def get_data(place: str, days: int, option: str) -> List[Dict[str, Any]]:
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

    # TODO: add date range filtering up to today + days to limit data returned to frontend

#    # List comprehension - nice for simple transformations
#    weather_data = [
#        {
#            "weather_icon": item["weather"][0]["icon"],
#            "temperature": item["main"]["temp"],
#            "date_time": item["dt_txt"]
#        }
#        for item in data["list"]
#    ]

    # Process each forecast item, building a list of desired weather information.
    weather_data: List[Dict[str, Any]] = []
    for item in data["list"]:
        try:
            weather_icon = item["weather"][0]["icon"]
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


get_data("Sveio", 1, "Sky")