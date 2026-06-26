# ============================================================
#  SPRINT 2 · WEEK 9 — Exercise Set
#  Topic: Gemini API, .env secrets, generate_content(), try/except
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SINGLE CALL, CLEAN OUTPUT
#  Ask the AI: "Give me 5 facts about Colombia in bullet points."
#  Print only the response text — no labels or extra formatting.
# ════════════════════════════════════════════════════════════

# TODO: write the API call and print statement


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — RESPONSE PROPERTIES
#  Ask any question. Then explore the response object:
#    response.text           -> the text answer
#    response.candidates     -> list of candidate answers
#    len(response.text)      -> character count
#  Print the character count and the first 100 characters.
# ════════════════════════════════════════════════════════════

response = model.generate_content("What is machine learning in one sentence?")

# TODO: print len(response.text)
# TODO: print response.text[:100]
# TODO: print response.candidates[0].finish_reason


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — BATCH QUESTIONS
#  Ask the AI the same question about 3 different topics.
#  Store the question template and topics in variables.
#  Print each response.
# ════════════════════════════════════════════════════════════

template = "Explain {topic} in exactly two sentences."
topics   = ["machine learning", "blockchain", "quantum computing"]

for topic in topics:
    question = template.format(topic=topic)
    # TODO: call the model and print the response


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — ERROR SAFE CALLER
#  Write a function  ask(prompt)  that:
#    - Calls model.generate_content(prompt)
#    - Returns response.text on success
#    - Returns "Error: {message}" on any exception
#  Test it with a normal prompt and with an empty string.
# ════════════════════════════════════════════════════════════

def ask(prompt):
    # TODO: implement with try/except
    pass

print(ask("What is the capital of Colombia?"))
print(ask(""))   # see what happens with empty input


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: QUIZ GENERATOR
#  Ask the AI to generate a 3-question multiple choice quiz
#  about a topic of your choice.
#  Parse the output to present each question one at a time.
#  Let the user answer, then reveal whether they are correct.
#
#  Hint: ask the AI to format the quiz as:
#    Q1: ...
#    A) ...  B) ...  C) ...  D) ...
#    Answer: A
#  Then split the response by "\n" and process line by line.
# ════════════════════════════════════════════════════════════

topic = input("Quiz topic: ")

# TODO: generate the quiz and turn it into an interactive experience
