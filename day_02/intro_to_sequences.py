"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["icecream", "sushi", "korean food"]

# Access items by index (first = 0):

print(f"The first food is {foods[0]}")
print(f"The last food is {foods[-1]}")


# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?

# A list index is out of range, it means that I don't have that many foods listed

# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()

foods.append("ramen")

print(foods)

# TODO: Insert a food at the beginning with .insert()

foods.insert(0,"tacos")
print(foods)

# TODO: Remove one food from the list with .remove()

foods.remove("icecream")
print(foods)

# TODO: How many foods are in the list? Use len()

print(len(foods))


# Bug Exploration:
# Try removing something that isn’t in the list:

# Q: What happens? Why?

# x not in list


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.

list= ["icecream", "sushi", "korean food", "rame"] 

print (list)

# Bug Exploration:
# Change your loop to go past the length of the list:


# Q: Why does this cause an error?

# A: because list is out of range? 

# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 

me = {
    "name": "mia",
    "age": 17,
    "student": True
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.



# Access values using keys by using the .get() method rather than indexing


# print(f"My name is {me['name']}")
print(f"my name is {me.get('name')}")
print(f"My age is {me.get('age')}")

print(f"My favorite color is {me.get('favorite_color')}")

# Bug Exploration:
# Try printing a key that doesn’t exist.

# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?
# A: It gives a KeyError. You can check with "if 'hometown' in me". .get() is useful because it won’t crash if the key is missing.


# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.
me["favorite_color"] = "blue"

# TODO: Change the value of an existing key.
me["age"] = 18

# TODO: Remove one key-value pair.
me.pop("student")

# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?
# A: It gives a KeyError. It’s kind of like when you try to remove something from a list that isn’t there.


# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()
for key, value in me.items():
    print(f"{key}: {value}")

# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?
# A: By default it only gives keys. To get both, you need to use .items().


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.
friends = [
    {"name": "Alex", "food": "ramen"},
    {"name": "Sam", "food": "pizza"},
    {"name": "Taylor", "food": "sushi"}
]

# TODO: Print the favorite food of the second friend.
print(friends[1]["food"])

# TODO: Loop through and print "<name> likes <food>" for each friend.
for friend in friends:
    print(f"{friend['name']} likes {friend['food']}")

# Bug Exploration:
# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?
# A: You’d get a KeyError. You can avoid it by using .get() or checking if the key is there first.


# --- Section 8: Reflection ---
# 1. How is a list different from a dictionary?
#    - A list uses numbers to find stuff. A dictionary uses keys (labels).
# 2. When would you want to use a dictionary instead of a list?
#    - When you want to label things instead of just using numbers.
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
#    - A class list: each student could be a dictionary with their info, and the whole group is a list.
# 4. What types of mistakes gave you the most errors today?
#    - IndexError and KeyError (trying to get something that isn’t there).
# 5. How might noticing errors actually help you learn?
#    - Errors show you exactly what went wrong, so you can fix it and understand better next time.
