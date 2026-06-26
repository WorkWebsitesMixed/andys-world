# ============================================================
#  SPRINT 3 · WEEK 19 — Exercise Set
#  Topic: sys.argv, argparse, subcommands, CLI design
# ============================================================

import sys
import argparse


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SYS.ARGV PRACTICE
#  Run this script with different arguments and observe output.
#  Then: modify the script so that if no arguments are given,
#  it prints a usage hint instead of crashing.
#
#  Run:  python S3_W19_exercises.py hello world 42
# ════════════════════════════════════════════════════════════

print(f"Number of arguments: {len(sys.argv) - 1}")
for i, arg in enumerate(sys.argv[1:], 1):
    print(f"  Arg {i}: {arg}")

# TODO: add a check: if len(sys.argv) == 1, print usage and exit


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — SIMPLE CALCULATOR CLI
#  Build a calculator that runs from the command line:
#    python ex2_calc.py add 5 3       ->  5 + 3 = 8
#    python ex2_calc.py multiply 4 7  ->  4 * 7 = 28
#
#  Use argparse with subcommands: add, subtract, multiply, divide
#  Each subcommand takes two positional arguments: a and b (floats).
# ════════════════════════════════════════════════════════════

# Save this as  ex2_calc.py  (or uncomment and run it directly):
# parser = argparse.ArgumentParser(description="CLI Calculator")
# subparsers = parser.add_subparsers(dest="op")
#
# for op in ["add", "subtract", "multiply", "divide"]:
#     p = subparsers.add_parser(op)
#     p.add_argument("a", type=float)
#     p.add_argument("b", type=float)
#
# args = parser.parse_args()
# TODO: route to the right operation and print the result


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — HELP TEXT QUALITY
#  A good CLI tool has clear help text.
#  Build a parser for a "notes" tool with these subcommands:
#    add --title TEXT --body TEXT    (adds a note)
#    list                            (lists all notes)
#    search --keyword TEXT           (searches notes)
#  Every argument must have a descriptive  help=  string.
#  Run the script with  --help  and each subcommand with  --help.
# ════════════════════════════════════════════════════════════

# TODO: build the notes parser with quality help strings
# You do not need to implement the actual storage — just the parser.


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — VALIDATE INPUTS
#  Build a CLI that accepts a date in YYYY-MM-DD format.
#  If the format is wrong, print a clear error and exit with code 1.
#  If the date is in the future, print "Upcoming date".
#  If the date is in the past, print "Past date".
#  Hint: from datetime import datetime
#        datetime.strptime(date_str, "%Y-%m-%d")  parses the string
# ════════════════════════════════════════════════════════════

from datetime import datetime

parser = argparse.ArgumentParser(description="Date checker")
parser.add_argument("date", help="Date in YYYY-MM-DD format")
args = parser.parse_args()

# TODO: parse the date and print past/future
# TODO: handle ValueError if the format is wrong


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: PIPELINE
#  Build a CLI tool that chains two operations:
#    python pipeline.py fetch-weather --city Medellin --save weather.txt
#    python pipeline.py read-file --file weather.txt --word-count
#    python pipeline.py summarize --file weather.txt  (uses AI)
#
#  The output of one command can be piped into the next.
#  Each subcommand should work independently AND as part of a chain.
# ════════════════════════════════════════════════════════════

# TODO: design and implement the pipeline CLI
