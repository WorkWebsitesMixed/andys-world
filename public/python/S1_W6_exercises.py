# ============================================================
#  SPRINT 1 · WEEK 6 — Exercise Set
#  Topic: list, dict, .append(), .remove(), for loops over data
# ============================================================


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SPOT THE BUG  (3 errors)
# ════════════════════════════════════════════════════════════

# colors = ["red", "green", "blue"]
# print(colors[3])         # Bug 1: index out of range — what is the last index?
#
# person = {"name": "Ana", age: 17}   # Bug 2: key is not a string
# print(person["name"])
#
# numbers = [5, 3, 8, 1]
# numbers.append(2, 7)    # Bug 3: append only takes one argument


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — LIST OPERATIONS
#  Start with the list below. Perform each operation in order
#  and print the list after each one to verify.
# ════════════════════════════════════════════════════════════

fruits = ["apple", "banana", "cherry"]

# TODO: append "mango"
# TODO: insert "grape" at index 1 — hint: fruits.insert(1, "grape")
# TODO: remove "banana"
# TODO: print the list sorted alphabetically (use sorted())
# TODO: print the total number of items


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — CONTACT BOOK
#  Create a dictionary called  contact  with these keys:
#    name, phone, email, city
#  Print each field on its own line with a label.
#  Then update the city to "Bogota" and print the full dict.
#  Finally, add a new key  "instagram"  with a made-up handle.
# ════════════════════════════════════════════════════════════

contact = {
    "name":  TODO,   # TODO: fill in your values
    "phone": TODO,
    "email": TODO,
    "city":  TODO,
}

# TODO: print each key/value with a for loop
# TODO: update city and add instagram


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — HIGHEST SCORER
#  Given the list of player score dicts below,
#  find and print the player with the highest score.
#  Do NOT use max() — use a for loop and an if statement.
# ════════════════════════════════════════════════════════════

scores = [
    {"name": "Ana",       "score": 4500},
    {"name": "Sofia",     "score": 7200},
    {"name": "Maria",     "score": 6100},
    {"name": "Laura",     "score": 9300},
    {"name": "Valentina", "score": 8800},
]

best_player = None
best_score  = 0

for player in scores:
    # TODO: compare player["score"] with best_score
    #       update best_player and best_score when you find a higher one
    pass

print(f"Winner: {best_player['name']} with {best_score} points")


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: WORD FREQUENCY
#  Count how many times each word appears in the sentence below.
#  Store the result in a dictionary: {"word": count, ...}
#  Print each word and its count, sorted by most frequent first.
#
#  Hint 1: sentence.split()  converts a string to a list of words
#  Hint 2: dict.get(key, 0)  returns 0 if the key doesn't exist yet
#  Hint 3: sorted(dict.items(), key=lambda x: x[1], reverse=True)
# ════════════════════════════════════════════════════════════

sentence = "the cat sat on the mat the cat sat on the hat the cat"

word_count = {}

# TODO: split the sentence and count each word
# TODO: print results sorted by frequency
