# ============================================================
#  SPRINT 3 · WEEK 16 — Exercise Set
#  Topic: csv module, pandas, DataFrame operations
# ============================================================

import csv
import pandas as pd


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — CSV READ AND SUMMARISE
#  Read sample_grades.csv using csv.DictReader.
#  Print a summary:
#    Total students: 5
#    Highest math:   95  (Maria Lopez)
#    Lowest average: 74.25  (Laura Gomez)
# ════════════════════════════════════════════════════════════

with open("sample_grades.csv", "r") as f:
    reader = csv.DictReader(f)
    rows   = list(reader)

# TODO: calculate and print the summary


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — PANDAS FILTER CHAIN
#  Load sample_grades.csv with pandas.
#  Print students who:
#    (a) have science grade > 85
#    (b) have both math > 80 AND english > 80
#    (c) are in the top 3 by average  (use .head(3) after sorting)
# ════════════════════════════════════════════════════════════

df = pd.read_csv("sample_grades.csv")

# TODO: (a)
# TODO: (b)  hint:  df[ (cond1) & (cond2) ]
# TODO: (c)


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — SUBJECT AVERAGE
#  Calculate the class average for each subject column.
#  Print a table:
#    Subject  | Class Average
#    math     |  82.4
#    science  |  85.0
#    ...
#  Hint: df["math"].mean()  gives the average of a column.
# ════════════════════════════════════════════════════════════

subjects = ["math", "science", "english", "history"]
# TODO: loop through subjects and print each average


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — CSV WRITER: NEW REPORT
#  Create a new CSV file  class_report.csv  with columns:
#    student, strongest_subject, weakest_subject, grade
#  For each student, find their highest and lowest scoring subject.
#  Add the letter grade from the lesson template.
# ════════════════════════════════════════════════════════════

def letter_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    else: return "D"

df = pd.read_csv("sample_grades.csv")
subjects = ["math", "science", "english", "history"]

with open("class_report.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["student","strongest_subject","weakest_subject","grade"])
    writer.writeheader()
    for _, row in df.iterrows():
        # TODO: find strongest and weakest subject using max/min on the subjects list
        # TODO: write the row to the CSV
        pass

print("class_report.csv written.")


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: GRADE IMPROVEMENT TRACKER
#  Create a second CSV  grades_updated.csv  manually with
#  the same students but different scores (imagine a second exam).
#  Load both CSVs and merge them using pandas:
#    pd.merge(df1, df2, on="student", suffixes=("_exam1", "_exam2"))
#  Calculate the improvement in average for each student.
#  Print who improved most and who dropped most.
# ════════════════════════════════════════════════════════════

# TODO: create grades_updated.csv manually, then merge and analyse
