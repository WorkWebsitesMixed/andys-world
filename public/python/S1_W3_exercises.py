# ============================================================
#  SPRINT 1 · WEEK 3 — Exercise Set
#  Topic: if / elif / else, Conditionals, random
# ============================================================


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SPOT THE BUG  (3 errors)
# ════════════════════════════════════════════════════════════

# score = 85
# if score >= 90
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("c")   # should be uppercase
# else
#     print("Below C")


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — GRADE CALCULATOR
#  Ask the user for a score (0-100).
#  Print the letter grade:  A (>=90), B (>=80), C (>=70),
#                           D (>=60), F (below 60)
#  Also print "Pass" or "Fail" depending on whether they scored >= 60.
# ════════════════════════════════════════════════════════════

score = int(input("Enter your score (0-100): "))

# TODO: write the if/elif/else chain for the letter grade
# TODO: write the Pass/Fail check below it


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — SEASON FINDER
#  Ask for a month number (1-12).
#  Print the season:
#    Dec-Feb = Summer  (Southern Hemisphere!)
#    Mar-May = Autumn
#    Jun-Aug = Winter
#    Sep-Nov = Spring
#  Use  or  to combine conditions on a single line.
#  Example:  if month == 12 or month == 1 or month == 2:
# ════════════════════════════════════════════════════════════

month = int(input("Enter a month number (1-12): "))

# TODO: write the season finder


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — COIN FLIP GAME
#  Use random to simulate a coin flip.
#  Ask the user to guess "heads" or "tails".
#  Generate the result with  random.choice(["heads", "tails"])
#  Print "Correct!" or "Wrong — it was {result}." as appropriate.
#  Count how many times they win across 3 flips using a variable.
# ════════════════════════════════════════════════════════════

import random

wins = 0

# TODO: write 3 rounds of the coin flip game using copy-paste or a loop


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE
#  Build a text-based "choose your own adventure" opening.
#  The player starts in a room and must choose a direction.
#  At least 3 rooms, 2 choices per room, 1 dead end, 1 win condition.
#  Only use print, input, and if/elif/else — no loops yet.
# ════════════════════════════════════════════════════════════

print("You wake up in a dark room.")
print("There is a door to the NORTH and a window to the EAST.")
choice = input("Which way do you go? (north/east): ")

# TODO: build out at least 3 decision points
