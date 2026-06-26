# ============================================================
#  SPRINT 2 · WEEK 9 — Hello Gemini
#  Your First AI API Call
#
#  Before this session install the libraries:
#    pip install google-generativeai python-dotenv
#
#  Create a file called  .env  in this folder with this line:
#    GEMINI_API_KEY=your_key_here
#
#  Get a free key at:  aistudio.google.com  (sign in with Google)
#  Run:  python S2_W9_template.py
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

# ── STEP 1: Load the API key from .env ───────────────────────
# load_dotenv() reads the .env file and makes its values available
# via os.environ. This keeps secrets OUT of your code.
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file.")
    quit()

print("API key loaded successfully.")


# ── STEP 2: Configure and create the model ───────────────────
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")   # fast, free-tier friendly

print("Model ready.")


# ── STEP 3: Your first AI call ───────────────────────────────
# generate_content() sends a prompt and returns a response object.
# .text gives you the text content of the response.

response = model.generate_content("Say hello in 3 different languages.")
print("\nAI response:")
print(response.text)


# ── STEP 4: Ask your own question ────────────────────────────
# TODO: write a prompt asking the AI something YOU are curious about
my_question = "TODO"

# TODO: send my_question to the model and print the response


# ── STEP 5: Build an interactive Q&A loop ────────────────────
print("\n" + "=" * 40)
print("  ASK THE AI ANYTHING")
print("  Type 'quit' to exit")
print("=" * 40)

while True:
    question = input("\nYour question: ").strip()

    if question.lower() == "quit":
        print("Goodbye!")
        break

    if question == "":
        print("Please type a question.")
        continue

    # TODO: send question to the model and print the response text
    # TODO: wrap the call in a try/except block to handle network errors:
    #   try:
    #       response = model.generate_content(question)
    #       print(response.text)
    #   except Exception as e:
    #       print(f"Error: {e}")


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a "mode" selector at the start:
#   "1. Explain like I'm 10"
#   "2. Give a technical answer"
#   "3. Respond as a poet"
# Prefix the user's question with a different instruction
# depending on the mode chosen.
