# ============================================================
#  SPRINT 1 · WEEK 3 — Making Decisions
#  Magic 8-Ball
#
#  Fill in every TODO. Run after each step.
#  Run:  python S1_W3_template.py
# ============================================================

import random

# ── The answer banks ─────────────────────────────────────────
# These are lists. We will learn them fully in Week 6.
POSITIVE = ["It is certain.", "Without a doubt.", "Yes, definitely.", "Signs point to yes."]
NEGATIVE = ["Don't count on it.", "My sources say no.", "Very doubtful.", "Outlook not so good."]
NEUTRAL  = ["Reply hazy, try again.", "Cannot predict now.", "Ask again later."]

print("MAGIC 8-BALL")
print("=" * 30)

# ── STEP 1: Get a question ───────────────────────────────────
question = input("Ask your question: ")

# ── STEP 2: Guard against an empty question ──────────────────
# TODO: write an if statement that checks if question == ""
#       If it is empty, print "Ask a real question!" and stop here.
#       Hint: you can use  quit()  to stop the program.



# ── STEP 3: Pick a random number to decide the category ──────
number = random.randint(1, 3)   # gives 1, 2, or 3 at random

# TODO: write an if / elif / else chain:
#   if number == 1  -->  answer = random.choice(POSITIVE)
#   elif number == 2  -->  answer = random.choice(NEGATIVE)
#   else  -->  answer = random.choice(NEUTRAL)



# ── STEP 4: Print the answer ─────────────────────────────────
# TODO: print the answer using an f-string
#       Format: "  >> Your question: {question}"
#               "  >> The 8-Ball says: {answer}"



# ── STEP 5: Ask again? ───────────────────────────────────────
# TODO: ask the user "Ask another question? (yes/no): "
#       Store the reply in a variable called  again
#       If again == "yes", print "Shake the ball again..."
#       Otherwise print "The ball has spoken. Goodbye."



# ── BONUS (Advanced) ─────────────────────────────────────────
# Wrap the whole thing in a while loop so the program keeps running
# until the user types "no". You know while loops from the exercise set!
