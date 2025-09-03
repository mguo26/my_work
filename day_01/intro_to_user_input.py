"""
Lesson: Loops, Conditionals, and User Input
-------------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how programs can respond to user input.
"""

# --- Section 1: Getting Input from the User ---

# TODO: Ask the user for their name and store it in a variable
name = input("enter your name: ")

# TODO: Ask the user for their age and store it as an integer

age = int(input("enter your age: "))

# Print out a greeting
print("Hello,", name)
print("You are", age, "years old")


# --- Section 2: Conditionals with Input ---

# TODO: Check if the user is old enough to vote (18+)
if age>=18:
   print("You can vote!")
else:
     print("You cannot vote yet.")

# TODO: Ask the user for a number and check if it's even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even number")

else:
    print("Odd number")


# --- Section 3: Loops with Input ---

# Problem: You want to ask a user for 5 test scores and print them
# without loops, you'd have to write 5 separate inputs.  

# TODO: Try writing 5 input statements manually first (commented out)
score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))
score4 = int(input("Score 4: "))
score5 = int(input("Score 5: "))



# Question: How could a loop make this easier?
#A loop lets us repeat the same input many times with fewer lines

# --- Section 4: For Loops with Input ---

# TODO: Use a for loop to ask for 5 test scores and print each one
# Example starter:
for i in range(5):
 score = int(input("Enter score #" + str(i+1) + ": "))
 print("You entered:", score)


# --- Section 5: While Loops with Input ---

# TODO: Keep asking the user to enter a positive number
# until they actually do. Use a while loop.
# Example starter:
num = int(input("Enter a positive number: "))
while num<=0:
     print("That is not positive. Try again!")
     num = int(input("Enter a positive number: "))
     print("Thank you! You entered:", num)


# --- Section 6: Challenges ---

# 1. Ask the user for a number and tell them if it's divisible by 3, 5, or both
n = int(input("Enter a number: "))
if n%3== 0 and n%5 == 0:
    print("Divisible by both 3 and 5")
elif n%3== 0: 
   print("Divisible by 3")
elif n%5== 0:
   print("Divisible by 5")
else:
   print("Not divisible by 3 or 5")

# 2. Ask the user for their favorite color repeatedly until they type "stop"

# 3. Create a mini grading program:
#     - Ask the user for scores until they type -1
#     - Keep track of how many scores are passing (>= 60)
#     - Print a summary at the end
passing = 0
total = 0
score = int(input("Enter a score (or -1 to stop): "))
while score != -1:
    if score >= 60:
        passing += 1
    total += 1
    score = int(input("Enter another score (or -1 to stop): "))

print("You entered", total, "scores.")
print(passing, "of them were passing.")


# --- Section 7: Reflection ---
# 1. How does using input change the way your program works compared to fixed variables?
# A: It makes the program interactive — the user controls the values instead of being hardcoded.
#
# 2. How do loops and conditionals work together when handling user input?
# A: Loops let the program keep asking for input, and conditionals decide how to respond to that input.
#
# 3. What are some real-world programs where loops + conditionals + input are all necessary?
# A: ATMs, online quizzes, password login systems, surveys, calculators, and games.
