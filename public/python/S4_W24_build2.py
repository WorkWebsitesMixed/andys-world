"""
S4_W24_build2.py  --  Build Sprint 2 guide
Week 24: All MUSTs working end-to-end. Start first SHOULD.

Checklist: run through this BEFORE the session ends.
"""

# ─────────────────────────────────────────────────────────────────────
# MUST FEATURE ACCEPTANCE TESTS
# For each MUST, write one test call here. If it runs without error = done.
# ─────────────────────────────────────────────────────────────────────

# Uncomment and fill in when ready to test:

# print("Testing MUST 1:")
# result_1 = must_feature_1()
# assert result_1 is not None, "MUST 1 returned None"
# print("  PASS")

# print("Testing MUST 2:")
# result_2 = must_feature_2()
# assert result_2 is not None, "MUST 2 returned None"
# print("  PASS")

# print("Testing MUST 3:")
# result_3 = must_feature_3()
# assert result_3 is not None, "MUST 3 returned None"
# print("  PASS")


# ─────────────────────────────────────────────────────────────────────
# SHOULD FEATURE START
# ─────────────────────────────────────────────────────────────────────

def should_feature_1():
    """First SHOULD feature. Only implement after all MUSTs pass."""
    print("TODO: should_feature_1")


# ─────────────────────────────────────────────────────────────────────
# SCOPE CHANGE LOG (if you changed anything from your Week 22 design)
# ─────────────────────────────────────────────────────────────────────

SCOPE_CHANGES = [
    # {"original": "...", "changed_to": "...", "reason": "..."},
]


# ─────────────────────────────────────────────────────────────────────
# END-OF-SESSION STATUS
# ─────────────────────────────────────────────────────────────────────

MUST_STATUS = {
    "MUST_1": "done",     # done / in-progress / blocked
    "MUST_2": "in-progress",
    "MUST_3": "not-started",
}

SHOULD_STATUS = {
    "SHOULD_1": "not-started",
}

print("Week 24 status:")
for k, v in MUST_STATUS.items():
    print(f"  {k}: {v}")
