# ============================================================
#  SPRINT 3 · WEEK 16 — CSV & Data
#  Grade Tracker with pandas
#
#  Before this session:
#    pip install pandas
#
#  This session uses  sample_grades.csv  in this folder.
#  Run:  python S3_W16_template.py
# ============================================================

import csv
import pandas as pd
from pathlib import Path


# ── STEP 1: Read a CSV with the standard library ─────────────
print("METHOD 1: csv module")
print("-" * 30)

with open("sample_grades.csv", "r") as f:
    reader = csv.DictReader(f)   # DictReader gives each row as a dict
    for row in reader:
        # TODO: print each student's name and their math grade
        pass


# ── STEP 2: Write a new CSV file ─────────────────────────────
new_data = [
    {"name": "Sofia",     "score": 92},
    {"name": "Ana",       "score": 85},
    {"name": "Maria",     "score": 97},
]

with open("scores.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    # TODO: use  writer.writerows(new_data)  to write all rows at once

print("\nscores.csv written.")


# ── STEP 3: pandas — read and explore ────────────────────────
print("\nMETHOD 2: pandas")
print("-" * 30)

df = pd.read_csv("sample_grades.csv")

print("First 3 rows:")
print(df.head(3))          # head(n) shows the first n rows

print("\nColumn names:")
print(df.columns.tolist())

print("\nShape (rows, columns):")
print(df.shape)            # (number of rows, number of columns)

print("\nBasic statistics:")
print(df.describe())       # count, mean, min, max, etc.


# ── STEP 4: Filter and select ────────────────────────────────
# Access a column:  df["column_name"]
# Filter rows:      df[df["column"] > value]

print("\nStudents with math grade above 85:")
# TODO: create a filtered dataframe: df[df["math"] > 85]
#       print it


print("\nJust names and averages:")
# TODO: select two columns: df[["student", "average"]]
#       print it


# ── STEP 5: Sort and find extremes ───────────────────────────
top_student = df.loc[df["average"].idxmax()]   # row with the highest average
print(f"\nTop student: {top_student['student']} ({top_student['average']} avg)")

# TODO: find and print the student with the LOWEST average
# TODO: sort the dataframe by average descending and print it
#       hint: df.sort_values("average", ascending=False)


# ── STEP 6: Add a new column ─────────────────────────────────
def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

df["grade"] = df["average"].apply(letter_grade)
# TODO: print the dataframe with the new grade column
# TODO: save it to  graded_results.csv  using df.to_csv(filename, index=False)


# ── BONUS (Advanced) ─────────────────────────────────────────
# Add a column "passed" that is True if average >= 70, False otherwise.
# Count how many students passed and how many failed.
# Generate a simple bar chart using  df["grade"].value_counts().plot(kind="bar")
# Hint: pip install matplotlib  then  import matplotlib.pyplot as plt; plt.show()
