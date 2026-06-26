# ============================================================
#  SPRINT 3 · WEEK 17 — Exercise Set
#  Topic: multiple APIs, params, JSON depth, data combination
# ============================================================

import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_KEY = os.environ.get("OPENWEATHER_KEY", "YOUR_KEY")


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — DEEP JSON DRILL
#  The dict below simulates a NewsAPI response.
#  Answer each question with a print statement.
# ════════════════════════════════════════════════════════════

news_response = {
    "status": "ok",
    "totalResults": 3,
    "articles": [
        {"title": "Colombia wins at Tech Olympics", "source": {"name": "BBC"},  "publishedAt": "2026-08-10T08:00:00Z"},
        {"title": "New Python version released",    "source": {"name": "CNN"},  "publishedAt": "2026-08-10T09:30:00Z"},
        {"title": "AI beats world chess champion",  "source": {"name": "Reuters"}, "publishedAt": "2026-08-10T11:00:00Z"},
    ]
}

# TODO: print the total number of results
# TODO: print all article titles using a for loop
# TODO: print the source name of the second article
# TODO: print all titles that contain the word "AI"


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — QUOTABLE API (no key needed)
#  Fetch a random quote from:  https://api.quotable.io/random
#  Print:  "Quote" — Author  (Category)
#  Try fetching 5 quotes in a loop.
# ════════════════════════════════════════════════════════════

for i in range(5):
    # TODO: GET https://api.quotable.io/random
    # TODO: parse and print content + author
    pass


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — WEATHER FOR MULTIPLE CITIES
#  Fetch weather for 4 Colombian cities.
#  Print a comparison table:
#    City       | Temp  | Description
#    Medellin   | 22.4C | few clouds
#    Bogota     | 14.1C | overcast clouds
#    Cartagena  | 31.2C | clear sky
#    Cali       | 26.8C | scattered clouds
# ════════════════════════════════════════════════════════════

cities = ["Medellin", "Bogota", "Cartagena", "Cali"]

# TODO: fetch weather for each city and print the table


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — SMART DIGEST FUNCTION
#  Write  build_digest(city, weather_key, news_key)  that
#  returns a single formatted string (not just prints).
#  This makes it reusable — you can print it, save it to a file,
#  or send it somewhere else.
# ════════════════════════════════════════════════════════════

def build_digest(city, weather_key, news_key=None):
    """Returns a formatted digest string for the given city."""
    # TODO: implement this function
    return ""

digest = build_digest("Medellin", WEATHER_KEY)
print(digest)

# Save it to a file
with open("digest.txt", "w") as f:
    f.write(digest)
print("Digest saved to digest.txt")


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: RATE LIMITER
#  The free tiers of these APIs have rate limits (calls per minute).
#  Add a  rate_limiter(calls_per_minute)  decorator that:
#    - Tracks the time of each call
#    - If more than calls_per_minute calls happened in the last 60 seconds,
#      waits before making the next call
#  Hint: use time.time() to get the current timestamp.
#        collections.deque(maxlen=n) keeps only the last n timestamps.
# ════════════════════════════════════════════════════════════

import time
from collections import deque

def rate_limiter(calls_per_minute):
    """Decorator that limits function calls per minute."""
    timestamps = deque(maxlen=calls_per_minute)

    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            if len(timestamps) == calls_per_minute:
                oldest = timestamps[0]
                elapsed = now - oldest
                if elapsed < 60:
                    wait_time = 60 - elapsed
                    print(f"Rate limit: waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
            timestamps.append(time.time())
            return func(*args, **kwargs)
        return wrapper
    return decorator

# TODO: apply @rate_limiter(5) to a weather-fetching function and test it
