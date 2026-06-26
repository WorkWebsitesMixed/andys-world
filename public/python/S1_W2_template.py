# ============================================================
#  SPRINT 1 · WEEK 2 — Hello Python
#  Student ID Card Generator
#
#  Fill in every line marked  TODO  to make the program work.
#  Run after each step:   python S1_W2_template.py
# ============================================================


# ── STEP 1: Basic print ──────────────────────────────────────
# Run this first. Then try changing 30 to a different number.

print("MARYMOUNT STEM ACADEMY")
print("=" * 30)           # TODO: experiment — what does * do to a string?
print("Loading your profile...")


# ── STEP 2: Variables ────────────────────────────────────────
# A variable is a label on a storage box. Change the value; re-run.

school  = "Marymount"
city    = TODO            # TODO: assign your city as a string  e.g. "Medellin"
program = TODO            # TODO: assign "STEM Programming"

print(school)
print(city)
print(program)


# ── STEP 3: User input ───────────────────────────────────────
# input() pauses the program and waits for the user to type.
# Whatever they type is stored as a string.

name    = input("Enter your name: ")
subject = TODO            # TODO: ask the user for their favourite subject


# ── STEP 4: f-strings ────────────────────────────────────────
# Rule: put f before the quotes. Wrap variables in curly braces {}.

print()
print("=" * 38)
print(f"  MARYMOUNT STEM ACADEMY")
print(f"  Student : {name}")
print(f"  Subject : {TODO}")   # TODO: put the subject variable inside {}
print(f"  Status  : Future Engineer")
print("=" * 38)


# ── STEP 5: String methods ───────────────────────────────────
# Methods transform a string and return a new version of it.
# The original variable is untouched.

print()
print("=" * 38)
print(f"  MARYMOUNT STEM ACADEMY")
print(f"  Student : {name.title()}")           # .title() → Title Case
print(f"  Subject : {TODO.upper()}")           # TODO: apply .upper() to subject
print(f"  Name has: {TODO} letters")           # TODO: use len() to count letters
print("=" * 38)


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a third input() for a lucky number.
# Include it in the card output using an f-string.
# Then: can you make the "=" line exactly as wide as the name + padding?
