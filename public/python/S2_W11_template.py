# ============================================================
#  SPRINT 2 · WEEK 11 — Conversation Memory
#  A Chatbot That Actually Remembers
#
#  Run:  python S2_W11_template.py
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# ── STEP 1: The problem without memory ───────────────────────
# Without history, each call is brand new — the AI forgets everything.

print("WITHOUT MEMORY (watch it forget):")
r1 = model.generate_content("My name is Sofia.")
print(f"Turn 1: {r1.text.strip()}")
r2 = model.generate_content("What is my name?")
print(f"Turn 2: {r2.text.strip()}")
# The AI has no idea. It will say it doesn't know.


# ── STEP 2: History is a list of dicts ───────────────────────
# The Gemini API accepts a  history  parameter — a list of message dicts.
# Each dict has "role" ("user" or "model") and "parts" (the text).

history = []   # starts empty; grows with every exchange

def chat(user_message, history):
    """
    Sends user_message to the model with full history context.
    Appends both the user message and model reply to history.
    Returns the model's reply text.
    """
    # Append the user's turn
    history.append({"role": "user",  "parts": [user_message]})

    # Send the entire history to the model
    response = model.generate_content(history)
    reply    = response.text.strip()

    # Append the model's reply so it becomes context for next time
    history.append({"role": "model", "parts": [reply]})

    return reply


# ── STEP 3: Test that memory works ───────────────────────────
print("\nWITH MEMORY:")
print(chat("My name is Sofia.", history))
print(chat("What is my name?",   history))   # should now remember!
print(chat("How many messages have we exchanged so far?", history))


# ── STEP 4: Full interactive chatbot ─────────────────────────
print("\n" + "=" * 40)
print("  MEMORY CHATBOT")
print("  Commands:  'quit'  |  'reset'  |  'history'")
print("=" * 40)

history = []   # fresh history for the interactive session

while True:
    user_input = input("\nYou: ").strip()

    if user_input == "":
        continue

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    elif user_input.lower() == "reset":
        history = []
        print("Conversation reset. Starting fresh.")

    elif user_input.lower() == "history":
        print(f"\n--- Conversation so far ({len(history)} messages) ---")
        for msg in history:
            role = "You" if msg["role"] == "user" else "AI"
            # TODO: print each message in format:  [You] message text
            pass
    else:
        reply = chat(user_input, history)
        print(f"AI: {reply}")


# ── STEP 5: Persona + memory combined ────────────────────────
# TODO: create a new model with a system instruction (e.g., a study tutor).
#       Run the same chat loop but with that persona model.
#       The persona should persist across the whole conversation.


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a "summarize" command that sends the current history to the model
# with the prompt: "Summarize our conversation in 3 bullet points."
# Print the summary without adding it to the history.
