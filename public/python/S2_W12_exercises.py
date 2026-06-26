# ============================================================
#  SPRINT 2 · WEEK 12 — Exercise Set
#  Topic: open(), read(), write(), append(), pathlib, file + AI
# ============================================================

from pathlib import Path


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — WRITE AND READ
#  Write a file called  my_bio.txt  with 5 lines about yourself.
#  Then read it back and print each line with its line number.
#  Format:  Line 1: I am a student at Marymount...
# ════════════════════════════════════════════════════════════

# TODO: write my_bio.txt
# TODO: read it back and print with line numbers


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — LINE COUNT AND WORD COUNT
#  Read sample_notes.txt and print:
#    - Total number of lines
#    - Total number of words
#    - Total number of characters
#    - The longest line (by character count)
# ════════════════════════════════════════════════════════════

notes = Path("sample_notes.txt").read_text(encoding="utf-8")

lines = notes.split("\n")
words = notes.split()

# TODO: print total lines, words, characters
# TODO: find and print the longest line


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — PERSONAL JOURNAL
#  Every time the script runs it should:
#    1. Ask for today's entry (user types until empty line)
#    2. Append the entry to journal.txt with today's date as header
#    3. Print how many total entries are in the journal
#
#  Hint: from datetime import date; date.today() gives today's date
# ════════════════════════════════════════════════════════════

from datetime import date

journal_path = Path("journal.txt")

print("Today's journal entry (press Enter twice to finish):")
lines_input = []
while True:
    line = input()
    if line == "":
        break
    lines_input.append(line)

entry_text = "\n".join(lines_input)
today      = date.today()

# TODO: append the entry to journal.txt with date header
# TODO: count entries by counting "---" separators


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — FILE SEARCH
#  Read sample_notes.txt.
#  Ask the user for a keyword.
#  Print every line that contains that keyword (case-insensitive).
#  Print the total count of matching lines.
# ════════════════════════════════════════════════════════════

keyword = input("Search keyword: ").strip().lower()
notes   = Path("sample_notes.txt").read_text(encoding="utf-8")

# TODO: filter and print matching lines with line numbers


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: AI NOTES QUIZ
#  Read sample_notes.txt.
#  Send the notes to the AI with this instruction:
#    "Generate 5 multiple-choice quiz questions based on these notes.
#     Format each as: Q: question  A) B) C) D)  Answer: X"
#  Then parse the response and run the quiz interactively.
#  Score the user at the end.
# ════════════════════════════════════════════════════════════

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# TODO: generate the quiz from sample_notes.txt
# TODO: run the interactive quiz and show score
