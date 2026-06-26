# ============================================================
#  SPRINT 1 · WEEK 2 — Free Time Challenge
#  The Fortune Teller
#
#  Build a program that predicts a student's future.
#  Fill in the TODOs. Then go further with the extensions.
# ============================================================

import random

# ── YOUR PREDICTIONS ─────────────────────────────────────────
# This is a list — we will learn lists properly in Week 6.
# For now: it holds multiple strings, separated by commas.
# Everything between [ ] is the list.

predictions = [
    "will build something a million people use",
    "will solve a problem everyone said was impossible",
    "will teach someone else to code by next year",
    "will get a scholarship for STEM",
    "will speak at a tech conference before graduating",
    # TODO: add at least 3 predictions of your own below this line

]


# ── ASK FOR A NAME ───────────────────────────────────────────

name = TODO    # TODO: use input() to ask "Your name: "


# ── PICK A RANDOM PREDICTION ─────────────────────────────────
# random.choice(list) picks one item at random from the list.

prediction = random.choice(predictions)


# ── PRINT THE RESULT ─────────────────────────────────────────

print()
print(f"Consulting the oracle for {TODO.title()}...")   # TODO: put name here
print()
print(f">>> {name.title()} {prediction}. <<<")


# ════════════════════════════════════════════════════════════
#  EXTENSION 1
#  Add a second input() that asks for the user's city.
#  Include the city in the output sentence.
#  Example: ">>> Sofia, from Medellin, will build something... <<<"
# ════════════════════════════════════════════════════════════

# Write your Extension 1 code here:


# ════════════════════════════════════════════════════════════
#  EXTENSION 2  (Advanced)
#  Make one "legendary" prediction appear only ~10% of the time.
#
#  Hint: random.random() returns a random float between 0.0 and 1.0.
#        If that float is less than 0.1, there is a ~10% chance.
#
#  Structure:
#    if random.random() < 0.1:
#        print(">>> LEGENDARY: ... <<<")
#    else:
#        prediction = random.choice(predictions)
#        print(f">>> {name.title()} {prediction}. <<<")
# ════════════════════════════════════════════════════════════

# Write your Extension 2 code here:


# ════════════════════════════════════════════════════════════
#  ULTRA EXTENSION  (Advanced — three tiers)
#  Build a system with three probability tiers:
#    Common    (70%) — normal predictions from the list
#    Rare      (20%) — a separate "rare" list of predictions
#    Legendary (10%) — one single incredible prediction
#
#  You will need:
#    - Two lists (common and rare)
#    - random.random() to decide which tier
#    - if / elif / else  (you already know these from your holiday course)
# ════════════════════════════════════════════════════════════

# Write your Ultra Extension code here:
