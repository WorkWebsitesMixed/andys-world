# ============================================================
#  SPRINT 3 · WEEK 15 — Exercise Set
#  Topic: os, pathlib, shutil, file system operations
# ============================================================

from pathlib import Path
import shutil
import os


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — EXPLORER
#  Print a tree of the current directory.
#  For each item: show whether it is a FILE or DIR, and its size in bytes.
#  Hint: item.stat().st_size gives the size in bytes.
#  Format:  [FILE]  build.sh            550 bytes
#           [DIR ]  sandbox             --
# ════════════════════════════════════════════════════════════

for item in Path(".").iterdir():
    # TODO: print file/dir label, name, and size


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — DUPLICATE FINDER
#  In the list below, find all filenames that appear more than once.
#  Print each duplicate and how many times it appears.
#  (In a real version you would read from a real directory.)
# ════════════════════════════════════════════════════════════

filenames = [
    "report.pdf", "notes.txt", "report.pdf", "photo.jpg",
    "notes.txt", "data.csv", "photo.jpg", "photo.jpg"
]

counts = {}
for name in filenames:
    # TODO: count occurrences using dict.get()
    pass

for name, count in counts.items():
    if count > 1:
        print(f"DUPLICATE: {name} appears {count} times")


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — RENAME BATCH
#  Create 5 test files named file_1.txt through file_5.txt.
#  Rename each one to add today's date as a prefix:
#    2026-08-10_file_1.txt
#  Hint: from datetime import date; str(date.today())
#  Clean up (delete) all renamed files at the end.
# ════════════════════════════════════════════════════════════

from datetime import date
today = str(date.today())

# Create test files
for i in range(1, 6):
    Path(f"file_{i}.txt").write_text(f"File {i}")

# TODO: rename each file with the date prefix using Path.rename()
# TODO: delete the renamed files at the end


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — SEARCH FOR EXTENSION
#  Write a function  find_files(directory, extension)  that
#  returns a list of all files with that extension in the directory.
#  Test it on "." (current dir) for ".py" and ".pdf".
#  Print the results with full paths.
# ════════════════════════════════════════════════════════════

def find_files(directory, extension):
    # TODO: use Path.iterdir() and filter by suffix
    pass

py_files  = find_files(".", ".py")
pdf_files = find_files(".", ".pdf")

print(f"\nPython files: {len(py_files)}")
for f in py_files:
    print(f"  {f}")


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: FOLDER SIZE REPORTER
#  Write a function  folder_report(directory)  that:
#    - Walks ALL sub-folders recursively (hint: Path.rglob("*"))
#    - Counts total files and total size in bytes
#    - Groups files by extension with count and total size per group
#    - Prints a table sorted by total size descending
#
#  Format:
#    Extension  | Files | Total Size
#    .pdf       |   12  | 4.5 MB
#    .py        |    8  | 24.3 KB
# ════════════════════════════════════════════════════════════

def folder_report(directory):
    pass  # TODO: implement

folder_report(".")
