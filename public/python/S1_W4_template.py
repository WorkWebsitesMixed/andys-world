# ============================================================
#  SPRINT 1 · WEEK 4 — Loops
#  Number Guessing Game
#
#  Fill in every TODO. Run after each step.
#  Run:  python S1_W4_template.py
# ============================================================

import random

print("NUMBER GUESSING GAME")
print("=" * 30)

# ── STEP 1: for loop warm-up ─────────────────────────────────
# Run this block, watch it count, then delete it before Step 2.
print("Warming up your brain:")
for i in range(1, 6):
    print(f"  Step {i}")  # TODO: change range to count from 1 to 10


# ── STEP 2: Generate the secret number ───────────────────────
secret = random.randint(1, 10)   # a random integer between 1 and 10
attempts = 0
MAX_ATTEMPTS = 4

print(f"\nI'm thinking of a number between 1 and 10.")
print(f"You have {MAX_ATTEMPTS} attempts.\n")


# ── STEP 3: The game loop ────────────────────────────────────
# A while loop keeps running until its condition becomes False.
# while True runs forever — we use break to escape.

while True:
    attempts += 1   # += 1 means "add 1 to the current value"

    # TODO: use input() to ask "Attempt {attempts}/{MAX_ATTEMPTS} - Your guess: "
    #       Convert the answer to an integer with int()
    guess = TODO

    # TODO: write three branches:
    #   if guess == secret   -> print "Correct! You got it in {attempts} attempts."
    #                           then break to exit the loop
    #   elif guess < secret  -> print "Too low! Try higher."
    #   else                 -> print "Too high! Try lower."



    # TODO: add a check: if attempts >= MAX_ATTEMPTS, print "No more attempts!
    #       The number was {secret}." then break



# ── STEP 4: Add a difficulty selector ────────────────────────
# Before the game loop, ask the user: "Difficulty? (easy/hard): "
# easy -> range is 1-10, MAX_ATTEMPTS = 5
# hard -> range is 1-50, MAX_ATTEMPTS = 4
# TODO: implement this before the while loop


# ── BONUS (Advanced) ─────────────────────────────────────────
# Track the player's best score (fewest attempts) across multiple games.
# Use a while loop to ask "Play again? (yes/no)" after each game.
# Print the best score at the end.
