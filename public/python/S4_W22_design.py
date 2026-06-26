# ============================================================
#  SPRINT 4 · WEEK 22 — Architecture
#  Final Project Design Session
#
#  This file is your PROJECT BLUEPRINT.
#  Fill it in during class. This becomes your technical spec.
#  You will refer back to it every build week.
# ============================================================


# ════════════════════════════════════════════════════════════
#  SECTION 1 — PROJECT IDENTITY
#  Fill in these strings.
# ════════════════════════════════════════════════════════════

PROJECT_NAME  = "TODO: your project name"
STUDENT_NAME  = "TODO: your name"
DESCRIPTION   = (
    "TODO: one paragraph describing what your tool does, "
    "who it is for, and why it is useful."
)
START_DATE    = "2026-"   # TODO: fill in today's date
SHOWCASE_DATE = "2026-"   # TODO: fill in the Week 27 date

print(f"Project: {PROJECT_NAME}")
print(f"Student: {STUDENT_NAME}")
print(f"Description: {DESCRIPTION}")


# ════════════════════════════════════════════════════════════
#  SECTION 2 — FEATURES LIST
#  List every feature your tool will have.
#  Mark each as MUST (required), SHOULD (important), or COULD (nice).
# ════════════════════════════════════════════════════════════

FEATURES = [
    # Format: ("Feature name", "MUST/SHOULD/COULD", "Which sprint built this skill")
    ("Main menu",                "MUST",   "Sprint 3 W19"),
    ("File organiser",           "MUST",   "Sprint 3 W15"),
    ("AI study assistant",       "MUST",   "Sprint 2 W13"),
    ("Morning digest",           "SHOULD", "Sprint 3 W17"),
    ("Movie / music explorer",   "COULD",  "Sprint 3 W18"),
    # TODO: add at least 2 features of your own
]

print("\nFEATURES:")
for name, priority, source in FEATURES:
    print(f"  [{priority:6}] {name:30} (from {source})")


# ════════════════════════════════════════════════════════════
#  SECTION 3 — FILE STRUCTURE
#  Plan where every file will live BEFORE you write any code.
# ════════════════════════════════════════════════════════════

FILE_STRUCTURE = """
my_toolkit/
    main.py              <- entry point, menu, routing
    .env                 <- API keys (never share this file)
    settings.json        <- user preferences (city, default notes file)
    data/
        notes/           <- user's study note .txt files
        favourites.json  <- saved movies/songs
        digest_log.txt   <- saved morning digests
    tools/
        __init__.py      <- makes tools/ a Python package
        organiser.py     <- file organiser module
        digest.py        <- morning digest module
        ai_chat.py       <- AI study assistant module
        movies.py        <- movie explorer module
        # TODO: add any extra tool files you plan
    utils/
        __init__.py
        display.py       <- shared print helpers (clear screen, banners)
        config.py        <- load/save settings.json
"""

print("\nFILE STRUCTURE:")
print(FILE_STRUCTURE)


# ════════════════════════════════════════════════════════════
#  SECTION 4 — PSEUDOCODE
#  Write the logic of your main() function in plain English
#  before you write any Python.
# ════════════════════════════════════════════════════════════

PSEUDOCODE_MAIN = """
START
  Load settings from settings.json (city, notes file)
  Print welcome banner with project name

  LOOP:
    Show menu with all tool names and numbers
    Get user choice

    IF choice == "1":  run file organiser
    IF choice == "2":  run morning digest
    IF choice == "3":  run AI study assistant
    IF choice == "4":  run movie explorer
    IF choice == "s":  open settings editor
    IF choice == "q":  print goodbye and STOP

    After each tool, press Enter to return to menu
END
"""

print("PSEUDOCODE (main):")
print(PSEUDOCODE_MAIN)


# ════════════════════════════════════════════════════════════
#  SECTION 5 — RISK REGISTER
#  What could go wrong? Plan for it now.
# ════════════════════════════════════════════════════════════

RISKS = [
    # (risk, likelihood, mitigation)
    ("API key missing or expired",       "High",   "Always check .env on startup; print a clear error message"),
    ("No internet connection",           "Medium", "Wrap all API calls in try/except; offer an offline fallback"),
    ("User enters invalid menu choice",  "High",   "Validate input with a while loop; never let the program crash"),
    ("Notes file not found",             "Medium", "Check Path.exists() before reading; ask user for correct path"),
    # TODO: add 2 more risks
]

print("RISK REGISTER:")
for risk, likelihood, mitigation in RISKS:
    print(f"  [{likelihood:6}] {risk}")
    print(f"           -> {mitigation}")
    print()
