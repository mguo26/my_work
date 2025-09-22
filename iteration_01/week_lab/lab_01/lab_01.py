def main():
    all_users = []
    
    while True:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        multilingual = input("Are you multilingual? (Yes/No): ")
        
        user_data = {
            "name": name,
            "age": age,
            "multilingual": multilingual,
            "languages": []
        }
        
        print(f"\nHello {name}, welcome to the program!\n")
        
        if age < 13:
            print("You cannot sit in the passenger seat of a car.")
        if age < 18:
            print("You cannot vote.")
        if age < 25:
            print("You cannot rent a car.")
        if age > 35:
            print("You are getting old...")
        
        if multilingual == "Yes":
            num_langs = int(input("How many languages do you speak? "))
            for i in range(num_langs):
                lang = input(f"Enter language #{i+1}: ")
                user_data["languages"].append(lang)
            print(f"You speak: {', '.join(user_data['languages'])}")
        else:
            wish_lang = input("What language do you wish to learn? ")
            user_data["languages"].append(f"Wish to learn: {wish_lang}")
            print(f"You wish to learn: {wish_lang}")
        
        all_users.append(user_data)
        
        another = input("\nWould another user like to enter their info? (Yes/No): ")
        if another != "Yes":
            break
    
    print("\nAll users' information collected:")
    for user in all_users:
        print(user)


if __name__ == "__main__":
    main()
