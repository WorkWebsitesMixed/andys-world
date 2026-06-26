# ============================================================
#  SPRINT 2 · WEEK 8 — APIs & JSON
#  Live Weather Fetcher
#
#  Before this session install the requests library:
#    pip install requests
#
#  Get a free API key at:  openweathermap.org  (free tier)
#  Fill in your API key below.
#  Run:  python S2_W8_template.py
# ============================================================

import requests

API_KEY = "YOUR_API_KEY_HERE"   # TODO: paste your OpenWeatherMap key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ── STEP 1: Your first API call ──────────────────────────────
# requests.get() sends an HTTP GET request to a URL.
# .json() converts the response body into a Python dictionary.

city = "Medellin"
url  = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data     = response.json()

print("RAW RESPONSE (just to see the structure):")
print(data)


# ── STEP 2: Check for errors ─────────────────────────────────
# The API returns a "cod" key: 200 = OK, 404 = city not found, etc.

if data["cod"] != 200:
    print(f"Error: {data['message']}")
else:
    print("Connection successful!")

# TODO: add a print that shows data["cod"] on its own


# ── STEP 3: Extract the fields you need ──────────────────────
# JSON becomes a nested dictionary. Use keys to drill in.

temp        = data["main"]["temp"]
feels_like  = data["main"]["feels_like"]
description = data["weather"][0]["description"]  # [0] = first item in a list
humidity    = data["main"]["humidity"]
wind_speed  = data["wind"]["speed"]

# TODO: print each variable to see its value


# ── STEP 4: Build a weather card ─────────────────────────────
print()
print("=" * 38)
print(f"  WEATHER — {city.upper()}")
print("=" * 38)
print(f"  Condition : {description.title()}")
print(f"  Temp      : {temp}C  (feels like {feels_like}C)")
# TODO: add humidity and wind_speed to the card


# ── STEP 5: Ask the user for any city ────────────────────────
def get_weather(city_name, api_key):
    """Fetches and returns weather data for any city."""
    url      = f"{BASE_URL}?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

city_input = input("\nEnter a city name: ")
# TODO: call get_weather() with city_input and API_KEY
#       print the result using the same card format as Step 4


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add an ASCII art icon based on the weather description:
#   "clear sky"  ->  "[o]"   (sun)
#   "rain"       ->  "[~~]"  (rain)
#   "clouds"     ->  "[--]"  (cloud)
# Hint: use  if "rain" in description  to catch partial matches.
