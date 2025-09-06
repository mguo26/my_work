
all_users= []

while True: 

    name = input("Enter your name: ") 

    age = int(input("Enter your age: ") )

    multilingual = input("Are you multilingual?: ") 

    data = {
        "name" : name,
        "age" : age,
        "multilingual" : multilingual,
        "languages": []

    }
    print(f"Hello! Welcome to the program, {data['name']}!")

    if data["age"] < 13:
        print("You can not sit in the passenger seat of a car.")

    if data["age"] < 18:
        print("You can not vote.")

    if data["age"] < 25:
        print("You can not rent a car.")

    if data["age"] > 35:
        print("You're getting old.")

    if multilingual == "yes":
        num_langs = int(input("How many languages do you speak?"))
        for i in range (num_langs):
            lang = input(f"Enter language #{i+1}:")
            data ["languages"].append(lang)
    else:
        lang = input("What language would you like to learn? ")
        data["languages"].append(f"Wants to learn {lang}")
        print(f"Great choice! You want to learn {lang}.")
    all_users.append(data)

    another = input("\nWould another user like to enter their information? (yes/no): ").strip().lower()
    if another != "yes":
        break
    
print("\nAll user data collected:")
for user in all_users:
    print(user) 