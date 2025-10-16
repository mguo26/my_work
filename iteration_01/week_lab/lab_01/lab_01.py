def main():
    all_users = []

    while True:
        name = input("Enter your name: ").strip().title()
        age = int(input("Enter your age: "))
        multilingual = input("Are you multilingual? (Yes/No): ").strip().capitalize()

        # user_data dictionary with clearer structure
        user_data = {
            "name": name,
            "age": age,
            "multilingual": multilingual,
            "languages_spoken": [],
            "language_to_learn": None
        }

        print(f"\nHello {name}, welcome to the program!\n")

        # age-based rules
        if age < 13:
            print("You cannot sit in the passenger seat of a car.")
        if age < 18:
            print("You cannot vote.")
        if age < 25:
            print("You cannot rent a car.")
        if age > 35:
            print("You are getting old...")

        # language info section
        if multilingual == "Yes":
            num_langs = int(input("How many languages do you speak? "))
            for i in range(num_langs):
                lang = input(f"Enter language #{i + 1}: ").strip().title()
                user_data["languages_spoken"].append(lang)
            print(f"You speak: {', '.join(user_data['languages_spoken'])}")
        else:
            wish_lang = input("What language do you wish to learn? ").strip().title()
            user_data["language_to_learn"] = wish_lang
            print(f"You wish to learn: {wish_lang}")

        all_users.append(user_data)

        another = input("\nWould another user like to enter their info? (Yes/No): ").strip().capitalize()
        if another != "Yes":
            break

    print("\nAll users' information collected:\n")
    for user in all_users:
        print(user)


if __name__ == "__main__":
    main()
