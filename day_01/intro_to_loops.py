"""
Lesson: Data Types, Variables, and Why Loops Are Necessary
----------------------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice patterns.
"""

# --- Section 1: Variables and Data Types ---

# TODO: Create a variable called name that stores your name
Name = "mia"
# TODO: Create a variable called age that stores your age
Age = 17
# TODO: Create a variable called pi that stores the value 3.14159
Pi = 3.14159

# Print each variable
print("Name:", Name)
print("Age:",Age)
print("Pi:", Pi)


# --- Section 2: Why Loops? ---

# Imagine you want to print the numbers 1 through 10.
# First, try it the "long way".

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# TODO: Keep going until you reach 10

# Question for you:
#   What happens if I want to print 1 through 100? Or 1 through 1000?
#A takes a long time a inefficient
#   Is it realistic to keep writing print statements forever?
# no


# --- Section 3: For Loops ---
# TODO: Replace the repeated print statements above with a for loop.

# Example starter (fill in the blanks):
# for ___ in ___:
#     print(___)

for i in range(1,11): 
    print (i) 

# Hint: What does range(start, stop) do?


# --- Section 4: While Loops ---
# A while loop repeats until a CONDITION is no longer true.

# TODO: Try to print numbers 1 through 10 using a while loop.
x=1
while x<= 10:
    print(x)
    x+=1

# Example starter:
# x = 1
# while ___:
#     print(___)
#     # TODO: Don’t forget to change x, or your loop will run forever!
x = 1
while x <= 10:
    print(x)
    x += 1   # don’t forget to increment, or loop will never stop!


# --- Section 5: Reflection ---
# 1. Why is a loop better than writing 100 print statements?
# A: Because loops make the code shorter and easier to read.
# 2. What does a loop REQUIRE in order to work?
# A: A starting value, a condition that tells it when to stop, and something that changes so it ends.
