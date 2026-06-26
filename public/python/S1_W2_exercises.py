# ============================================================
#  SPRINT 1 · WEEK 2 — Exercise Set
#  Topic: Variables, Strings, f-strings, input()
#
#  Work through these in order. Each one builds on the last.
#  Run each exercise separately (comment out the others).
# ============================================================


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SPOT THE BUG
#  The three lines below each have one mistake.
#  Uncomment them, fix the errors, and make the script run.
#
#  Clue: one is a missing quote, one is wrong syntax,
#        one is a case issue.
# ════════════════════════════════════════════════════════════

# name = input(Enter your name: )   # Bug 1 — what is missing?
# city = "Medellin                  # Bug 2 — look carefully
# print(f"Hello {Name}!")           # Bug 3 — Python is case-sensitive


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — FILL IN THE BLANKS
#  Complete the code so it prints a two-line greeting.
#  Replace every ________ with working Python.
# ════════════════════════════════════════════════════════════

first_name = input("First name: ")
last_name  = input("Last name: ")

# Print "Hello, FirstName LastName!" using an f-string
print(f"Hello, ________ ________!")

# Print "Your full name has X letters." — count ALL letters, no spaces
full_name   = first_name + last_name    # concatenation joins two strings
print(f"Your full name has ________ letters.")


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — BUILD FROM SCRATCH
#  Write a program that:
#    1. Asks for the user's favourite colour
#    2. Asks for their lucky number
#    3. Prints a sentence combining both using an f-string
#
#  Example output:
#    Your power combo: BLUE and the number 7.
#
#  Requirement: the colour must be printed in ALL CAPS.
# ════════════════════════════════════════════════════════════

# Write your code here:


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — CHALLENGE: INITIALS
#  Ask for first and last name separately.
#  Print the initials in the format  A.F.
#
#  Hint: strings can be indexed like a list.
#        "Sofia"[0]  gives you  "S"
# ════════════════════════════════════════════════════════════

# Write your code here:


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE (Advanced student)
#  Ask for a full sentence.
#  Print it three ways:
#    (a) In UPPERCASE
#    (b) With all spaces replaced by underscores
#    (c) Reversed — last character first
#
#  Hints:
#    .upper()            →  converts to uppercase
#    .replace(" ", "_")  →  swaps spaces for underscores
#    text[::-1]          →  reverses the string (we haven't seen this yet — figure it out!)
# ════════════════════════════════════════════════════════════

# Write your code here:
