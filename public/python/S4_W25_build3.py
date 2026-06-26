"""
S4_W25_build3.py  --  Build Sprint 3 + Polish guide
Week 25: Last build session. Finish. Harden. Freeze.

Go through EVERY item on the polish checklist below.
"""

# ─────────────────────────────────────────────────────────────────────
# POLISH CHECKLIST  (change False to True as you complete each item)
# ─────────────────────────────────────────────────────────────────────

CHECKLIST = {
    "Program starts without crashing":          False,
    "All MUSTs work end-to-end":                False,
    "Empty/wrong input gives friendly message": False,
    "API errors caught and displayed cleanly":  False,
    "Output formatted consistently":            False,
    "Welcome banner on startup":                False,
    "README comment block in main.py":          False,
    "No hardcoded API keys":                    False,
    ".env.example file exists":                 False,
    "At least one SHOULD implemented":          False,
}

def print_checklist():
    done  = sum(1 for v in CHECKLIST.values() if v)
    total = len(CHECKLIST)
    print(f"\nPolish checklist: {done}/{total} complete")
    for item, status in CHECKLIST.items():
        mark = "OK" if status else "--"
        print(f"  [{mark}] {item}")

print_checklist()


# ─────────────────────────────────────────────────────────────────────
# ERROR HANDLING TEMPLATE
# Add this pattern around any API call or file operation:
# ─────────────────────────────────────────────────────────────────────

def safe_call(fn, *args, **kwargs):
    """Wrapper that catches any exception and returns None on failure."""
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────
# README COMMENT TEMPLATE  (paste at the top of your main.py)
# ─────────────────────────────────────────────────────────────────────

README_TEMPLATE = """
# ============================================================
# PROJECT: <name>
# ============================================================
# DESCRIPTION:
#   <one or two sentences>
#
# REQUIREMENTS:
#   pip install google-generativeai python-dotenv requests pandas
#
# SETUP:
#   1. Copy .env.example to .env
#   2. Add your API keys to .env
#
# HOW TO RUN:
#   python main.py
#
# FEATURES:
#   - <MUST 1>
#   - <MUST 2>
#   - <MUST 3>
# ============================================================
"""

# ─────────────────────────────────────────────────────────────────────
# .env.example TEMPLATE  (save as .env.example in your project folder)
# ─────────────────────────────────────────────────────────────────────

ENV_EXAMPLE = """
GEMINI_API_KEY=your_gemini_key_here
WEATHER_API_KEY=your_openweathermap_key_here
NEWS_API_KEY=your_newsapi_key_here
OMDB_API_KEY=your_omdb_key_here
"""

# Remove any keys your project does not use.
