"""
S4_W26_rehearsal.py  --  Showcase rehearsal guide
Week 26: No new code. Run the demo until it is fluent.

Fill in your talking points below. Read them aloud while running the demo.
"""

# ─────────────────────────────────────────────────────────────────────
# TALKING POINTS (5 minutes)
# ─────────────────────────────────────────────────────────────────────

HOOK = """
This project solves [PROBLEM] that I/someone I know actually has.
Before I wrote this, I had to [MANUAL STEP] every time I wanted to [GOAL].
Now I just run one command.
"""

DEMO_RUN_1 = """
(Run the main workflow here. Type slowly and clearly.)
WHAT TO TYPE:  ...
WHAT TO SAY:   ...
EXPECTED OUTPUT: ...
"""

TECHNICAL_DECISION = """
I chose to use [X] because [Y].
The alternative was [Z], but it would have [PROBLEM].
Here is the line of code: (open VS Code, point to it)
"""

DEMO_RUN_2 = """
(Show error handling. What happens with bad input?)
WHAT TO TYPE:  ...
WHAT TO SAY:   "What happens if the user types the wrong thing?"
EXPECTED:      A friendly error message, NOT a Python traceback.
"""

CLOSE = """
If I had two more weeks, I would add [SHOULD or COULD feature].
The most interesting thing I learned building this was [INSIGHT].
"""


# ─────────────────────────────────────────────────────────────────────
# TIMING LOG (fill in after each rehearsal run)
# ─────────────────────────────────────────────────────────────────────

REHEARSAL_LOG = [
    # {"run": 1, "duration_seconds": 0, "over_time": False, "cut": ""},
]


# ─────────────────────────────────────────────────────────────────────
# TOMORROW'S CHECKLIST
# ─────────────────────────────────────────────────────────────────────

TOMORROW = {
    ".env file on showcase machine":        False,
    "All packages installed":               False,
    "Project folder on Desktop":            False,
    "VS Code font size >= 16pt":            False,
    "Terminal font size >= 16pt":           False,
    "Backup screenshot/recording ready":    False,
    "Talking points memorised":             False,
}

def print_tomorrow():
    done = sum(1 for v in TOMORROW.values() if v)
    print(f"\nShowcase checklist: {done}/{len(TOMORROW)}")
    for item, status in TOMORROW.items():
        mark = "OK" if status else "--"
        print(f"  [{mark}] {item}")

print_tomorrow()
print("\nGood luck tomorrow. You have built something real.")
