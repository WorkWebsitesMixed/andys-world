# ============================================================
#  SPRINT 2 · WEEK 10 — Exercise Set
#  Topic: system instructions, personas, temperature, GenerationConfig
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SAME QUESTION, 3 TONES
#  Ask "What is photosynthesis?" to 3 models:
#    1. No system instruction (default)
#    2. "Answer as if the user is 6 years old."
#    3. "Answer as a university biology professor."
#  Print each response with a clear label.
# ════════════════════════════════════════════════════════════

question = "What is photosynthesis?"

# TODO: create 3 models with different system instructions and print results


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — INVENT A PERSONA
#  Create a model with a system instruction for a persona of YOUR choice.
#  (Ideas: a pirate, a robot, a time traveller from 1920, a football coach)
#  Ask it 3 questions and verify that it stays in character.
# ════════════════════════════════════════════════════════════

my_persona_model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="TODO: write your persona here"
)

questions = [
    "What is the internet?",
    "How do you feel about Mondays?",
    "What is your greatest achievement?",
]

for q in questions:
    # TODO: print the question and the response


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — TEMPERATURE EXPERIMENT
#  Use the same creative prompt at temperatures 0.1, 0.9, and 1.8.
#  Print all three responses.
#  Write a comment describing what you observe between them.
# ════════════════════════════════════════════════════════════

from google.generativeai.types import GenerationConfig

prompt = "Write a one-line description of the colour blue."

for temp in [0.1, 0.9, 1.8]:
    config = GenerationConfig(temperature=temp)
    model  = genai.GenerativeModel("gemini-1.5-flash")
    # TODO: generate and print the response with label


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — PROMPT PREFIX TRICK
#  Instead of a system instruction, prefix the user's question
#  with an instruction inside the same string.
#  Compare results with and without the prefix.
#
#  Example prefix: "Respond only with bullet points. Question: "
# ════════════════════════════════════════════════════════════

model = genai.GenerativeModel("gemini-1.5-flash")
base_question = "Tell me about artificial intelligence."
prefix = "TODO: write a prefix instruction here. Question: "

# TODO: send base_question alone, then prefix + base_question
#       print and compare


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: AUTOMATED WRITING COACH
#  Ask the user to write a short paragraph (3-5 sentences).
#  Send it to the AI with a system instruction that makes it:
#    1. Identify 2 strengths
#    2. Suggest 1 specific improvement
#    3. Rewrite the paragraph applying the improvement
#  Format the output clearly.
# ════════════════════════════════════════════════════════════

writing_coach = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="TODO: write the writing coach system instruction"
)

print("Writing Coach — paste your paragraph, then press Enter twice.")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

user_text = "\n".join(lines)
# TODO: send user_text to writing_coach and print the response
