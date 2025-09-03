"""
Lesson: Conditionals in Python
------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how conditionals change what happens.
"""

# --- Section 1: True or False? (Boolean Expressions) ---

# Conditionals always depend on something being True or False.
# Let's explore.

# TODO: Create two variables. One that represents age, and the other a boolean that is True if you are a student and false if you are not:
age = 17
is_student = True

# What happens when we compare numbers?

print("Is age greater than 18?", age > 18)
print("Is age less than 13?", age < 13)


# What happens when we compare equality?
print("Is age exactly 16?", age == 16)

# What happens when we use a variable directly?
print("Is student status True?", is_student)

# Reflection Question (write your answer in a comment):
# Q: Why do all of these print either True or False?
# A: Because boolean values always evaluate to true or faulse 


# --- Section 2: If Statements ---

# Problem: You want to check if someone can vote (age >= 18).
# First, try without conditionals (just print something no matter what).

 # TODO: What’s wrong with this approach?

#"it prints you can vote no matter the age"

if age >= 18:
    print("You can vote!")
else:
    print("Sorry, you are too young to vote.")


# Now add an IF statement:
# if ___:
#     print("You can vote!")



# --- Section 3: If/Else ---

# TODO: Write a program that checks if a number is even or odd.
# Steps to guide you:
# 1. Make a variable called num
# 2. Use the modulo operator (%) to check if num % 2 == 0
# 3. If even, print "Even number"
# 4. Otherwise, print "Odd number"

num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# --- Section 4: If / Elif / Else ---

# TODO: Imagine a grading system:
#   - 90 or above → "A"
#   - 80 or above → "B"
#   - 70 or above → "C"
#   - 60 or above → "D"
#   - below 60   → "F"

# Write this using if / elif / else statements.

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)



# --- Section 5: Nesting Conditionals ---

# TODO: Ask two questions:
#   1. Is the person a student?
#   2. Is their age under 18?
# If both are true, print "You are a student and a minor."
# Otherwise, print something else.

if is_student and age < 18:
    print("You are a student and a minor.")
else:
    print("Condition not met.")


# --- Section 6: Reflection ---
# 1. What does a conditional REQUIRE in order to run effectively?
# A: A condition that can evaluate to True or False.
#
# 2. How do elif and else make your code shorter or more readable?
# A: You don't have to writ multiple separate if statements and makes sure that only one block runs.
#
# 3. Can you think of a situation in real life where you’d use multiple conditionals?
# A: Deciding what to wear based on the weather. if it’s raining wear a raincoat, elif it’s cold wear a jacket, else wear a tshirt.
