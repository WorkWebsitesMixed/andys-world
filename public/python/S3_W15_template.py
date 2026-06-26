# ============================================================
#  SPRINT 3 · WEEK 15 — File System Automation
#  Desktop Organiser: sort 50 files in under a second
#
#  Run:  python S3_W15_template.py
# ============================================================

import os
import shutil
from pathlib import Path


# ── STEP 1: List files in a directory ────────────────────────
# Path(".") means "the current folder".
# .iterdir() yields every item inside it.

current_dir = Path(".")

print("Files in this folder:")
for item in current_dir.iterdir():
    if item.is_file():
        # TODO: print item.name and item.suffix (the extension e.g. ".py")
        pass


# ── STEP 2: Create and remove directories ────────────────────
test_dir = Path("test_folder")

test_dir.mkdir(exist_ok=True)   # exist_ok=True means no error if it already exists
print(f"\nCreated: {test_dir}")

# Write a test file inside it
(test_dir / "hello.txt").write_text("Hello from Python!")

print(f"Contents of {test_dir}:")
for item in test_dir.iterdir():
    print(f"  {item.name}")

# TODO: delete the test file using  (test_dir / "hello.txt").unlink()
# TODO: delete the now-empty directory using  test_dir.rmdir()


# ── STEP 3: Move and copy files ──────────────────────────────
# shutil.move(src, dst)  moves a file
# shutil.copy(src, dst)  copies a file

# First create a file to move
source = Path("to_move.txt")
source.write_text("I will be moved.")

dest_dir = Path("moved_files")
dest_dir.mkdir(exist_ok=True)

shutil.move(str(source), str(dest_dir / source.name))
print(f"\nMoved {source.name} to {dest_dir}/")
# TODO: verify the move by listing dest_dir.iterdir()

shutil.rmtree(dest_dir)   # removes a non-empty directory


# ── STEP 4: Categorise files by extension ────────────────────
CATEGORIES = {
    ".py":   "Python_Scripts",
    ".txt":  "Text_Files",
    ".pdf":  "PDFs",
    ".jpg":  "Images",
    ".jpeg": "Images",
    ".png":  "Images",
    ".csv":  "Data",
}

def get_category(suffix):
    """Returns the folder name for a given file extension."""
    return CATEGORIES.get(suffix.lower(), "Other")

# Test it:
for ext in [".py", ".txt", ".jpg", ".docx"]:
    print(f"{ext:8} -> {get_category(ext)}")


# ── STEP 5: The organiser ────────────────────────────────────
def organise(target_dir):
    """
    Moves all files in target_dir into sub-folders by category.
    Skips directories and the script itself.
    """
    target = Path(target_dir)

    if not target.exists():
        print(f"Directory not found: {target_dir}")
        return

    moved = 0

    for item in target.iterdir():
        if item.is_dir():
            continue   # skip sub-folders
        if item.name == Path(__file__).name:
            continue   # skip this script

        category   = get_category(item.suffix)
        dest_folder = target / category
        dest_folder.mkdir(exist_ok=True)

        # TODO: move item into dest_folder using shutil.move()
        #       print what you moved and where
        moved += 1

    print(f"\nDone. Moved {moved} files.")

# To test: create a "sandbox" folder, put some test files in it,
# then call:  organise("sandbox")
sandbox = Path("sandbox")
sandbox.mkdir(exist_ok=True)
(sandbox / "notes.txt").write_text("test")
(sandbox / "script.py").write_text("print('hi')")
(sandbox / "data.csv").write_text("a,b\n1,2")

organise("sandbox")
shutil.rmtree("sandbox")   # clean up after demo


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a  dry_run=True  parameter to organise() that prints what
# it WOULD do without actually moving anything.
# Add a log: write each move to  organiser_log.txt  with a timestamp.
