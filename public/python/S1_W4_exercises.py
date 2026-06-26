# ============================================================
#  SPRINT 1 · WEEK 4 — Exercise Set
#  Topic: for loops, while loops, range(), break, continue
# ============================================================


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SPOT THE BUG  (3 errors)
# ════════════════════════════════════════════════════════════

# total = 0
# for i in range(1, 11)     # Bug 1
#     total = total + i
#
# count = 0
# while count < 5
#     print(count)          # Bug 2: prints 0-4 but should print 1-5
#     count += 1
#
# for i in range(10):
#     if i == 5:
#         break             # Bug 3: should skip 5 but keep going, not stop
#     print(i)


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — TIMES TABLES
#  Ask for a number, print its times table from 1 to 12.
#  Example for 7:
#    7 x  1 =  7
#    7 x  2 = 14
#    ...
#    7 x 12 = 84
# ════════════════════════════════════════════════════════════

n = int(input("Which times table? "))

# TODO: write a for loop using range(1, 13)


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — FIZZBUZZ
#  Print numbers 1 to 30.
#  BUT: if divisible by 3, print "Fizz" instead.
#       if divisible by 5, print "Buzz" instead.
#       if divisible by BOTH, print "FizzBuzz".
#  Hint: the modulo operator  %  gives the remainder.
#        12 % 3 == 0  means 12 is divisible by 3.
#  Important: check the "both" case FIRST in your if chain.
# ════════════════════════════════════════════════════════════

for i in range(1, 31):
    # TODO: write the FizzBuzz logic here
    pass  # delete this line when you write your code


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — STAR PYRAMID
#  Print a triangle of stars using nested loops.
#  Expected output (5 rows):
#    *
#    **
#    ***
#    ****
#    *****
#  Hint: the outer loop goes from 1 to 5.
#        the inner loop prints "*" that many times.
#        print("*" * i)  works in one line!
# ════════════════════════════════════════════════════════════

rows = int(input("How many rows? "))

# TODO: write the nested loop (or use the one-liner trick)


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: SUM UNTIL
#  Keep asking the user to enter numbers.
#  Add each one to a running total.
#  Stop when the total exceeds 100.
#  Print how many numbers it took and what the total is.
#
#  Bonus: also track the highest number entered.
# ════════════════════════════════════════════════════════════

total = 0
count = 0
highest = 0

# TODO: write the while loop
