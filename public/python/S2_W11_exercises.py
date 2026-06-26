# ============================================================
#  SPRINT 2 · WEEK 11 — Exercise Set
#  Topic: conversation history, list of dicts, chat loops
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def chat(user_message, history):
    history.append({"role": "user",  "parts": [user_message]})
    response = model.generate_content(history)
    reply    = response.text.strip()
    history.append({"role": "model", "parts": [reply]})
    return reply


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — CHAIN OF 5
#  Without any loops, call chat() 5 times in a row.
#  Build a mini story: tell the AI a character's name, goal,
#  obstacle, plot twist, and ending — one per turn.
#  Print each reply.
# ════════════════════════════════════════════════════════════

history = []
# TODO: 5 sequential chat() calls building a story


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — MESSAGE COUNTER
#  Run a short chat (at least 6 turns).
#  After each turn, print how many total messages are in history.
#  Note: each turn adds 2 messages (user + model).
# ════════════════════════════════════════════════════════════

history = []

# TODO: write a chat loop that prints message count after each turn


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — HISTORY SLICER
#  After a 6-turn conversation, print only the last 2 exchanges
#  (4 messages from the end of history).
#  Hint: history[-4:]  gives the last 4 items in a list.
# ════════════════════════════════════════════════════════════

# TODO: run 6 turns, then slice and print the last 2 exchanges


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — LANGUAGE TUTOR
#  Build a Spanish-English language tutor chatbot.
#  System instruction: the AI is a friendly tutor that teaches
#  Spanish vocabulary. It asks the user for a word in English,
#  gives the Spanish translation and one example sentence,
#  then asks for the next word.
#  Run for 5 words minimum.
# ════════════════════════════════════════════════════════════

tutor_model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="TODO: write the language tutor system instruction"
)

history = []
# TODO: run the tutor loop


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: MEMORY EXPORT
#  After a conversation ends, save the full history to a file
#  called  chat_history.txt  in a readable format:
#    [You]  message text
#    [AI]   reply text
#    ---
#  Then write a load_history(filename) function that reads the file
#  back into the correct list-of-dicts format so the conversation
#  can be resumed in a future run.
# ════════════════════════════════════════════════════════════

def save_history(history, filename="chat_history.txt"):
    # TODO: write the history to a file
    pass

def load_history(filename="chat_history.txt"):
    # TODO: read the file and return a list of dicts
    pass
