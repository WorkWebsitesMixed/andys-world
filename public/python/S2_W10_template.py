# ============================================================
#  SPRINT 2 · WEEK 10 — Prompt Engineering in Code
#  AI Personas: same question, wildly different answers
#
#  Run:  python S2_W10_template.py
# ============================================================

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


# ── STEP 1: The system instruction ───────────────────────────
# A system instruction tells the model WHO it is before any question.
# It shapes tone, vocabulary, and personality for the whole session.

model_default = genai.GenerativeModel("gemini-1.5-flash")

model_teacher = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="You are a patient, encouraging secondary school teacher. "
                       "Always use simple language, real-life examples, and end "
                       "with one check-in question."
)

test_question = "What is gravity?"

print("DEFAULT MODEL:")
print(model_default.generate_content(test_question).text)

print("\nTEACHER PERSONA:")
print(model_teacher.generate_content(test_question).text)


# ── STEP 2: Build your own personas ──────────────────────────
# TODO: create model_chef with a system instruction that makes the AI
#       answer every question as a passionate Colombian chef.
model_chef = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="TODO: write the chef's system instruction here"
)

# TODO: create model_poet that answers only in short rhyming poems.
model_poet = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="TODO"
)

print("\nCHEF PERSONA:")
# TODO: send test_question to model_chef and print the response

print("\nPOET PERSONA:")
# TODO: send test_question to model_poet and print the response


# ── STEP 3: Persona selector ─────────────────────────────────
PERSONAS = {
    "1": ("Default",  model_default),
    "2": ("Teacher",  model_teacher),
    "3": ("Chef",     model_chef),
    "4": ("Poet",     model_poet),
}

def show_persona_menu():
    print("\n--- Choose a persona ---")
    for key, (name, _) in PERSONAS.items():
        print(f"  {key}. {name}")

print("\n" + "=" * 40)
print("  PERSONA PLAYGROUND")
print("  Ask anything — the AI changes who it is")
print("=" * 40)

while True:
    show_persona_menu()
    choice = input("Persona (or 'quit'): ").strip()

    if choice == "quit":
        break

    if choice not in PERSONAS:
        print("Invalid choice.")
        continue

    persona_name, active_model = PERSONAS[choice]
    question = input(f"Ask the {persona_name}: ").strip()

    # TODO: send question to active_model and print the response


# ── STEP 4: Temperature — controlling creativity ──────────────
# Temperature (0.0 to 2.0) controls randomness.
# Low temp (0.2) = focused, predictable.  High temp (1.8) = creative, wild.
# GenerationConfig lets you set temperature and other parameters.

from google.generativeai.types import GenerationConfig

model_focused  = genai.GenerativeModel("gemini-1.5-flash")
model_creative = genai.GenerativeModel("gemini-1.5-flash")

config_focused  = GenerationConfig(temperature=0.2)
config_creative = GenerationConfig(temperature=1.8)

creative_prompt = "Invent a name for a new planet and describe it in 2 sentences."

print("\nFOCUSED (low temp):")
print(model_focused.generate_content(creative_prompt, generation_config=config_focused).text)

print("\nCREATIVE (high temp):")
# TODO: send the same prompt with config_creative and print


# ── BONUS (Advanced) ─────────────────────────────────────────
# Build a "Debate Bot": give it the system instruction to always argue
# the OPPOSITE of whatever the user says. Test it with 5 statements.
