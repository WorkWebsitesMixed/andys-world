# ============================================================
#  SPRINT 2 · WEEK 13 — AI CAPSTONE BUILD
#  Personal AI Study Assistant
#
#  BUILD GUIDE — Session is 60 minutes of project work.
#
#  What you are building:
#    A command-line study assistant that reads your own notes
#    and answers questions about them using the Gemini API.
#    It remembers the conversation so you can ask follow-up
#    questions, and it ONLY answers from your notes.
#
#  Minimum requirements (aim to finish all by end of session):
#    [ ] load_notes(filename): reads a .txt file, returns a string
#    [ ] setup_model(): creates and returns a Gemini model
#          with a system instruction that restricts it to the notes
#    [ ] chat(question, notes, history): sends a message with
#          note context on the first turn, plain question after
#    [ ] main(): loads notes, runs the Q&A loop
#          - "quit"   -> exits
#          - "reset"  -> clears history
#          - "load"   -> asks for a new notes file
#
#  Bonus features (tackle these if you finish early):
#    [ ] Let the user pick any .txt file at startup
#    [ ] Add a "summarize" command
#    [ ] Save the Q&A session to a transcript file
#    [ ] Show a spinner or "Thinking..." while waiting for the API
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


# ── Module 1: Notes Loader ───────────────────────────────────

def load_notes(filename):
    """Reads a text file and returns its content as a string.
    Returns None if the file does not exist."""
    path = Path(filename)
    if not path.exists():
        print(f"File not found: {filename}")
        return None
    content = path.read_text(encoding="utf-8")
    print(f"Loaded {len(content)} characters from {filename}")
    return content


# ── Module 2: AI Model Setup ─────────────────────────────────

def setup_model():
    """Creates and returns a Gemini model configured as a study assistant."""
    return genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction=(
            "You are a focused study assistant. "
            "The user will share study notes with you on the first message. "
            "After that, answer their questions using ONLY information from those notes. "
            "If the answer is not in the notes, say exactly: "
            "'That information is not in your notes.' "
            "Keep answers concise and clear."
        )
    )


# ── Module 3: Chat Function ──────────────────────────────────

def chat(question, notes, history, model):
    """Sends a question to the model.
    On the first call, includes the notes as context.
    Returns the model's reply."""
    if len(history) == 0:
        # First turn: inject notes
        first_message = f"Here are my study notes:\n\n{notes}\n\nI will now ask you questions."
        history.append({"role": "user",  "parts": [first_message]})
        init_response = model.generate_content(history)
        history.append({"role": "model", "parts": [init_response.text]})

    history.append({"role": "user",  "parts": [question]})
    response = model.generate_content(history)
    reply    = response.text.strip()
    history.append({"role": "model", "parts": [reply]})
    return reply


# ── Module 4: Main Program ───────────────────────────────────

def main():
    print("=" * 45)
    print("  PERSONAL AI STUDY ASSISTANT")
    print("  Commands: quit | reset | load")
    print("=" * 45)

    # Default notes file
    notes_file = "sample_notes.txt"
    notes      = load_notes(notes_file)

    if not notes:
        notes_file = input("Enter path to your notes file: ").strip()
        notes      = load_notes(notes_file)
        if not notes:
            print("No notes loaded. Exiting.")
            return

    model   = setup_model()
    history = []

    print(f"\nNotes loaded: {notes_file}")
    print("Ask me anything about your notes.\n")

    while True:
        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() == "quit":
            print("Good studying! Goodbye.")
            break

        elif question.lower() == "reset":
            history = []
            print("Conversation reset.")

        elif question.lower() == "load":
            new_file = input("Enter path to notes file: ").strip()
            new_notes = load_notes(new_file)
            if new_notes:
                notes    = new_notes
                history  = []
                notes_file = new_file
                print(f"Switched to {new_file}. History cleared.")
        else:
            try:
                reply = chat(question, notes, history, model)
                print(f"\nAssistant: {reply}\n")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
