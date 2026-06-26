# ============================================================
#  SPRINT 3 · WEEK 18 — Exercise Set
#  Topic: OMDb API, JSON files, data persistence, list manipulation
# ============================================================

import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
OMDB_KEY = os.environ.get("OMDB_KEY", "YOUR_KEY")
BASE_URL = "http://www.omdbapi.com/"


def get_movie(title, api_key=OMDB_KEY):
    params   = {"t": title, "apikey": api_key}
    response = requests.get(BASE_URL, params=params)
    data     = response.json()
    return data if data.get("Response") != "False" else None


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — FIELD EXTRACTOR
#  Fetch the movie "The Dark Knight".
#  Extract and print these fields in a clean format:
#    Title, Year, Rated, Genre, Director, Awards, BoxOffice
#  Some fields may not exist — use  data.get("BoxOffice", "N/A")
# ════════════════════════════════════════════════════════════

# TODO: fetch and print the fields


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — TOP RATED FROM A LIST
#  Fetch ratings for this list of movies.
#  Find and print the highest rated one.
# ════════════════════════════════════════════════════════════

movie_titles = ["Parasite", "Coco", "The Shawshank Redemption", "Spirited Away", "Whiplash"]

# TODO: fetch each movie, compare imdbRating (convert to float), print winner


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — JSON PERSISTENCE
#  Fetch 3 movies of your choice.
#  Save them as a JSON file  my_movies.json  (pretty-printed, indent=2).
#  Load the file back and print the titles to confirm.
# ════════════════════════════════════════════════════════════

# TODO: build a list of 3 movie dicts
# TODO: save with json.dump() using indent=2
# TODO: reload with json.load() and print titles


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — GENRE FILTER
#  Fetch these 5 movies and group them by first genre.
#  Print each genre group.
#  Hint: movie["Genre"].split(",")[0].strip() gives the first genre.
# ════════════════════════════════════════════════════════════

titles = ["Inception", "The Lion King", "Avengers Endgame", "La La Land", "Dune"]

genre_groups = {}
for title in titles:
    movie = get_movie(title)
    if movie:
        genre = movie.get("Genre", "Unknown").split(",")[0].strip()
        # TODO: add to genre_groups dict (genre -> list of titles)
        pass

for genre, movie_list in genre_groups.items():
    print(f"{genre}: {', '.join(movie_list)}")


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: "WHAT TO WATCH" RECOMMENDER
#  Ask the user for:
#    1. A mood ("happy", "tense", "thoughtful", "action")
#    2. A preferred decade ("80s", "90s", "2000s", "2010s", "2020s")
#
#  Build a dict mapping mood -> list of titles to try.
#  Fetch the movies that match the mood.
#  Filter by year (e.g. 80s = Year starts with "198").
#  Print the best match (highest imdbRating among filtered results).
#
#  Bonus: save the recommendation and the user's mood to a log file.
# ════════════════════════════════════════════════════════════

MOOD_MAP = {
    "happy":     ["The Secret Life of Walter Mitty", "Chef", "Julie and Julia", "About Time"],
    "tense":     ["No Country for Old Men", "Gone Girl", "Prisoners", "Parasite"],
    "thoughtful":["Arrival", "Her", "Eternal Sunshine", "The Truman Show"],
    "action":    ["Mad Max Fury Road", "John Wick", "Mission Impossible", "Edge of Tomorrow"],
}

# TODO: implement the recommender
