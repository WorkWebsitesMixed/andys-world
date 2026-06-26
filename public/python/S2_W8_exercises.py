# ============================================================
#  SPRINT 2 · WEEK 8 — Exercise Set
#  Topic: requests, JSON, HTTP GET, API calls
# ============================================================


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — READ THE STRUCTURE
#  The dict below simulates a real API response.
#  Answer each question with a print statement — no guessing.
# ════════════════════════════════════════════════════════════

api_response = {
    "city": "Medellin",
    "cod": 200,
    "main": {
        "temp": 22.4,
        "feels_like": 23.1,
        "humidity": 72
    },
    "weather": [
        {"id": 801, "description": "few clouds", "icon": "02d"}
    ],
    "wind": {"speed": 3.5, "deg": 180}
}

# TODO: print the city name
# TODO: print the temperature
# TODO: print the weather description
# TODO: print the wind speed
# TODO: print the icon code from inside the weather list


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — BUILD THE WEATHER FUNCTION
#  Complete the function below so it returns a formatted string.
#  Test it with the dict from Exercise 1 (no real API key needed).
# ════════════════════════════════════════════════════════════

def format_weather(data):
    """Takes an API response dict, returns a one-line summary string."""
    city        = data["city"]
    temp        = data["main"]["temp"]
    description = data["weather"][0]["description"]
    # TODO: return an f-string like:
    # "Medellin: 22.4C, few clouds"
    return TODO


print(format_weather(api_response))


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — ERROR HANDLING
#  Write a function  safe_get_weather(city, api_key)  that:
#    - Makes the real API call
#    - If cod == 200: returns the formatted weather string
#    - If cod != 200: returns "Error: {message from API}"
#  Test it with a fake city name ("Zzzzland") to trigger the error.
# ════════════════════════════════════════════════════════════

import requests

def safe_get_weather(city, api_key):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    url      = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    # TODO: complete this function
    pass


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — MULTI-CITY REPORT
#  Given the list of cities below, fetch weather for each one
#  and print a report. Handle errors gracefully.
# ════════════════════════════════════════════════════════════

cities = ["Medellin", "Bogota", "Cartagena", "Zzzzland"]

API_KEY = "YOUR_API_KEY_HERE"   # fill in your key

for city in cities:
    # TODO: call safe_get_weather and print the result


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: WEATHER COMPARISON
#  Fetch weather for 3 real cities.
#  Find the hottest and coldest ones.
#  Print a comparison table:
#    City        | Temp  | Condition
#    Medellin    | 22.4C | few clouds
#    Bogota      | 14.1C | overcast clouds
#    Cartagena   | 31.2C | clear sky
#    Hottest: Cartagena | Coldest: Bogota
# ════════════════════════════════════════════════════════════

# Write your code here:
