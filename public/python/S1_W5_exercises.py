# ============================================================
#  SPRINT 1 · WEEK 5 — Exercise Set
#  Topic: def, return, parameters, scope, if __name__
# ============================================================


# ════════════════════════════════════════════════════════════
#  EXERCISE 1 — SPOT THE BUG  (3 errors)
# ════════════════════════════════════════════════════════════

# def add(a, b)        # Bug 1
#     return a + b
#
# result = add(3, 4)
# print(result)
#
# def square(n):
#     answer = n * n
#
# print(square(5))     # Bug 2: prints None — why?
#
# x = 10
# def double():
#     x = x * 2       # Bug 3: scope error — what is the fix?
#     return x
# print(double())


# ════════════════════════════════════════════════════════════
#  EXERCISE 2 — CALCULATOR FUNCTIONS
#  Write four functions: add, subtract, multiply, divide.
#  Each takes two parameters and returns the result.
#  divide should check for division by zero and return None if so.
#  Then write a main() that shows a menu and calls the right function.
# ════════════════════════════════════════════════════════════

def add(a, b):
    return TODO   # TODO: return the sum

def subtract(a, b):
    return TODO   # TODO: return the difference

def multiply(a, b):
    pass          # TODO: write this function completely

def divide(a, b):
    pass          # TODO: write this function, handle zero division


# ════════════════════════════════════════════════════════════
#  EXERCISE 3 — IS_EVEN / IS_ODD
#  Write a function  is_even(n)  that returns True if n is even,
#  False otherwise.
#  Write is_odd(n) that calls is_even and returns the opposite.
#  Test with 10 different numbers using a for loop.
# ════════════════════════════════════════════════════════════

def is_even(n):
    pass  # TODO: use the % operator

def is_odd(n):
    pass  # TODO: call is_even and flip the result


# ════════════════════════════════════════════════════════════
#  EXERCISE 4 — REFACTOR THIS
#  The code below works but repeats itself badly.
#  Rewrite it using a single function  greet_user(name, lang)
#  that prints in the right language.
# ════════════════════════════════════════════════════════════

# Original (messy) code — do not run this block, just read it:
# print("Hello, Ana!")
# print("Hola, Sofia!")
# print("Bonjour, Maria!")
# print("Hello, Laura!")
# print("Hola, Valentina!")

# TODO: write greet_user(name, lang) and call it 5 times


# ════════════════════════════════════════════════════════════
#  EXERCISE 5 — ULTRA CHALLENGE: RECURSION PREVIEW
#  A function can call itself! This is called recursion.
#  Write a function  countdown(n)  that:
#    - prints n
#    - calls countdown(n - 1)
#    - stops when n reaches 0  (base case — essential to avoid infinite loop)
#  Then write  factorial(n)  that returns n! = n * (n-1) * ... * 1
#  Example: factorial(5) = 120
# ════════════════════════════════════════════════════════════

def countdown(n):
    if n <= 0:
        print("Blast off!")
        return
    # TODO: print n and call countdown(n - 1)

def factorial(n):
    if n <= 1:
        return 1
    # TODO: return n multiplied by factorial(n - 1)
