# ============================================================
#  SPRINT 3 · WEEK 18 — Fun APIs
#  Movie Explorer with OMDb
#
#  Get a FREE key at:  omdbapi.com  (click "API Key" tab)
#  Add to your .env:   OMDB_KEY=your_key_here
#
#  Run:  python S3_W18_template.py
# ============================================================

import requests
import os
from dotenv import load_dotenv

load_dotenv()
OMDB_KEY = os.environ.get("OMDB_KEY", "YOUR_KEY")
BASE_URL = "http://www.omdbapi.com/"


# ── STEP 1: Fetch one movie ───────────────────────────────────
def get_movie(title, api_key):
    """Fetches movie details by title. Returns a dict or None."""
    params   = {"t": title, "apikey": api_key}
    response = requests.get(BASE_URL, params=params)
    data     = response.json()

    if data.get("Response") == "False":
        print(f"Movie not found: {title}")
        return None
    return data

movie = get_movie("Inception", OMDB_KEY)
if movie:
    print(f"Title:  {movie['Title']}")
    print(f"Year:   {movie['Year']}")
    print(f"Rating: {movie['imdbRating']}/10")
    print(f"Plot:   {movie['Plot']}")


# ── STEP 2: Search for movies ────────────────────────────────
def search_movies(query, api_key, movie_type="movie"):
    """Searches for movies matching a query string.
    movie_type can be 'movie', 'series', or 'episode'."""
    params   = {"s": query, "type": movie_type, "apikey": api_key}
    response = requests.get(BASE_URL, params=params)
    data     = response.json()

    if data.get("Response") == "False":
        return []
    return data.get("Search", [])

print("\nSearch results for 'space':")
results = search_movies("space", OMDB_KEY)
for r in results[:5]:
    # TODO: print each result's Title and Year
    pass


# ── STEP 3: Movie card printer ───────────────────────────────
def print_movie_card(movie):
    """Prints a formatted movie card."""
    if not movie:
        return

    # TODO: print a formatted card with:
    #   Title, Year, Genre, Director, Cast (first 2 actors from Actors field),
    #   Rating, Runtime, Plot (first 100 chars)
    #   Use str.split(",") to get a list from the Actors field.
    pass

print_movie_card(movie)


# ── STEP 4: Favourites list ──────────────────────────────────
favourites = []

def add_to_favourites(title, api_key):
    """Looks up a movie and adds it to the favourites list."""
    movie_data = get_movie(title, api_key)
    if movie_data:
        favourites.append({
            "title":  movie_data["Title"],
            "year":   movie_data["Year"],
            "rating": movie_data["imdbRating"],
        })
        print(f"Added: {movie_data['Title']}")

add_to_favourites("The Matrix", OMDB_KEY)
add_to_favourites("Interstellar", OMDB_KEY)
# TODO: add 2 more of your favourite movies

# TODO: print all favourites sorted by rating (highest first)
# Hint: sorted(favourites, key=lambda x: float(x["rating"]), reverse=True)


# ── STEP 5: Interactive explorer ─────────────────────────────
print("\n" + "=" * 40)
print("  MOVIE EXPLORER")
print("  Commands: search [query] | movie [title] | favourites | quit")
print("=" * 40)

while True:
    command = input("\n> ").strip().lower()

    if command == "quit":
        break

    elif command.startswith("search "):
        query   = command[7:]
        results = search_movies(query, OMDB_KEY)
        # TODO: print results

    elif command.startswith("movie "):
        title = command[6:]
        # TODO: get and print_movie_card

    elif command == "favourites":
        # TODO: print the favourites list
        pass

    else:
        print("Unknown command.")


# ── BONUS (Advanced) ─────────────────────────────────────────
# Save and load favourites from a JSON file.
# Hint:  import json
#        json.dump(favourites, f, indent=2)
#        json.load(f)
