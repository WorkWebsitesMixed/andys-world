# ============================================================
#  SPRINT 3 · WEEK 20 — TOOLKIT BUILD
#  The Personal Toolkit — main entry point
#
#  BUILD GUIDE — 60 minutes of project work.
#
#  What you are building:
#    A unified menu-driven CLI app that combines everything
#    from Sprints 1, 2, and 3 into one tool you actually use.
#
#  Architecture:
#    main.py         <- this file: menu + routing
#    tools/
#      organiser.py  <- file organiser (from W15)
#      digest.py     <- morning digest (from W17)
#      movies.py     <- movie explorer (from W18)
#      ai_chat.py    <- AI study assistant (from W12-13)
#
#  Minimum requirements:
#    [ ] A clear menu that shows all available tools
#    [ ] Each option calls the right module function
#    [ ] A "quit" option that exits cleanly
#    [ ] At least 3 working tools integrated
#    [ ] Error handling with try/except around API calls
#
#  Bonus features:
#    [ ] A settings menu (configure city, default notes file)
#    [ ] Save last-used settings to settings.json
#    [ ] A "help" option that explains each tool
#    [ ] Command-line args to jump directly to a tool:
#          python main.py --tool digest
# ============================================================

import os
import sys
from pathlib import Path

# ── Tool Imports ─────────────────────────────────────────────
# Uncomment these as you build each module:
# from tools.organiser import run_organiser
# from tools.digest    import run_digest
# from tools.movies    import run_movie_explorer
# from tools.ai_chat   import run_ai_chat

# For now, placeholder functions so the menu runs:
def run_organiser():
    print("[Organiser] Coming soon — paste your W15 code into tools/organiser.py")

def run_digest():
    print("[Digest] Coming soon — paste your W17 code into tools/digest.py")

def run_movie_explorer():
    print("[Movies] Coming soon — paste your W18 code into tools/movies.py")

def run_ai_chat():
    print("[AI Chat] Coming soon — paste your W13 code into tools/ai_chat.py")


# ── Menu ─────────────────────────────────────────────────────
TOOLS = {
    "1": ("File Organiser",    run_organiser),
    "2": ("Morning Digest",    run_digest),
    "3": ("Movie Explorer",    run_movie_explorer),
    "4": ("AI Study Assistant",run_ai_chat),
}

def show_menu():
    print()
    print("=" * 42)
    print("  PERSONAL TOOLKIT")
    print("=" * 42)
    for key, (name, _) in TOOLS.items():
        print(f"  {key}. {name}")
    print("  q. Quit")
    print("=" * 42)

def main():
    print("Welcome to your Personal Toolkit.")
    print("Built with Python. Powered by you.")

    while True:
        show_menu()
        choice = input("\nSelect tool: ").strip().lower()

        if choice == "q":
            print("\nGoodbye!")
            break

        if choice in TOOLS:
            name, func = TOOLS[choice]
            print(f"\n--- {name} ---")
            try:
                func()
            except Exception as e:
                print(f"Error in {name}: {e}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# ── Build Checklist ──────────────────────────────────────────
#
#  Step 1 (10 min): Create a  tools/  folder.
#                   Add an empty  tools/__init__.py  file.
#
#  Step 2 (15 min): Copy your W15 organiser code into  tools/organiser.py.
#                   Wrap the main logic in a  run_organiser()  function.
#                   Uncomment its import above and test option 1.
#
#  Step 3 (15 min): Copy your W17 digest code into  tools/digest.py.
#                   Wrap in  run_digest()  and test option 2.
#
#  Step 4 (10 min): Connect one more tool (movies or AI).
#
#  Step 5 (10 min): Polish: error handling, clear screen between tools,
#                   press Enter to return to menu.
