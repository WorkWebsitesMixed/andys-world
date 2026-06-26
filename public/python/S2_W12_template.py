# ============================================================
#  SPRINT 2 · WEEK 12 — File I/O
#  Feed the AI Your Own Notes
#
#  This session uses the file  sample_notes.txt  in this folder.
#  Run:  python S2_W12_template.py
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# ── STEP 1: Write to a file ───────────────────────────────────
# open(filename, mode) opens a file.
# "w" = write (creates or overwrites)  |  "a" = append  |  "r" = read

with open("my_note.txt", "w") as f:
    f.write("Python is a high-level programming language.\n")
    f.write("It was created by Guido van Rossum in 1991.\n")
    f.write("Python emphasises readability and simplicity.\n")

print("File written. Check your folder for my_note.txt")


# ── STEP 2: Read from a file ─────────────────────────────────
with open("my_note.txt", "r") as f:
    content = f.read()   # reads the entire file as one string

print("\nFile contents:")
print(content)

# TODO: print the number of lines in the file
# Hint:  content.split("\n")  gives a list of lines


# ── STEP 3: Append to a file ─────────────────────────────────
with open("my_note.txt", "a") as f:
    # TODO: write 2 more facts about Python using f.write()
    pass

print("\nAfter appending:")
with open("my_note.txt", "r") as f:
    print(f.read())


# ── STEP 4: pathlib — a cleaner way to work with files ───────
# Path objects know about file system operations.

notes_path = Path("sample_notes.txt")

if notes_path.exists():
    notes = notes_path.read_text(encoding="utf-8")
    print(f"\nLoaded {len(notes)} characters from {notes_path.name}")
else:
    print("sample_notes.txt not found. Using my_note.txt instead.")
    notes = Path("my_note.txt").read_text(encoding="utf-8")

# TODO: print how many words are in notes
# Hint: len(notes.split())


# ── STEP 5: Feed the notes to the AI ────────────────────────
study_model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=(
        "You are a study assistant. The user will give you study notes "
        "and ask questions about them. Answer ONLY based on the notes provided. "
        "If the answer is not in the notes, say 'That is not in your notes.'"
    )
)

history = []

def chat_with_notes(user_message, notes, history):
    """Sends a message with notes as context."""
    # First turn: include the notes as context
    if len(history) == 0:
        full_message = f"Here are my study notes:\n\n{notes}\n\nNow answer my questions."
        history.append({"role": "user",  "parts": [full_message]})
        response = study_model.generate_content(history)
        history.append({"role": "model", "parts": [response.text]})

    # Subsequent turns: just the question
    history.append({"role": "user",  "parts": [user_message]})
    response = study_model.generate_content(history)
    reply    = response.text.strip()
    history.append({"role": "model", "parts": [reply]})
    return reply

print("\n" + "=" * 40)
print("  STUDY ASSISTANT")
print("  Loaded notes from:", notes_path.name if notes_path.exists() else "my_note.txt")
print("  Type 'quit' to exit")
print("=" * 40)

while True:
    question = input("\nYour question: ").strip()
    if question.lower() == "quit":
        break
    if question:
        print("AI:", chat_with_notes(question, notes, history))


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a "save" command that writes the Q&A transcript to a file
# called  study_session.txt  with timestamps.
# Use  from datetime import datetime  and  datetime.now().strftime(...)
