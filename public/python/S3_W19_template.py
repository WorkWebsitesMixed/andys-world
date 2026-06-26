# ============================================================
#  SPRINT 3 · WEEK 19 — CLI Tools
#  Run Scripts Like a Real Developer Tool
#
#  Run examples:
#    python S3_W19_template.py
#    python S3_W19_template.py --help
#    python S3_W19_template.py greet --name Sofia
#    python S3_W19_template.py weather --city Medellin
# ============================================================

import sys
import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()


# ── STEP 1: sys.argv — what the terminal passes to Python ────
# sys.argv is a list. sys.argv[0] is the script name.
# Any words after the script name become sys.argv[1], [2], etc.

print("sys.argv contents:")
print(sys.argv)
print(f"Script name:   {sys.argv[0]}")
print(f"Total args:    {len(sys.argv) - 1}")   # minus 1 for the script name

if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")


# ── STEP 2: Manual argument parsing ─────────────────────────
# Before argparse existed, developers did this by hand.
# It gets messy fast — which is why argparse was invented.

if len(sys.argv) >= 2 and sys.argv[1] == "greet":
    if len(sys.argv) >= 4 and sys.argv[2] == "--name":
        name = sys.argv[3]
        print(f"\nHello, {name}!")
    else:
        print("\nUsage:  python script.py greet --name YourName")


# ── STEP 3: argparse — the professional way ──────────────────
def build_parser():
    """Creates and returns the argument parser."""
    parser = argparse.ArgumentParser(
        description="Personal Toolkit CLI — your tools in one place",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python S3_W19_template.py greet --name Sofia\n"
            "  python S3_W19_template.py weather --city Bogota\n"
            "  python S3_W19_template.py count --file notes.txt\n"
        )
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # greet subcommand
    greet_parser = subparsers.add_parser("greet", help="Print a greeting")
    greet_parser.add_argument("--name", required=True, help="Your name")
    greet_parser.add_argument("--lang", default="en", choices=["en", "es", "fr"],
                              help="Language (default: en)")

    # weather subcommand
    weather_parser = subparsers.add_parser("weather", help="Fetch live weather")
    weather_parser.add_argument("--city", required=True, help="City name")

    # count subcommand
    count_parser = subparsers.add_parser("count", help="Count words in a file")
    count_parser.add_argument("--file", required=True, help="Path to text file")

    return parser


# ── STEP 4: Command handlers ─────────────────────────────────
def cmd_greet(args):
    greetings = {"en": "Hello", "es": "Hola", "fr": "Bonjour"}
    word      = greetings.get(args.lang, "Hello")
    print(f"{word}, {args.name}! Welcome to the Personal Toolkit.")

def cmd_weather(args):
    api_key = os.environ.get("OPENWEATHER_KEY", "YOUR_KEY")
    url     = (f"https://api.openweathermap.org/data/2.5/weather"
               f"?q={args.city}&appid={api_key}&units=metric")
    try:
        data = requests.get(url).json()
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].title()
            print(f"{args.city}: {temp}C, {desc}")
        else:
            print(f"City not found: {args.city}")
    except Exception as e:
        print(f"Error: {e}")

def cmd_count(args):
    # TODO: open args.file, count lines/words/characters, print the summary
    pass


# ── STEP 5: Route commands ───────────────────────────────────
def main():
    parser = build_parser()
    args   = parser.parse_args()

    if args.command == "greet":
        cmd_greet(args)
    elif args.command == "weather":
        cmd_weather(args)
    elif args.command == "count":
        cmd_count(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a  movies  subcommand that fetches an OMDb movie.
# Add a  --verbose  flag (store_true) to all commands that
# prints extra detail when enabled.
# Add  --output FILE  to the count command that saves the result.
