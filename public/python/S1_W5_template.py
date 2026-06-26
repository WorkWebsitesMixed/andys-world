# ============================================================
#  SPRINT 1 · WEEK 5 — Functions
#  Game Menu
#
#  Fill in every TODO. Run after each step.
#  Run:  python S1_W5_template.py
# ============================================================


# ── STEP 1: Why functions? ───────────────────────────────────
# Without a function you'd repeat this block for every greeting:
#   print("Hello, Ana!")
#   print("Hello, Sofia!")
#   print("Hello, Maria!")
# With a function, you write it once and call it three times.

def greet(name):
    """Prints a personalised greeting."""
    print(f"Hello, {name}! Welcome to the game.")

greet("Ana")
greet("Sofia")
greet("Maria")


# ── STEP 2: A function that returns a value ──────────────────
def roll_dice(sides):
    """Returns a random number from 1 to sides."""
    import random
    return random.randint(1, sides)   # return sends the value back to the caller

result = roll_dice(6)
print(f"You rolled: {result}")

# TODO: call roll_dice with 20 sides and print the result


# ── STEP 3: Build the game menu ──────────────────────────────
def show_menu():
    """Prints the main menu. Returns nothing."""
    print("\n" + "=" * 30)
    print("  ADVENTURE GAME")
    print("  1. New game")
    print("  2. Instructions")
    print("  3. Quit")
    print("=" * 30)


def show_instructions():
    """Prints the game instructions."""
    # TODO: print 3-4 lines of made-up instructions for your game


def play_game():
    """Starts a new game round (placeholder)."""
    player = input("Enter your character name: ")
    hp     = 10
    print(f"\n{player} enters the dungeon with {hp} HP...")
    # TODO: add 2 more print lines to describe the start of the game


# ── STEP 4: The main loop ────────────────────────────────────
# Now wire everything together with a while loop.

def main():
    """Main program entry point."""
    print("WELCOME TO THE ADVENTURE GAME")

    while True:
        show_menu()
        choice = input("Choose (1/2/3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            # TODO: print an error message for invalid choices
            pass


# ── STEP 5: Run the program ──────────────────────────────────
# This pattern means: only run main() if this file is executed directly.
# (We will understand this fully when we build multi-file projects.)
if __name__ == "__main__":
    main()


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a  check_password()  function that asks for a secret word.
# Only let the user start a new game if the password is correct.
# Return True if correct, False if wrong.
# Call it inside play_game() before the game starts.
