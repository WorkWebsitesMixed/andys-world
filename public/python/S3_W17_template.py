# ============================================================
#  SPRINT 3 · WEEK 17 — Web APIs (Advanced)
#  Personal Morning Digest
#
#  APIs used (both free):
#    Weather: openweathermap.org  (your existing key)
#    News:    newsapi.org         (free developer key)
#
#  Run:  python S3_W17_template.py
# ============================================================

import requests
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

WEATHER_KEY = os.environ.get("OPENWEATHER_KEY", "YOUR_WEATHER_KEY")
NEWS_KEY    = os.environ.get("NEWSAPI_KEY",     "YOUR_NEWS_KEY")
CITY        = "Medellin"


# ── STEP 1: Weather function (review from W8) ────────────────
def get_weather(city, api_key):
    """Returns a weather summary dict for the given city."""
    url      = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data     = response.json()

    if data.get("cod") != 200:
        return None

    return {
        "city":        city,
        "temp":        data["main"]["temp"],
        "feels_like":  data["main"]["feels_like"],
        "description": data["weather"][0]["description"].title(),
        "humidity":    data["main"]["humidity"],
    }


# ── STEP 2: News function ─────────────────────────────────────
def get_headlines(api_key, country="co", count=3):
    """Returns a list of top headline strings from NewsAPI."""
    url    = (f"https://newsapi.org/v2/top-headlines"
              f"?country={country}&apiKey={api_key}&pageSize={count}")
    # TODO: make the GET request with requests.get(url)
    # TODO: check response.status_code == 200
    # TODO: return a list of article["title"] strings from data["articles"]
    return []


# ── STEP 3: Weather icon ─────────────────────────────────────
def weather_icon(description):
    """Returns an ASCII icon based on the weather description."""
    desc = description.lower()
    if "clear"  in desc: return "[SUN]"
    if "cloud"  in desc: return "[CLD]"
    if "rain"   in desc: return "[RAN]"
    if "thunder"in desc: return "[STM]"
    if "snow"   in desc: return "[SNW]"
    # TODO: add "fog" and "mist" icons
    return "[   ]"


# ── STEP 4: Assemble the digest ──────────────────────────────
def print_digest(city, weather_key, news_key):
    """Prints the complete morning digest."""
    today   = date.today().strftime("%A %d %B %Y")   # e.g. "Monday 10 August 2026"
    weather = get_weather(city, weather_key)
    headlines = get_headlines(news_key)

    print()
    print("=" * 48)
    print(f"  MORNING DIGEST — {today}")
    print("=" * 48)

    if weather:
        icon = weather_icon(weather["description"])
        print(f"  {icon} {weather['city'].upper()}: {weather['temp']}C — {weather['description']}")
        print(f"  Feels like {weather['feels_like']}C | Humidity {weather['humidity']}%")
    else:
        print("  Weather data unavailable.")

    print()
    print("  TODAY'S HEADLINES:")
    if headlines:
        for i, headline in enumerate(headlines, 1):
            # TODO: print each headline with its number, wrapped at ~70 chars
            print(f"  {i}. {headline[:70]}...")
    else:
        print("  News data unavailable.")

    print("=" * 48)
    print()


print_digest(CITY, WEATHER_KEY, NEWS_KEY)


# ── STEP 5: Run on a schedule (preview) ──────────────────────
# TODO: wrap print_digest in a loop that asks the user if they want to
#       refresh. Press Enter to refresh, type "quit" to exit.


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a "motivational quote of the day" from a public quotes API:
#   https://api.quotable.io/random
# No key required. Parse  data["content"]  and  data["author"].
